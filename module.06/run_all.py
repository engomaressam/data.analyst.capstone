"""
Module 06: Run All - Complete Pipeline
=======================================

Executes all scripts to generate the final presentation.
One-click generation of all deliverables.

Usage: python run_all.py

Author: Diaa
Date: October 2025
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
    """Run complete pipeline for final presentation generation."""
    print("\n" + "="*70)
    print("MODULE 06: FINAL PRESENTATION - COMPLETE PIPELINE")
    print("="*70)
    print("\nThis will generate:")
    print("  1. All required charts and visualizations")
    print("  2. PDF presentation (DataAnalystPresentation.pdf)")
    print("  3. HTML presentation (interactive web version)")
    print("\n" + "="*70)
    
    # Check if we're in the right directory
    if not os.path.exists('final_presentation_generator.py'):
        print("\n❌ Error: Please run this script from the module.06 directory")
        print("Usage: cd module.06 && python run_all.py")
        return
    
    # Create outputs directory
    os.makedirs('outputs', exist_ok=True)
    os.makedirs('outputs/charts', exist_ok=True)
    
    # Run all scripts in sequence
    scripts = [
        ('chart_generator.py', 'Chart Generator'),
        ('final_presentation_generator.py', 'PDF Presentation Generator'),
        ('create_html_presentation.py', 'HTML Presentation Creator')
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
        print("🎉 FINAL PRESENTATION GENERATED SUCCESSFULLY!")
        print("="*70)
        print("\nGenerated files:")
        print("\n📄 **PRIMARY SUBMISSION:**")
        print("  • outputs/DataAnalystPresentation.pdf  ⭐ SUBMIT THIS")
        print("\n📊 Supporting Files:")
        print("  • outputs/DataAnalystPresentation.html (web version)")
        print("  • outputs/charts/ (all visualizations)")
        print("\n" + "="*70)
        print("NEXT STEPS:")
        print("="*70)
        print("\n1. Review the PDF:")
        print("   - Open outputs/DataAnalystPresentation.pdf")
        print("   - Verify all slides present")
        print("   - Check for any errors")
        print("\n2. Submit for grading:")
        print("   - Upload DataAnalystPresentation.pdf to course platform")
        print("   - Complete peer review assignment")
        print("\n3. Celebrate! 🎊")
        print("   - All 6 modules complete!")
        print("   - Capstone project finished!")
        print("   - Portfolio ready for employers!")
        print("="*70)
        
        # Display file paths
        pdf_path = os.path.abspath('outputs/DataAnalystPresentation.pdf')
        html_path = os.path.abspath('outputs/DataAnalystPresentation.html')
        
        print(f"\n📍 File Locations:")
        print(f"   PDF: {pdf_path}")
        print(f"   HTML: {html_path}")
        
    else:
        print("\n❌ Some scripts failed. Check error messages above.")
        print("\nTroubleshooting:")
        print("  1. Ensure all dependencies installed: pip install -r ../requirements.txt")
        print("  2. Check that data file exists: ../data/survey_results_updated.csv")
        print("  3. Verify kaleido installed: pip install kaleido")

if __name__ == "__main__":
    main()
