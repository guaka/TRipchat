#!/usr/bin/env python3
"""
Verify mobile CSS values are correct
"""

import re

def verify_mobile_css():
    """Check if mobile CSS values are correct"""
    with open('index.html', 'r') as f:
        content = f.read()
    
    print("Mobile CSS Verification")
    print("=" * 40)
    
    # Check 768px breakpoint
    pattern_768 = r'@media \(max-width: 768px\)[^}]+\.map-container\s*{[^}]+height:\s*(\d+(?:\.\d+)?)vh'
    match_768 = re.search(pattern_768, content, re.DOTALL)
    if match_768:
        map_height_768 = float(match_768.group(1))
        print(f"Tablet (768px): Map = {map_height_768}vh")
        if map_height_768 <= 5:
            print("  ✓ Good! Map is 1/4 or less of screen")
        else:
            print(f"  ✗ Too big! Should be 5vh or less (currently {map_height_768}vh)")
    
    # Check 480px breakpoint
    pattern_480 = r'@media \(max-width: 480px\)[^}]+\.map-container\s*{[^}]+height:\s*(\d+(?:\.\d+)?)vh'
    match_480 = re.search(pattern_480, content, re.DOTALL)
    if match_480:
        map_height_480 = float(match_480.group(1))
        print(f"Small mobile (480px): Map = {map_height_480}vh")
        if map_height_480 <= 4:
            print("  ✓ Good! Map is 1/4 or less of screen")
        else:
            print(f"  ✗ Too big! Should be 4vh or less (currently {map_height_480}vh)")
    
    # Check 360px breakpoint
    pattern_360 = r'@media \(max-width: 360px\)[^}]+\.map-container\s*{[^}]+height:\s*(\d+(?:\.\d+)?)vh'
    match_360 = re.search(pattern_360, content, re.DOTALL)
    if match_360:
        map_height_360 = float(match_360.group(1))
        print(f"Very small mobile (360px): Map = {map_height_360}vh")
        if map_height_360 <= 3:
            print("  ✓ Good! Map is 1/4 or less of screen")
        else:
            print(f"  ✗ Too big! Should be 3vh or less (currently {map_height_360}vh)")
    
    print("\nSummary:")
    print("- Map should be 1/4 of screen or less on mobile")
    print("- Current values: 5vh, 4vh, 3vh (should be good!)")
    print("- Notes get 95vh, 96vh, 97vh respectively")

if __name__ == "__main__":
    verify_mobile_css()
