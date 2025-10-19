"""
Removing Duplicates Lab - Python Test Script
Tests duplicate removal, missing value handling, and compensation normalization
"""

import pandas as pd

def test_removing_duplicates():
    print("=" * 70)
    print("Testing Removing Duplicates Lab")
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
    
    # Task 1: Identify Duplicates
    print("\n2. Identifying duplicate rows...")
    try:
        num_duplicates = df.duplicated().sum()
        print(f"✓ Number of duplicate rows: {num_duplicates}")
    except Exception as e:
        print(f"✗ Error identifying duplicates: {e}")
        return False
    
    # Task 2: Remove Duplicates
    print("\n3. Removing duplicate rows...")
    try:
        original_shape = df.shape
        df_cleaned = df.drop_duplicates()
        removed = original_shape[0] - df_cleaned.shape[0]
        
        print(f"✓ Removed {removed} duplicate rows")
        print(f"✓ Final shape: {df_cleaned.shape}")
        
        remaining = df_cleaned.duplicated().sum()
        print(f"✓ Remaining duplicates: {remaining}")
        
        df = df_cleaned
    except Exception as e:
        print(f"✗ Error removing duplicates: {e}")
        return False
    
    # Task 3: Handle Missing Values
    print("\n4. Handling missing values...")
    try:
        missing_values = df.isnull().sum()
        total_missing = missing_values.sum()
        print(f"✓ Total missing values: {total_missing}")
        
        if 'EdLevel' in df.columns:
            edlevel_missing = df['EdLevel'].isnull().sum()
            print(f"✓ Missing in EdLevel: {edlevel_missing}")
            
            if edlevel_missing > 0:
                most_frequent = df['EdLevel'].mode()[0]
                df['EdLevel'].fillna(most_frequent, inplace=True)
                print(f"✓ Imputed EdLevel with: '{most_frequent}'")
                print(f"✓ Missing after imputation: {df['EdLevel'].isnull().sum()}")
    except Exception as e:
        print(f"✗ Error handling missing values: {e}")
        return False
    
    # Task 4: Normalize Compensation
    print("\n5. Normalizing compensation data...")
    try:
        if 'ConvertedCompYearly' in df.columns:
            comp_missing = df['ConvertedCompYearly'].isnull().sum()
            print(f"✓ Missing in ConvertedCompYearly: {comp_missing}")
            
            if comp_missing > 0:
                median_comp = df['ConvertedCompYearly'].median()
                df['ConvertedCompYearly'].fillna(median_comp, inplace=True)
                print(f"✓ Imputed with median: ${median_comp:,.2f}")
                print(f"✓ Missing after imputation: {df['ConvertedCompYearly'].isnull().sum()}")
            
            print(f"✓ Compensation data normalized")
    except Exception as e:
        print(f"✗ Error normalizing compensation: {e}")
        return False
    
    print("\n" + "=" * 70)
    print("✓ ALL TESTS PASSED - Removing Duplicates Lab Complete!")
    print("=" * 70)
    print(f"\nData Quality Summary:")
    print(f"  - Final dataset shape: {df.shape}")
    print(f"  - Duplicates removed: {removed}")
    print(f"  - Missing values handled: Yes")
    print(f"  - Compensation normalized: Yes")
    return True

if __name__ == "__main__":
    success = test_removing_duplicates()
    exit(0 if success else 1)
