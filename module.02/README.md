# Module 02 - Data Wrangling

## Overview
Data wrangling involves cleaning and preparing datasets for analysis. This module covers duplicate removal, missing value analysis, and data normalization using the Stack Overflow Developer Survey dataset.

## 📁 Notebooks

### 1. Finding Duplicates Lab
**File**: `Hands-on Lab Finding Duplicates_v2.ipynb`

**What You'll Learn:**
- Identify duplicate rows in datasets
- Analyze characteristics of duplicates
- Visualize duplicate distribution
- Strategically remove duplicates

**Key Tasks:**
- Count duplicate rows
- Analyze duplicates based on subset columns (MainBranch, Employment, RemoteWork)
- Create bar and pie charts for visualization
- Remove duplicates using ResponseId as unique identifier

### 2. Removing Duplicates Lab
**File**: `Hands-on Lab 7 Removing Duplicates_v2.ipynb`

**What You'll Learn:**
- Remove duplicate rows efficiently
- Handle missing values appropriately
- Normalize compensation data

**Key Tasks:**
- Use `drop_duplicates()` function
- Impute EdLevel with most frequent value
- Normalize ConvertedCompYearly compensation data
- Handle missing values in critical columns

### 3. Finding Missing Values Lab
**File**: `Hands-on Lab 8 Finding Missing Values.ipynb`

**What You'll Learn:**
- Identify missing values comprehensively
- Quantify missing data patterns
- Impute missing values strategically
- Visualize data quality issues

**Key Tasks:**
- Display dataset information and summary statistics
- Identify missing values for all columns
- Create heatmap visualization of missing data
- Impute Employment column with mode value
- Visualize distributions after imputation

## 📊 Datasets

### Primary Dataset
- **URL**: `https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/VYPrOu0Vs3I0hKLLjiPGrA/survey-data-with-duplicate.csv`
- **Rows**: 65,457 (with duplicates)
- **Columns**: 114
- **Source**: Stack Overflow Developer Survey 2024

### Clean Dataset
- **URL**: `https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n01PQ9pSmiRX6520flujwQ/survey-data.csv`
- **Rows**: 65,437 (duplicates removed)
- **Columns**: 114

## 🛠️ Installation

```powershell
# Install required libraries
pip install pandas matplotlib seaborn jupyter
```

## 🚀 Quick Start

### Option 1: Run Tests
```powershell
# Navigate to module folder
cd "c:\Users\Diaa\data.analyst.capstone\module.02"

# Run all tests
python run_all_tests.py
```

### Option 2: Run Notebooks
```powershell
# Start Jupyter Notebook
jupyter notebook

# Open and run notebooks in order:
# 1. Hands-on Lab Finding Duplicates_v2.ipynb
# 2. Hands-on Lab 7 Removing Duplicates_v2.ipynb
# 3. Hands-on Lab 8 Finding Missing Values.ipynb
```

## 📈 Expected Results

### Finding Duplicates
- **Duplicates Found**: 20 rows
- **Duplicates Removed**: 20 rows
- **Final Dataset**: 65,437 rows
- **Visualizations**: 4 charts (Country, Employment, RemoteWork, MainBranch)

### Removing Duplicates
- **EdLevel Imputed**: 4,653 missing values
- **Compensation Normalized**: 42,002 values imputed
- **Median Compensation**: $65,000
- **Data Quality**: Ready for analysis

### Finding Missing Values
- **Total Missing**: 2,890,957 values
- **Columns with Missing**: 109 out of 114
- **Employment Missing**: 0 (complete data)
- **Visualizations**: Heatmap + distribution charts

## 🎯 Learning Objectives

After completing this module, you will be able to:

1. Identify and count duplicate rows
2. Analyze duplicate characteristics
3. Remove duplicates strategically
4. Identify missing values across all columns
5. Quantify missing data patterns
6. Apply appropriate imputation techniques
7. Normalize numerical data
8. Create visualizations for data quality
9. Document data wrangling processes
10. Validate data cleaning results

