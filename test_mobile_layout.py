#!/usr/bin/env python3
"""
Mobile Layout Verification Script
Tests the actual mobile layout to ensure map is 1/4 of screen height
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

def setup_mobile_driver():
    """Setup Chrome driver with mobile emulation"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in background
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    
    # Mobile device emulation
    mobile_emulation = {
        "deviceMetrics": {
            "width": 375,  # iPhone X width
            "height": 812,  # iPhone X height
            "pixelRatio": 3.0
        },
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def measure_layout(driver, url):
    """Measure the actual layout dimensions"""
    driver.get(url)
    time.sleep(3)  # Wait for page to load
    
    try:
        # Get viewport dimensions
        viewport_height = driver.execute_script("return window.innerHeight")
        viewport_width = driver.execute_script("return window.innerWidth")
        
        # Find map container
        map_container = driver.find_element(By.CLASS_NAME, "map-container")
        map_rect = driver.execute_script("""
            var rect = arguments[0].getBoundingClientRect();
            return {
                top: rect.top,
                left: rect.left,
                width: rect.width,
                height: rect.height,
                bottom: rect.bottom,
                right: rect.right
            };
        """, map_container)
        
        # Find note container
        note_container = driver.find_element(By.CLASS_NAME, "note-container")
        note_rect = driver.execute_script("""
            var rect = arguments[0].getBoundingClientRect();
            return {
                top: rect.top,
                left: rect.left,
                width: rect.width,
                height: rect.height,
                bottom: rect.bottom,
                right: rect.right
            };
        """, note_container)
        
        # Calculate percentages
        map_height_pct = (map_rect['height'] / viewport_height) * 100
        note_height_pct = (note_rect['height'] / viewport_height) * 100
        
        return {
            'viewport': {'width': viewport_width, 'height': viewport_height},
            'map': map_rect,
            'note': note_rect,
            'map_height_pct': map_height_pct,
            'note_height_pct': note_height_pct,
            'is_quarter': abs(map_height_pct - 25.0) < 2.0  # Within 2% of 25%
        }
        
    except Exception as e:
        print(f"Error measuring layout: {e}")
        return None

def test_different_screen_sizes():
    """Test different mobile screen sizes"""
    screen_sizes = [
        {"width": 375, "height": 812, "name": "iPhone X"},
        {"width": 414, "height": 896, "name": "iPhone 11"},
        {"width": 360, "height": 640, "name": "Small Android"},
        {"width": 320, "height": 568, "name": "iPhone SE"}
    ]
    
    driver = setup_mobile_driver()
    results = {}
    
    try:
        for size in screen_sizes:
            print(f"\nTesting {size['name']} ({size['width']}x{size['height']})")
            
            # Update mobile emulation
            driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {
                'width': size['width'],
                'height': size['height'],
                'deviceScaleFactor': 2.0,
                'mobile': True
            })
            
            # Measure layout
            layout = measure_layout(driver, "http://localhost:5173")
            if layout:
                results[size['name']] = layout
                print(f"  Map height: {layout['map_height_pct']:.1f}% (target: 25%)")
                print(f"  Note height: {layout['note_height_pct']:.1f}%")
                print(f"  Is quarter: {layout['is_quarter']}")
            else:
                print(f"  Failed to measure layout")
                
    finally:
        driver.quit()
    
    return results

def generate_css_fix(results):
    """Generate CSS fixes based on measurements"""
    print("\n" + "="*50)
    print("MOBILE LAYOUT ANALYSIS")
    print("="*50)
    
    for device, data in results.items():
        print(f"\n{device}:")
        print(f"  Map: {data['map_height_pct']:.1f}% (target: 25%)")
        print(f"  Note: {data['note_height_pct']:.1f}%")
        
        if not data['is_quarter']:
            current_map_pct = data['map_height_pct']
            target_pct = 25.0
            ratio = target_pct / current_map_pct
            
            print(f"  Fix needed: Reduce map height by {ratio:.2f}x")
            print(f"  Suggested CSS: height: {25/ratio:.1f}vh")

if __name__ == "__main__":
    print("Starting mobile layout verification...")
    print("Make sure the server is running on http://localhost:5173")
    
    results = test_different_screen_sizes()
    generate_css_fix(results)
    
    # Save results to file
    with open('mobile_layout_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to mobile_layout_results.json")
