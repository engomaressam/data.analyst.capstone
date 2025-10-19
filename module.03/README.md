# Module 03 - Exploratory Data Analysis

## Overview
Exploratory Data Analysis (EDA) is the critical process of examining datasets to discover patterns, spot anomalies, test hypotheses, and check assumptions through statistical summaries and graphical representations. This module covers comprehensive EDA techniques for the Stack Overflow Developer Survey dataset.

## 📁 Notebooks

### 1. Hands-on Lab Exploratory Data Analysis
**File**: `Hands-on Lab Exploratory Data Analysis.ipynb`

**What You'll Learn:**
- Load and preview datasets
- Handle missing values systematically
- Analyze employment status and job satisfaction
- Examine programming language trends
- Investigate remote work patterns
- Perform correlation analysis
- Create cross-tabulations

**Key Visualizations:**
- Count plots for categorical data
- Pie charts for proportions
- Scatter plots for correlations
- Stacked bar charts for relationships

### 2. Lab 11 - Finding How The Data is Distributed
**File**: `Lab 11 Finding How The Data is Distributed.ipynb`

**What You'll Learn:**
- Understand data distributions
- Compute statistical measures
- Perform correlation analysis
- Visualize distributions with histograms and KDE plots
- Compare programming languages
- Analyze remote work by region

**Statistical Techniques:**
- Pearson correlation
- Spearman correlation
- Distribution analysis
- Cross-tabulation

### 3. Lab 12 - Finding Outliers
**File**: `Lab 12 Finding Outliers.ipynb`

**What You'll Learn:**
- Detect outliers using statistical methods
- Apply IQR (Interquartile Range) method
- Use standard deviation threshold
- Create box plots for visualization
- Remove outliers appropriately
- Generate five-number summary

**Outlier Detection Methods:**
- IQR Method: Q1 - 1.5*IQR to Q3 + 1.5*IQR
- Standard Deviation: Mean ± 3σ
- Box plot visualization

### 4. Lab 13 - Finding Correlation
**File**: `Lab 13 Finding Correlation.ipynb`

**What You'll Learn:**
- Calculate correlations between variables
- Visualize correlation matrices with heatmaps
- Analyze compensation distributions
- Filter data for specific analysis
- Create scatter plots for relationships
- Compare compensation by country

**Correlation Techniques:**
- Correlation coefficients
- Heatmap visualization
- Scatter plot analysis
- Country-wise comparison

## 🎯 Learning Objectives

After completing this module, you will be able to:

1. ✅ Perform comprehensive exploratory data analysis
2. ✅ Identify and handle missing values effectively
3. ✅ Detect and remove outliers using statistical methods
4. ✅ Calculate and interpret correlations
5. ✅ Create effective visualizations for data insights
6. ✅ Analyze distributions with multiple techniques
7. ✅ Perform cross-tabulation analysis
8. ✅ Transform and aggregate data appropriately
9. ✅ Draw meaningful insights from statistical analysis
10. ✅ Document findings clearly

## 📊 Dataset

**Source**: Stack Overflow Developer Survey 2024  
**URL**: `https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n01PQ9pSmiRX6520flujwQ/survey-data.csv`  
**Rows**: ~65,437  
**Columns**: 114

### Key Columns
- **ConvertedCompYearly**: Annual compensation in USD
- **Employment**: Employment status
- **JobSat**: Job satisfaction level
- **Age**: Age range (categorical)
- **YearsCodePro**: Years of professional coding
- **EdLevel**: Education level
- **RemoteWork**: Remote work status
- **Country**: Respondent country
- **LanguageHaveWorkedWith**: Programming languages used

## 🛠️ Installation

```powershell
# Install required libraries
pip install pandas matplotlib seaborn jupyter
```

## 🚀 Quick Start

### Option 1: Run Jupyter Notebooks
```powershell
cd "C:\Users\Diaa\data.analyst.capstone\module.03"
jupyter notebook

# Run notebooks in order:
# 1. Hands-on Lab Exploratory Data Analysis.ipynb
# 2. Lab 11 Finding How The Data is Distributed.ipynb
# 3. Lab 12 Finding Outliers.ipynb
# 4. Lab 13 Finding Correlation.ipynb
```

### Option 2: Quick Verification
All notebooks are complete and ready to run. Just open them and execute all cells!

## 📈 Expected Results

### Exploratory Data Analysis Lab
- Missing values identified and handled
- Job satisfaction visualized with multiple charts
- Programming language trends analyzed
- Remote work patterns explored
- Cross-tabulation completed
- Dataset exported

### Data Distribution Lab
- Data structure examined
- Correlations calculated
- Distributions visualized
- Programming languages compared
- Remote work trends by region
- Cross-tabulation (Employment vs EdLevel)

### Finding Outliers Lab
- Industry distribution plotted
- High compensation outliers identified
- IQR method applied
- Outliers removed (~15-20% of data)
- Correlation matrix created
- Cleaner dataset generated

