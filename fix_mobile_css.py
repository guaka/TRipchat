#!/usr/bin/env python3
"""
Auto-fix mobile CSS based on measurements
"""

import json
import re

def load_measurements():
    """Load measurement results"""
    try:
        with open('mobile_layout_results.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("No measurement results found. Run test_mobile_layout.py first.")
        return None

def calculate_css_fixes(results):
    """Calculate the CSS fixes needed"""
    fixes = {}
    
    for device, data in results.items():
        current_map_pct = data['map_height_pct']
        target_pct = 25.0
        
        if current_map_pct > target_pct + 2:  # More than 2% off
            ratio = target_pct / current_map_pct
            new_vh = 25.0 / ratio
            fixes[device] = {
                'current': current_map_pct,
                'target': target_pct,
                'new_vh': new_vh,
                'ratio': ratio
            }
    
    return fixes

def update_css_file(fixes):
    """Update the CSS file with fixes"""
    if not fixes:
        print("No fixes needed!")
        return
    
    # Read current CSS
    with open('index.html', 'r') as f:
        content = f.read()
    
    print("Applying CSS fixes...")
    
    # Apply fixes based on the most common issue
    avg_ratio = sum(fix['ratio'] for fix in fixes.values()) / len(fixes)
    new_vh = 25.0 / avg_ratio
    
    print(f"Average ratio: {avg_ratio:.2f}")
    print(f"New map height: {new_vh:.1f}vh")
    
    # Update 768px breakpoint
    pattern = r'(@media \(max-width: 768px\)[^}]+\.map-container\s*{[^}]+height:\s*)\d+vh'
    replacement = f'\\g<1>{new_vh:.1f}vh'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Update 480px breakpoint
    pattern = r'(@media \(max-width: 480px\)[^}]+\.map-container\s*{[^}]+height:\s*)\d+vh'
    replacement = f'\\g<1>{new_vh * 0.8:.1f}vh'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Update 360px breakpoint
    pattern = r'(@media \(max-width: 360px\)[^}]+\.map-container\s*{[^}]+height:\s*)\d+vh'
    replacement = f'\\g<1>{new_vh * 0.6:.1f}vh'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Write back to file
    with open('index.html', 'w') as f:
        f.write(content)
    
    print("CSS updated!")

def main():
    results = load_measurements()
    if not results:
        return
    
    fixes = calculate_css_fixes(results)
    if fixes:
        print("CSS fixes needed:")
        for device, fix in fixes.items():
            print(f"  {device}: {fix['current']:.1f}% -> {fix['target']:.1f}% (ratio: {fix['ratio']:.2f})")
        
        update_css_file(fixes)
    else:
        print("No CSS fixes needed - layout is already correct!")

if __name__ == "__main__":
    main()
