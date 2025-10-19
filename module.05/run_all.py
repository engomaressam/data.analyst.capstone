"""
Module 05: Run All Dashboards
==============================

Quick script to generate all dashboards and outputs.
Run this to create everything at once!

Usage: python run_all.py
"""

import os
import sys
import subprocess

def run_script(script_name, description):
    """Run a Python script and report status."""
    print("\n" + "="*70)
    print(f"Running: {description}")
    print("="*70)
    
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            capture_output=False,
            text=True,
            check=True
        )
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running {script_name}")
        print(f"Error: {e}")
        return False
    except FileNotFoundError:
        print(f"❌ Script not found: {script_name}")
        return False

def main():
    """Run all dashboard generation scripts."""
    print("\n" + "="*70)
    print("MODULE 05: DASHBOARD CREATION - COMPLETE PIPELINE")
    print("="*70)
    print("\nThis will generate:")
    print("  • 3 Interactive HTML dashboards")
    print("  • 3 High-resolution PNG images")
    print("  • 1 Professional PDF presentation")
    print("  • 1 Combined web dashboard")
    print("\n" + "="*70)
    
    # Check if we're in the right directory
    if not os.path.exists('dashboard_builder.py'):
        print("\n❌ Error: Please run this script from the module.05 directory")
        print("Usage: cd module.05 && python run_all.py")
        return
    
    # Create outputs directory
    os.makedirs('outputs', exist_ok=True)
    
    # Run all scripts in sequence
    scripts = [
        ('dashboard_builder.py', 'Dashboard Builder'),
        ('pdf_generator.py', 'PDF Presentation Generator'),
        ('create_html_dashboard.py', 'HTML Dashboard Creator')
    ]
    
    results = []
    for script, description in scripts:
        success = run_script(script, description)
        results.append((description, success))
    
    # Summary
    print("\n" + "="*70)
    print("EXECUTION SUMMARY")
    print("="*70)
    
    for description, success in results:
        status = "✅ SUCCESS" if success else "❌ FAILED"
        print(f"{status}: {description}")
    
    all_success = all(success for _, success in results)
    
    if all_success:
        print("\n" + "="*70)
        print("🎉 ALL DASHBOARDS GENERATED SUCCESSFULLY!")
        print("="*70)
        print("\nGenerated files in ./outputs/:")
        print("  • dashboard_1_current_tech.html")
        print("  • dashboard_1_current_tech.png")
        print("  • dashboard_2_future_tech.html")
        print("  • dashboard_2_future_tech.png")
        print("  • dashboard_3_demographics.html")
        print("  • dashboard_3_demographics.png")
        print("  • Dashboard_Presentation.pdf")
        print("  • Interactive_Dashboard.html")
        print("\nTo view:")
        print("  • Open Interactive_Dashboard.html in your browser")
        print("  • View Dashboard_Presentation.pdf for formal presentation")
        print("="*70)
    else:
        print("\n❌ Some scripts failed. Check error messages above.")

if __name__ == "__main__":
    main()
