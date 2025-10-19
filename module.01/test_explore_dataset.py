"""
Explore Dataset Lab - Python Test Script
Tests dataset exploration and analysis capabilities
"""

import pandas as pd

def test_explore_dataset():
    print("=" * 60)
    print("Testing Explore Dataset Lab")
    print("=" * 60)
    
    # Load the dataset
    print("\n1. Loading dataset...")
    try:
        file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/VYPrOu0Vs3I0hKLLjiPGrA/survey-data-with-duplicate.csv"
        df = pd.read_csv(file_path)
        print("✓ Dataset loaded successfully")
    except Exception as e:
        print(f"✗ Error loading dataset: {e}")
        return False
    
    # Display first 5 rows
    print("\n2. Displaying first 5 rows...")
    try:
        print(df.head(5))
        print("✓ First 5 rows displayed")
    except Exception as e:
        print(f"✗ Error displaying rows: {e}")
        return False
    
    # Print number of rows
    print("\n3. Counting rows...")
    try:
        num_rows = len(df)
        print(f"✓ Number of rows: {num_rows}")
    except Exception as e:
        print(f"✗ Error counting rows: {e}")
        return False
    
    # Print number of columns
    print("\n4. Counting columns...")
    try:
        num_cols = len(df.columns)
        print(f"✓ Number of columns: {num_cols}")
    except Exception as e:
        print(f"✗ Error counting columns: {e}")
        return False
    
    # Print data types
    print("\n5. Identifying data types...")
    try:
        print("\nData types:")
        print(df.dtypes)
        print("✓ Data types identified")
    except Exception as e:
        print(f"✗ Error identifying data types: {e}")
        return False
    
    # Calculate mean age
    print("\n6. Calculating mean age...")
    try:
        # Age is categorical, need to convert to numeric
        # Map age ranges to their midpoints
        age_map = {
            'Under 18 years old': 16,
            '18-24 years old': 21,
            '25-34 years old': 29.5,
            '35-44 years old': 39.5,
            '45-54 years old': 49.5,
            '55-64 years old': 59.5,
            '65 years or older': 70,
            'Prefer not to say': None
        }
        df['Age_numeric'] = df['Age'].map(age_map)
        mean_age = df['Age_numeric'].mean()
        print(f"✓ Mean age of survey participants: {mean_age:.1f}")
    except Exception as e:
        print(f"✗ Error calculating mean age: {e}")
        return False
    
    # Count unique countries
    print("\n7. Counting unique countries...")
    try:
        unique_countries = df['Country'].nunique()
        print(f"✓ Number of unique countries: {unique_countries}")
    except Exception as e:
        print(f"✗ Error counting unique countries: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("✓ ALL TESTS PASSED - Explore Dataset Lab Complete!")
    print("=" * 60)
    print(f"\nKEY FINDINGS:")
    print(f"  - Total rows: {num_rows}")
    print(f"  - Total columns: {num_cols}")
    print(f"  - Mean age: {mean_age:.1f}")
    print(f"  - Unique countries: {unique_countries}")
    return True

if __name__ == "__main__":
    success = test_explore_dataset()
    exit(0 if success else 1)
