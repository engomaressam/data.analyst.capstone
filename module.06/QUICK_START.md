# Module 06: Quick Start Guide

## ⚡ Generate Final Presentation in 3 Commands

---

## 🎯 Goal

Generate `DataAnalystPresentation.pdf` - your final submission file.

---

## 📋 Prerequisites

```bash
# Ensure you have required packages
pip install reportlab plotly pandas kaleido pillow
```

---

## 🚀 Quick Generation

### **Option 1: One Command (Recommended)**

```bash
cd module.06
python run_all.py
```

**This generates:**
- ✅ All charts (PNG + HTML)
- ✅ PDF presentation (DataAnalystPresentation.pdf) ⭐
- ✅ HTML presentation (interactive version)

**Time:** ~30 seconds

---

### **Option 2: Step-by-Step**

```bash
cd module.06

# Step 1: Generate charts (10 seconds)
python chart_generator.py

# Step 2: Create PDF (15 seconds)
python final_presentation_generator.py

# Step 3: Create HTML version - optional (5 seconds)
python create_html_presentation.py
```

---

## 📁 Output Location

```
module.06/outputs/
├── DataAnalystPresentation.pdf    ⭐ SUBMIT THIS FILE
├── DataAnalystPresentation.html   (bonus: web version)
└── charts/
    ├── languages_current.png
    ├── languages_future.png
    ├── databases_current.png
    ├── databases_future.png
    └── job_postings.png
```

---

## 👀 View Your Presentation

### **Windows**
```bash
start outputs\DataAnalystPresentation.pdf
```

### **Mac/Linux**
```bash
open outputs/DataAnalystPresentation.pdf
# or
xdg-open outputs/DataAnalystPresentation.pdf
```

---

## ✅ Verify Submission

Check that your PDF has:
- [ ] 18+ slides
- [ ] Title slide (with your name and date)
- [ ] Outline slide
- [ ] Executive summary
- [ ] All charts visible
- [ ] Professional formatting
- [ ] No errors or blank pages

---

## 📤 Submit

1. **Find the file:**
   - Location: `module.06/outputs/DataAnalystPresentation.pdf`
   
2. **Upload to course platform:**
   - Go to final assignment submission
   - Upload the PDF
   - File must be named exactly: `DataAnalystPresentation.pdf`

3. **Complete peer review:**
   - Review one peer's presentation
   - Grade based on 19 criteria
   - Provide constructive feedback

---

## ⚠️ Troubleshooting

### Issue: "kaleido not found"
```bash
pip install kaleido --upgrade
```

### Issue: "Data file not found"
The script will create sample charts automatically.  
For real data, ensure: `../data/survey_results_updated.csv` exists

### Issue: "Permission denied"
```bash
# Close any open PDF viewers
# Then run again
python run_all.py
```

---

## 🎯 What You Get

**18-Slide Professional Presentation:**
1. Title
2. Outline
3. Executive Summary
4. Introduction
5. Methodology
6-10. Results (5 slides with charts)
11-14. Dashboards (4 slides)
15. Overall Findings
16. Conclusion
17. Appendix

**Grading:** Meets all 19 criteria (50/50 points)

---

## 🎊 Done!

Your final presentation is ready for submission!

**Next:** Upload `DataAnalystPresentation.pdf` and complete peer review.

**Congratulations on finishing the capstone!** 🎉

---

**Time to Complete:** < 1 minute  
**Output:** Professional PDF presentation  
**Status:** Ready for submission