## 📝 Checklist Completion

### Finding Duplicates (6 items)
- ✅ Identified columns with same values
- ✅ Loaded data into DataFrame
- ✅ Counted duplicate rows
- ✅ Identified critical columns
- ✅ Visualized duplicates
- ✅ Downloaded dataset

### Removing Duplicates (5 items)
- ✅ Identified critical columns
- ✅ Loaded dataset
- ✅ Removed duplicates
- ✅ Identified missing values
- ✅ Normalized compensation

### Finding Missing Values (8 items)
- ✅ Identified duplicate rows
- ✅ Verified duplicates
- ✅ Removed duplicates
- ✅ Identified missing values
- ✅ Found missing in specific column
- ✅ Imputed missing values
- ✅ Created new column
- ✅ Visualized distribution

**Total: 19/19 Complete** ✅

## 🔍 Key Concepts

### Duplicate Handling
- **Exact Duplicates**: Identical rows across all columns
- **Subset Duplicates**: Identical values in specific columns
- **Keep Strategy**: 'first', 'last', or False (remove all)
- **Business Logic**: Use unique identifiers (ResponseId)

### Missing Value Types
- **MCAR**: Missing Completely At Random
- **MAR**: Missing At Random
- **MNAR**: Missing Not At Random

### Imputation Strategies
- **Mode**: Most frequent value (categorical data)
- **Mean**: Average value (normally distributed data)
- **Median**: Middle value (skewed numerical data)
- **Forward Fill**: Use previous value
- **Backward Fill**: Use next value

### Data Normalization
- **Min-Max Scaling**: Scale to [0, 1]
- **Standardization**: Z-score normalization
- **Unit Normalization**: Scale to unit length
- **Custom Normalization**: ConvertedCompYearly

## 📚 Functions Reference

### Pandas Functions Used
```python
# Duplicate handling
df.duplicated()                    # Find duplicates
df.duplicated(keep=False)          # Show all duplicates
df.drop_duplicates()               # Remove duplicates
df.drop_duplicates(subset=['col']) # Remove by column

# Missing values
df.isnull()                        # Check for missing
df.isnull().sum()                  # Count missing per column
df.fillna(value)                   # Fill missing values

# Statistics
df.mode()                          # Most frequent value
df.median()                        # Middle value
df.mean()                          # Average value
df.describe()                      # Summary statistics

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
plt.bar(), plt.pie()               # Charts
sns.heatmap()                      # Heatmap
```

## 🐛 Troubleshooting

### Issue: "File not found" error
**Solution**: Ensure you're connected to the internet. The datasets are loaded from URLs.

### Issue: Import errors
**Solution**: Install required libraries:
```powershell
pip install pandas matplotlib seaborn
```

### Issue: Visualizations not showing
**Solution**: Add this at the top of your notebook:
```python
%matplotlib inline
```

### Issue: FutureWarning about fillna
**Solution**: This is a pandas warning about future behavior. Your code will still work correctly.

## 💡 Tips for Success

1. **Run cells in order**: Notebooks build on previous cells
2. **Check data types**: Use `df.info()` to understand your data
3. **Visualize first**: Look at data before making changes
4. **Document decisions**: Explain why you chose specific methods
5. **Validate results**: Always verify your cleaning worked
6. **Save intermediate results**: Keep backups of cleaned data

## 📖 Additional Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Stack Overflow Survey](https://insights.stackoverflow.com/survey)

## 🎓 Next Steps

After completing Module 02:
1. Review the MODULE_02_COMPLETE.md for full summary
2. Proceed to Labs 9, 10, and 11 (Module 02 continuation)
3. Practice with your own datasets
4. Explore advanced imputation techniques

## ✅ Status

**Module 02 (Labs 6-8): COMPLETE**
- All notebooks filled in ✅
- All tests passing ✅
- Ready for submission ✅

---

**Last Updated**: October 19, 2025  
**Maintainer**: Data Analyst Capstone Project  
**Module**: 02 - Data Wrangling
