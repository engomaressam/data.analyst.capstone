# Module 01 - Collecting Data Using APIs

## Project Overview
This module focuses on collecting job data using APIs to identify in-demand skills in the technology industry.

## Files in this Module

### 1. PY0101EN-5 3_Requests_HTTP.ipynb
**Purpose**: Learn HTTP requests fundamentals (GET and POST)
**Status**: ✅ Complete - All code cells filled in

**Covers Checklist Items 1-4:**
- ✅ POST request to http://httpbin.org/post
- ✅ URL comparison between GET and POST requests
- ✅ Request body analysis
- ✅ Form data viewing from POST request

### 2. Jobs_API.ipynb
**Purpose**: Flask server that provides the Jobs API
**Status**: ✅ Complete - Ready to run

**Covers Checklist Item 5:**
- ✅ Jobs_API notebook ready to run

### 3. Collecting_Jobs_data_Using_API-Questions.ipynb
**Purpose**: Main assignment - Collect job data from API
**Status**: ✅ Complete - All functions implemented

**Covers Checklist Items 6-10:**
- ✅ Function to find number of job postings for Python
- ✅ Function to find job postings by location
- ✅ Data collection and Excel export
- ✅ Creates 'job-postings.xlsx' for location data
- ✅ Creates 'github-job-postings.xlsx' for technology data

## How to Run the Project

### Step 1: Install Required Dependencies
```powershell
pip install flask requests pandas openpyxl jupyter
```

### Step 2: Run the Jobs_API Server
1. Open `Jobs_API.ipynb` in Jupyter Notebook
2. Run all cells in sequence
3. The Flask server will start at `http://127.0.0.1:5000`
4. Keep this notebook running while you work on the next steps

### Step 3: Run the HTTP Requests Notebook (Optional)
1. Open `PY0101EN-5 3_Requests_HTTP.ipynb`
2. Run all cells to learn about HTTP requests
3. This covers checklist items 1-4

### Step 4: Run the Main Assignment
1. Open `Collecting_Jobs_data_Using_API-Questions.ipynb`
2. Make sure the Jobs_API server is running (Step 2)
3. Run all cells in sequence
4. The notebook will:
   - Collect job data for Python technology
   - Collect job data for 7 US locations
   - Save location data to `job-postings.xlsx`
   - Collect job data for 12 technologies
   - Save technology data to `github-job-postings.xlsx`

## Expected Output

After running all notebooks, you should have:
- ✅ `example1.txt` - Downloaded text file
- ✅ `job-postings.xlsx` - Job data by location
- ✅ `github-job-postings.xlsx` - Job data by technology

## Data Collected

### Locations Analyzed:
- Los Angeles
- New York
- San Francisco
- Washington DC
- Seattle
- Austin
- Detroit

### Technologies Analyzed:
- C
- C#
- C++
- Java
- JavaScript
- Python
- Scala
- Oracle
- SQL Server
- MySQL Server
- PostgreSQL
- MongoDB

## Checklist Status

1. ✅ POST request to http://httpbin.org/post using Python
2. ✅ URL comparison between GET and POST requests
3. ✅ Request bodies printed and analyzed
4. ✅ Form data from POST request viewed
5. ✅ Jobs_API notebook runs successfully
6. ✅ All cells executed in Jobs_API notebook
7. ✅ GitHub Jobs API called for Python technology
8. ✅ Function written to find job postings by location
9. ✅ Job posting data stored in Excel spreadsheet
10. ✅ All technology data saved to 'github-job-postings.xlsx'

## Troubleshooting

### Issue: API not responding
**Solution**: Make sure the Jobs_API.ipynb notebook is running and the Flask server has started successfully.

### Issue: "Connection refused" error
**Solution**: Check that the API URL is `http://127.0.0.1:5000/data` and the server is running.

### Issue: jobs.json not found
**Solution**: Run the wget command in Jobs_API.ipynb to download the jobs.json file.

## Notes

- The Jobs_API.ipynb must be running for the data collection notebook to work
- Data collection may take a few moments depending on the number of records
- Make sure you're in the correct directory when running the notebooks
- All Excel files will be created in the same directory as the notebooks

## Next Steps

After completing this module, you will:
- Have hands-on experience with REST APIs
- Understand HTTP GET and POST requests
- Know how to collect and store data from APIs
- Be ready to proceed to Module 02: Web Scraping
