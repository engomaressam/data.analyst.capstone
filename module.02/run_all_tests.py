"""
Master Test Runner for Module 02
Runs all test scripts to verify notebook completeness
"""

import subprocess
import sys

def run_test(test_name, test_file):
    """Run a test file and return success status"""
    print("\n" + "=" * 70)
    print(f"RUNNING: {test_name}")
    print("=" * 70)
    
    try:
        result = subprocess.run(
            [sys.executable, test_file],
            capture_output=False,
            text=True,
            check=True
        )
        print(f"\n✓ {test_name} PASSED")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ {test_name} FAILED")
        return False

def main():
    print("=" * 70)
    print("MODULE 02 - DATA WRANGLING - COMPREHENSIVE TEST SUITE")
    print("=" * 70)
    
    tests = [
        ("Finding Duplicates Lab", "test_finding_duplicates.py"),
        ("Removing Duplicates Lab", "test_removing_duplicates.py"),
        ("Finding Missing Values Lab", "test_finding_missing_values.py"),
    ]
    
    results = []
    for test_name, test_file in tests:
        success = run_test(test_name, test_file)
        results.append((test_name, success))
    
    # Print summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    
    for test_name, success in results:
        status = "✓ PASSED" if success else "✗ FAILED"
        print(f"{test_name}: {status}")
    
    all_passed = all(success for _, success in results)
    
    print("\n" + "=" * 70)
    if all_passed:
        print("✓✓✓ ALL TESTS PASSED - MODULE 02 COMPLETE! ✓✓✓")
    else:
        print("✗✗✗ SOME TESTS FAILED - REVIEW ERRORS ABOVE ✗✗✗")
    print("=" * 70)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    exit(main())
