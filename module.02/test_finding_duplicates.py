"""
Finding Duplicates Lab - Python Test Script
Tests duplicate identification, analysis, visualization, and removal
"""

import pandas as pd
import matplotlib.pyplot as plt

def test_finding_duplicates():
    print("=" * 70)
    print("Testing Finding Duplicates Lab")
    print("=" * 70)
    
    # Load the dataset
    print("\n1. Loading dataset...")
    try:
        file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/VYPrOu0Vs3I0hKLLjiPGrA/survey-data-with-duplicate.csv"
        df = pd.read_csv(file_path)
        print(f"✓ Dataset loaded: {df.shape}")
    except Exception as e:
        print(f"✗ Error loading dataset: {e}")
        return False
    
    # Task 1: Identify Duplicate Rows
    print("\n2. Identifying duplicate rows...")
    try:
        num_duplicates = df.duplicated().sum()
        print(f"✓ Number of duplicate rows: {num_duplicates}")
        
        duplicates = df[df.duplicated(keep=False)]
        print(f"✓ Total rows including all duplicates: {len(duplicates)}")
    except Exception as e:
        print(f"✗ Error identifying duplicates: {e}")
        return False
    
    # Task 2: Analyze Characteristics
    print("\n3. Analyzing duplicate characteristics...")
    try:
        subset_cols = ['MainBranch', 'Employment', 'RemoteWork']
        duplicates_subset = df[df.duplicated(subset=subset_cols, keep=False)]
        print(f"✓ Duplicate rows based on subset columns: {len(duplicates_subset)}")
    except Exception as e:
        print(f"✗ Error analyzing duplicates: {e}")
        return False
    
    # Task 3: Visualization (skip display in test)
    print("\n4. Testing visualization code...")
    try:
        # Just verify the data exists for plotting
        if 'Country' in duplicates.columns:
            country_counts = duplicates['Country'].value_counts().head(10)
            print(f"✓ Country distribution calculated: {len(country_counts)} countries")
        if 'Employment' in duplicates.columns:
            employment_counts = duplicates['Employment'].value_counts()
            print(f"✓ Employment distribution calculated: {len(employment_counts)} categories")
    except Exception as e:
        print(f"✗ Error in visualization prep: {e}")
        return False
    
    # Task 4: Strategic Removal
    print("\n5. Removing duplicates strategically...")
    try:
        critical_columns = ['ResponseId']
        df_cleaned = df.drop_duplicates(subset=critical_columns, keep='first')
        removed = df.shape[0] - df_cleaned.shape[0]
        print(f"✓ Removed {removed} duplicate rows")
        print(f"✓ Final dataset shape: {df_cleaned.shape}")
        
        remaining = df_cleaned.duplicated(subset=critical_columns).sum()
        print(f"✓ Remaining duplicates: {remaining}")
    except Exception as e:
        print(f"✗ Error removing duplicates: {e}")
        return False
    
    print("\n" + "=" * 70)
    print("✓ ALL TESTS PASSED - Finding Duplicates Lab Complete!")
    print("=" * 70)
    print(f"\nKey Results:")
    print(f"  - Original dataset: {df.shape[0]} rows")
    print(f"  - Duplicates found: {num_duplicates}")
    print(f"  - Duplicates removed: {removed}")
    print(f"  - Final dataset: {df_cleaned.shape[0]} rows")
    return True

if __name__ == "__main__":
    success = test_finding_duplicates()
    exit(0 if success else 1)