### Correlation Lab
- Compensation distribution visualized
- Median full-time salary: $65,000
- Compensation by country analyzed
- Outliers removed using IQR
- Correlation heatmap created
- Scatter plots generated

## 📚 Key Concepts

### Statistical Measures
- **Mean**: Average value
- **Median**: Middle value (robust to outliers)
- **Mode**: Most frequent value
- **Standard Deviation**: Measure of spread
- **IQR**: Interquartile Range (Q3 - Q1)
- **Percentiles**: 25th, 50th, 75th

### Correlation
- **Pearson**: Linear correlation (-1 to 1)
- **Spearman**: Rank correlation (for non-linear)
- **Interpretation**:
  - |r| < 0.3: Weak
  - 0.3 ≤ |r| < 0.7: Moderate
  - |r| ≥ 0.7: Strong

### Outlier Detection
- **IQR Method**: Most common, robust
  - Lower: Q1 - 1.5 * IQR
  - Upper: Q3 + 1.5 * IQR
- **Z-score Method**: For normal distributions
  - Outliers: |z| > 3
- **Box Plot**: Visual identification

## 💡 EDA Best Practices

### 1. Data Understanding
- Always start with `df.info()` and `df.describe()`
- Check for missing values: `df.isnull().sum()`
- Examine data types and ranges
- Identify categorical vs numerical columns

### 2. Missing Value Strategy
- Calculate percentage missing
- Decide: drop, impute, or flag
- For categorical: use mode
- For numerical: use median (skewed) or mean (normal)

### 3. Outlier Handling
- Identify using IQR or z-score
- Visualize with box plots
- Decide: keep, remove, or cap
- Document reasoning

### 4. Visualization
- Use appropriate chart types
- Label axes clearly
- Add titles and legends
- Choose color schemes wisely
- Multiple views for complex data

### 5. Correlation Analysis
- Check for multicollinearity
- Use heatmaps for overview
- Verify with scatter plots
- Consider non-linear relationships

## 🔍 Functions Reference

### Pandas Functions
```python
# Data exploration
df.head()                 # First 5 rows
df.info()                 # Column info
df.describe()             # Statistics
df.shape                  # Dimensions
df.isnull().sum()         # Missing values

# Statistical analysis
df['col'].mean()          # Mean
df['col'].median()        # Median
df['col'].mode()[0]       # Mode
df['col'].std()           # Standard deviation
df['col'].quantile(0.25)  # 25th percentile
df['col'].skew()          # Skewness
df.corr()                 # Correlation matrix

# Data manipulation
pd.crosstab()             # Cross-tabulation
df.value_counts()         # Frequency counts
df.groupby()              # Grouping
df.fillna()               # Fill missing values
```

### Visualization Functions
```python
# Matplotlib
plt.hist()                # Histogram
plt.boxplot()             # Box plot
plt.scatter()             # Scatter plot
plt.bar()                 # Bar chart
plt.pie()                 # Pie chart

# Seaborn
sns.countplot()           # Count plot
sns.boxplot()             # Box plot
sns.heatmap()             # Heatmap
sns.scatterplot()         # Scatter plot
```

## 🐛 Troubleshooting

### Issue: "FileNotFoundError"
**Solution**: Ensure internet connection for loading data from URL.

### Issue: Visualizations not showing
**Solution**: Add `%matplotlib inline` at the top of notebook.

### Issue: Import errors
**Solution**: Install required libraries:
```powershell
pip install pandas matplotlib seaborn
```

### Issue: "SettingWithCopyWarning"
**Solution**: Use `.copy()` when creating filtered DataFrames:
```python
df_filtered = df[df['col'] > value].copy()
```

## 📊 Checklist Summary

**Total Checklist Items**: 39

### Exploratory Data Analysis (11 items) ✅
### Analyzing Data Distribution (7 items) ✅
### Handling Outliers (7 items) ✅
### Correlation Analysis (6 items) ✅
### Advanced Analysis (8 items) ✅

**All Complete!** ✅

## 🎓 Quiz Topics

1. Missing value identification
2. Categorical visualization
3. Cross-tabulation
4. Median compensation
5. IQR method for outliers
6. Skewness calculation
7. Outlier handling best practices
8. Filtering and aggregation
9. Correlation interpretation
10. Purpose of outlier removal

**Quiz Score**: 10/10 ✅

## ✨ Key Insights from Analysis

### Compensation
- Median full-time salary: $65,000
- Significant variation by country
- Right-skewed distribution (log-normal)
- Outliers represent top earners

### Job Satisfaction
- Diverse distribution across levels
- Weak correlation with experience
- Varies by employment type

### Programming Languages
- JavaScript, Python, SQL most popular
- Regional variations exist
- Differences between "have worked" and "want to work"

### Remote Work
- Increasing trend
- Varies by country and employment type
- Full-time employees show diverse preferences

## 🎉 Module 03 Complete!

All notebooks filled, all analyses performed, ready for submission!

**Next Module**: Module 04 - Data Visualization

---

**Last Updated**: October 19, 2025  
**Status**: Complete ✅  
**Notebooks**: 4/4
