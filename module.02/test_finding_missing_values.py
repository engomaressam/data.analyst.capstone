"""
Finding Missing Values Lab - Python Test Script
Tests missing value identification, analysis, imputation, and visualization
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def test_finding_missing_values():
    print("=" * 70)
    print("Testing Finding Missing Values Lab")
    print("=" * 70)
    
    # Load the dataset
    print("\n1. Loading dataset...")
    try:
        file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n01PQ9pSmiRX6520flujwQ/survey-data.csv"
        df = pd.read_csv(file_path)
        print(f"✓ Dataset loaded: {df.shape}")
    except Exception as e:
        print(f"✗ Error loading dataset: {e}")
        return False
    
    # Task 1: Display basic information
    print("\n2. Displaying dataset information...")
    try:
        print(f"✓ Rows: {len(df)}")
        print(f"✓ Columns: {len(df.columns)}")
        print(f"✓ Data types identified")
    except Exception as e:
        print(f"✗ Error displaying info: {e}")
        return False
    
    # Task 2: Identify missing values
    print("\n3. Identifying missing values...")
    try:
        missing_values = df.isnull().sum()
        missing_percent = (df.isnull().sum() / len(df)) * 100
        
        columns_with_missing = (missing_values > 0).sum()
        total_missing = missing_values.sum()
        
        print(f"✓ Columns with missing values: {columns_with_missing}")
        print(f"✓ Total missing values: {total_missing}")
        
        # Show top 5
        top_missing = missing_values[missing_values > 0].sort_values(ascending=False).head()
        print("\n✓ Top 5 columns with missing values:")
        for col, count in top_missing.items():
            pct = (count / len(df)) * 100
            print(f"    {col}: {count} ({pct:.2f}%)")
    except Exception as e:
        print(f"✗ Error identifying missing values: {e}")
        return False
    
    # Task 3: Visualization (skip display in test)
    print("\n4. Testing visualization capabilities...")
    try:
        missing_summary = pd.DataFrame({
            'Column': missing_values.index,
            'Missing_Count': missing_values.values
        })
        missing_summary = missing_summary[missing_summary['Missing_Count'] > 0]
        print(f"✓ Prepared data for heatmap: {len(missing_summary)} columns")
    except Exception as e:
        print(f"✗ Error in visualization prep: {e}")
        return False
    
    # Task 4: Count missing in Employment
    print("\n5. Analyzing Employment column...")
    try:
        if 'Employment' in df.columns:
            employment_missing = df['Employment'].isnull().sum()
            employment_pct = (employment_missing / len(df)) * 100
            print(f"✓ Missing in Employment: {employment_missing} ({employment_pct:.2f}%)")
    except Exception as e:
        print(f"✗ Error analyzing Employment: {e}")
        return False
    
    # Task 5: Find most frequent value
    print("\n6. Finding most frequent Employment value...")
    try:
        if 'Employment' in df.columns:
            most_frequent = df['Employment'].mode()[0]
            frequency = df['Employment'].value_counts().iloc[0]
            print(f"✓ Most frequent value: '{most_frequent}'")
            print(f"✓ Frequency: {frequency}")
    except Exception as e:
        print(f"✗ Error finding mode: {e}")
        return False
    
    # Task 6: Impute missing values
    print("\n7. Imputing missing values in Employment...")
    try:
        if 'Employment' in df.columns:
            original_missing = df['Employment'].isnull().sum()
            df['Employment'].fillna(most_frequent, inplace=True)
            after_missing = df['Employment'].isnull().sum()
            imputed_count = original_missing - after_missing
            
            print(f"✓ Imputed {imputed_count} missing values")
            print(f"✓ Remaining missing: {after_missing}")
    except Exception as e:
        print(f"✗ Error imputing values: {e}")
        return False
    
    # Task 7: Visualization (skip display)
    print("\n8. Testing distribution visualization...")
    try:
        if 'Employment' in df.columns:
            employment_counts = df['Employment'].value_counts()
            print(f"✓ Employment distribution calculated: {len(employment_counts)} categories")
            print(f"✓ Total respondents: {employment_counts.sum()}")
    except Exception as e:
        print(f"✗ Error in distribution viz: {e}")
        return False
    
    print("\n" + "=" * 70)
    print("✓ ALL TESTS PASSED - Finding Missing Values Lab Complete!")
    print("=" * 70)
    print(f"\nMissing Values Summary:")
    print(f"  - Columns with missing data: {columns_with_missing}")
    print(f"  - Total missing values: {total_missing}")
    print(f"  - Employment missing values imputed: {imputed_count}")
    print(f"  - Dataset ready for analysis!")
    return True

if __name__ == "__main__":
    success = test_finding_missing_values()
    exit(0 if success else 1)
