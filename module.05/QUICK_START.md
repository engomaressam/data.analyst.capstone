# Module 05 - Quick Start Guide

## 🚀 Get Started in 5 Minutes!

---

## Prerequisites

Make sure you have Python installed and the required packages:

```bash
pip install plotly pandas matplotlib wordcloud pillow reportlab kaleido
```

---

## Option 1: Run Everything at Once (Recommended)

```bash
cd module.05
python run_all.py
```

This will generate all dashboards, PDFs, and HTML files automatically!

---

## Option 2: Step-by-Step

### Step 1: Create Interactive Dashboards

```bash
cd module.05
python dashboard_builder.py
```

**Output:**
- `outputs/dashboard_1_current_tech.html` ✅
- `outputs/dashboard_1_current_tech.png` ✅
- `outputs/dashboard_2_future_tech.html` ✅
- `outputs/dashboard_2_future_tech.png` ✅
- `outputs/dashboard_3_demographics.html` ✅
- `outputs/dashboard_3_demographics.png` ✅

### Step 2: Generate PDF Presentation

```bash
python pdf_generator.py
```

**Output:**
- `outputs/Dashboard_Presentation.pdf` ✅

### Step 3: Create Combined Web Dashboard

```bash
python create_html_dashboard.py
```

**Output:**
- `outputs/Interactive_Dashboard.html` ✅

---

## View Your Dashboards

### Interactive HTML Dashboard
```bash
# Windows
start outputs/Interactive_Dashboard.html

# Mac/Linux
open outputs/Interactive_Dashboard.html
```

### PDF Presentation
```bash
# Windows
start outputs/Dashboard_Presentation.pdf

# Mac/Linux
open outputs/Dashboard_Presentation.pdf
```

---

## Troubleshooting

### Issue: Module not found

```bash
# Install missing packages
pip install plotly pandas matplotlib wordcloud pillow reportlab kaleido
```

### Issue: Data file not found

Make sure `../data/survey_results_updated.csv` exists.

### Issue: Kaleido not working

```bash
# Try reinstalling
pip uninstall kaleido
pip install kaleido --upgrade
```

---

## What You'll Get

✅ **3 Interactive HTML Dashboards**
- Hover for details
- Zoom and pan
- Professional styling

✅ **3 High-Resolution Images**
- 1600×900 pixels
- Perfect for presentations
- Print-quality

✅ **1 Professional PDF**
- Complete presentation
- Cover page
- All dashboards included

✅ **1 Combined Web Dashboard**
- Single-page application
- Tabbed navigation
- Portfolio-ready

---

## Next Steps

1. **View your dashboards** in a browser
2. **Share the PDF** with employers
3. **Add to your portfolio** website
4. **Push to GitHub** for showcase

---

## Need Help?

Check the full documentation:
- `README.md` - Complete guide
- `QUIZ_ANSWERS_MODULE05.md` - Quiz solutions
- `MODULE_05_COMPLETE.md` - Completion summary

---

**Ready to impress employers with Python dashboards!** 🚀
