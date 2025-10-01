#!/usr/bin/env python3
"""
Iterate until mobile layout is correct
"""

import subprocess
import time
import json
import os

def run_test():
    """Run the mobile layout test"""
    try:
        result = subprocess.run(['python3', 'test_mobile_layout.py'], 
                              capture_output=True, text=True, timeout=30)
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print("Test timed out")
        return False
    except Exception as e:
        print(f"Error running test: {e}")
        return False

def check_results():
    """Check if we've achieved the target"""
    try:
        with open('mobile_layout_results.json', 'r') as f:
            results = json.load(f)
        
        all_good = True
        for device, data in results.items():
            map_pct = data['map_height_pct']
            if abs(map_pct - 25.0) > 2.0:  # More than 2% off
                print(f"{device}: Map is {map_pct:.1f}% (target: 25%)")
                all_good = False
            else:
                print(f"{device}: ✓ Map is {map_pct:.1f}% (good!)")
        
        return all_good
    except FileNotFoundError:
        print("No results file found")
        return False

def apply_fix():
    """Apply CSS fix"""
    try:
        result = subprocess.run(['python3', 'fix_mobile_css.py'], 
                              capture_output=True, text=True)
        return result.returncode == 0
    except Exception as e:
        print(f"Error applying fix: {e}")
        return False

def main():
    print("Starting mobile layout iteration...")
    print("Make sure the server is running: python3 -m http.server 5173")
    
    max_iterations = 5
    iteration = 0
    
    while iteration < max_iterations:
        iteration += 1
        print(f"\n--- Iteration {iteration} ---")
        
        # Run test
        print("Running mobile layout test...")
        if not run_test():
            print("Test failed, stopping")
            break
        
        # Check results
        print("Checking results...")
        if check_results():
            print("\n🎉 SUCCESS! Mobile layout is now correct!")
            break
        
        # Apply fix
        print("Applying CSS fix...")
        if not apply_fix():
            print("Fix failed, stopping")
            break
        
        print("Waiting 2 seconds before next iteration...")
        time.sleep(2)
    
    if iteration >= max_iterations:
        print(f"\n⚠️  Reached maximum iterations ({max_iterations})")
        print("Check the results manually")

if __name__ == "__main__":
    main()
