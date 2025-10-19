# Quick Start Guide - Module 01 API Data Collection

## ✅ All Checklist Items COMPLETED!

All 10 checklist items for "Collecting Data Using APIs" are now complete.

## 🚀 Quick Start Instructions

### Step 1: Install Dependencies (Run Once)
Open PowerShell and run:
```powershell
pip install flask requests pandas openpyxl jupyter notebook
```

### Step 2: Start the API Server
1. Open Jupyter Notebook:
   ```powershell
   cd "c:\Users\Diaa\data.analyst.capstone\module.01"
   jupyter notebook
   ```
2. Open `Jobs_API.ipynb`
3. Run ALL cells (Cell → Run All)
4. Wait for Flask server to start
5. **KEEP THIS NOTEBOOK RUNNING**

### Step 3: Run the Main Assignment
1. In Jupyter, open `Collecting_Jobs_data_Using_API-Questions.ipynb`
2. Run ALL cells (Cell → Run All)
3. Watch as it collects job data

### Step 4: Check Your Results
Two Excel files will be created:
- ✅ `job-postings.xlsx` - Job counts by location
- ✅ `github-job-postings.xlsx` - Job counts by technology

## 📊 What Gets Analyzed

### 7 Locations:
Los Angeles, New York, San Francisco, Washington DC, Seattle, Austin, Detroit

### 12 Technologies:
C, C#, C++, Java, JavaScript, Python, Scala, Oracle, SQL Server, MySQL Server, PostgreSQL, MongoDB

## ⚠️ Important Notes

1. **Jobs_API.ipynb MUST be running** before you run the main assignment
2. If you see connection errors, restart Jobs_API.ipynb
3. The API runs on `http://127.0.0.1:5000`
4. Data collection takes 1-2 minutes to complete

## 🎯 Checklist Verification

Run these commands to verify completion:

**Check if notebooks exist:**
```powershell
ls *.ipynb
```

**Expected files:**
- ✅ Jobs_API.ipynb
- ✅ Collecting_Jobs_data_Using_API-Questions.ipynb
- ✅ PY0101EN-5 3_Requests_HTTP.ipynb

**After running, check output files:**
```powershell
ls *.xlsx
```

**Expected output:**
- ✅ job-postings.xlsx
- ✅ github-job-postings.xlsx

## 🐛 Common Issues

**Problem**: "Connection refused" error
**Solution**: Make sure Jobs_API.ipynb is running

**Problem**: "jobs.json not found"
**Solution**: Run the wget cell in Jobs_API.ipynb to download it

**Problem**: "ModuleNotFoundError: No module named 'flask'"
**Solution**: Run `pip install flask`

## ✨ You're Ready!

All code is complete and ready to run. Just follow Steps 1-3 above and you're done!

---
**Full documentation available in README.md**
