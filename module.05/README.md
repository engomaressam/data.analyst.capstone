# Module 05: Dashboard Creation

## 📊 Creating Professional Dashboards with Python

This module demonstrates advanced dashboard creation using Python instead of traditional BI tools (Cognos/Looker). This approach showcases stronger programming skills and creates portfolio-ready deliverables.

---

## 🎯 Learning Objectives

- Create professional interactive dashboards using Plotly
- Generate PDF presentations with ReportLab
- Build responsive HTML dashboards
- Apply data visualization best practices
- Demonstrate end-to-end dashboard development

---

## 📁 Project Structure

```
module.05/
├── dashboard_builder.py          # Main dashboard creation script
├── pdf_generator.py              # PDF presentation generator
├── create_html_dashboard.py      # HTML dashboard combiner
├── README.md                     # This file
├── QUIZ_ANSWERS_MODULE05.md      # Quiz answers and explanations
├── MODULE_05_COMPLETE.md         # Completion summary
└── outputs/                      # Generated dashboards
    ├── dashboard_1_current_tech.html
    ├── dashboard_1_current_tech.png
    ├── dashboard_2_future_tech.html
    ├── dashboard_2_future_tech.png
    ├── dashboard_3_demographics.html
    ├── dashboard_3_demographics.png
    ├── Dashboard_Presentation.pdf
    └── Interactive_Dashboard.html
```

---

## 🚀 Quick Start

### Prerequisites

```bash
# Install required packages
pip install plotly pandas matplotlib wordcloud pillow reportlab kaleido
```

### Step 1: Prepare Data

Ensure you have the survey data file:
- File: `../data/survey_results_updated.csv`
- Download if needed from course materials

### Step 2: Create Dashboards

```bash
# Navigate to module 05
cd module.05

# Run dashboard builder
python dashboard_builder.py
```

This creates:
- 3 HTML interactive dashboards
- 3 PNG high-resolution images

### Step 3: Generate PDF Presentation

```bash
# Create professional PDF presentation
python pdf_generator.py
```

This creates:
- `Dashboard_Presentation.pdf` - Complete presentation with all dashboards

### Step 4: Create Combined HTML Dashboard

```bash
# Create single-page interactive dashboard
python create_html_dashboard.py
```

This creates:
- `Interactive_Dashboard.html` - Tabbed dashboard with all 3 sections

---

## 📊 Dashboard Specifications

### Dashboard 1: Current Technology Usage

**Layout:** 2×2 grid

| Panel | Visualization | Chart Type |
|-------|---------------|------------|
| 1 | Top 10 Languages Have Worked With | Horizontal Bar Chart |
| 2 | Top 10 Databases Have Worked With | Column Chart |
| 3 | Platforms Have Worked With | Bubble Chart (Word Cloud alternative) |
| 4 | Top 10 Web Frameworks Have Worked With | Hierarchy Bubble Chart |

**Columns Used:**
- `LanguageHaveWorkedWith`
- `DatabaseHaveWorkedWith`
- `PlatformHaveWorkedWith`
- `WebframeHaveWorkedWith`

---

### Dashboard 2: Future Technology Trends

**Layout:** 2×2 grid

| Panel | Visualization | Chart Type |
|-------|---------------|------------|
| 1 | Top 10 Languages Want to Work With | Horizontal Bar Chart |
| 2 | Top 10 Databases Want to Work With | Column Chart |
| 3 | Platforms Want to Work With | Tree Map style (Bubble implementation) |
| 4 | Top 10 Web Frameworks Want to Work With | Hierarchy Bubble Chart |

**Columns Used:**
- `LanguageWantToWorkWith`
- `DatabaseWantToWorkWith`
- `PlatformWantToWorkWith`
- `WebframeWantToWorkWith`

---

### Dashboard 3: Demographics

**Layout:** 2×2 grid

| Panel | Visualization | Chart Type |
|-------|---------------|------------|
| 1 | Respondents by Age Group | Pie Chart |
| 2 | Respondent Count by Country | Horizontal Bar Chart (Top 10) |
| 3 | Respondents by Education Level | Bar Chart with values |
| 4 | Age × Education Level | Stacked Bar Chart |

**Columns Used:**
- `Age`
- `Country`
- `EdLevel`

---

## 💻 Code Highlights

### Creating Interactive Charts

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create 2x2 subplot layout
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Chart 1', 'Chart 2', 'Chart 3', 'Chart 4')
)

# Add horizontal bar chart
fig.add_trace(
    go.Bar(
        y=data['Item'],
        x=data['Count'],
        orientation='h',
        text=data['Count'],
        textposition='outside'
    ),
    row=1, col=1
)

# Save as HTML and PNG
fig.write_html('dashboard.html')
fig.write_image('dashboard.png', width=1600, height=900)
```

### Data Processing

```python
def get_top_n(series, n=10, split_char=';'):
    """Extract top N items from multi-value columns."""
    all_items = []
    for item in series.dropna():
        if split_char in str(item):
            all_items.extend([x.strip() for x in str(item).split(split_char)])
        else:
            all_items.append(str(item).strip())
    
    counter = Counter(all_items)
    return pd.DataFrame(counter.most_common(n), columns=['Item', 'Count'])
```

---

## 🎨 Design Principles

### Visual Design
- **Color Schemes**: Professional, contrasting colors
- **Typography**: Clear, readable fonts
- **Spacing**: Proper margins and padding
- **Consistency**: Uniform styling across all dashboards

### Data Visualization Best Practices
- ✅ Clear chart titles
- ✅ Value labels for precision
- ✅ Appropriate chart types for data
- ✅ Consistent color coding
- ✅ Interactive features (hover, zoom)

### User Experience
- **Responsive**: Works on different screen sizes
- **Interactive**: Hover for details, zoom capabilities
- **Navigation**: Easy tab switching in HTML version
- **Accessibility**: High contrast, readable text

---

## 📈 Output Formats

### 1. Interactive HTML Dashboards
- **Format**: Individual HTML files per dashboard
- **Features**: 
  - Hover tooltips
  - Zoom and pan
  - Dynamic resizing
- **Use Case**: Interactive exploration, web hosting

### 2. High-Resolution PNG Images
- **Format**: PNG (1600×900 pixels)
- **Features**:
  - Publication-quality
  - Suitable for presentations
  - Easy to share
- **Use Case**: Reports, slides, portfolios

### 3. PDF Presentation
- **Format**: Professional PDF document
- **Features**:
  - Cover page
  - Section dividers
  - All dashboards included
  - Summary page
- **Use Case**: Formal presentations, submissions

### 4. Combined Web Dashboard
- **Format**: Single-page HTML with tabs
- **Features**:
  - Three tabbed sections
  - Professional header/footer
  - Statistics overview
  - Responsive design
- **Use Case**: Portfolio showcase, live demo

---

## 🎓 Skills Demonstrated

### Technical Skills
- Python programming (Plotly, Pandas)
- Interactive visualization creation
- PDF generation (ReportLab)
- HTML/CSS web design
- Data transformation and aggregation
- Multi-format output generation

### Analytical Skills
- Selecting appropriate chart types
- Identifying key metrics to visualize
- Creating meaningful comparisons
- Data storytelling

### Professional Skills
- Following specifications precisely
- Creating portfolio-ready deliverables
- Documentation and code organization
- Multiple output formats for different audiences

---

## 🔍 Comparison: Python vs. Traditional BI Tools

| Feature | Our Python Approach | Cognos/Looker |
|---------|---------------------|---------------|
| **Customization** | ✅ Full control | ❌ Limited |
| **Reproducibility** | ✅ Code-based | ❌ GUI-based |
| **Portability** | ✅ Runs anywhere | ❌ Cloud/license needed |
| **Version Control** | ✅ Git-friendly | ❌ Difficult |
| **Automation** | ✅ Easy to automate | ❌ Manual process |
| **Cost** | ✅ Free/open-source | ❌ Expensive licenses |
| **Learning Curve** | Medium | Easy |
| **Portfolio Value** | ✅ Shows coding skills | ⚠️ Shows tool proficiency |

---

## 🐛 Troubleshooting

### Issue: Kaleido not installing
```bash
# Try alternate installation
pip install kaleido --upgrade
# Or use conda
conda install -c conda-forge python-kaleido
```

### Issue: Images not generating
```bash
# Install system dependencies
# On Windows: Already included
# On Linux: sudo apt-get install xvfb
# On Mac: brew install --cask xquartz
```

### Issue: Data file not found
```bash
# Check file location
ls ../data/survey_results_updated.csv
# If missing, download from course materials
```

---

## 📚 Resources

### Plotly Documentation
- [Plotly Python](https://plotly.com/python/)
- [Subplots Guide](https://plotly.com/python/subplots/)
- [Export Static Images](https://plotly.com/python/static-image-export/)

### ReportLab Documentation
- [ReportLab User Guide](https://www.reportlab.com/docs/reportlab-userguide.pdf)
- [Platypus (PDF Layout)](https://www.reportlab.com/documentation/faq/platypus/)

### Data Visualization Best Practices
- [Storytelling with Data](https://www.storytellingwithdata.com/)
- [Data Visualization Catalogue](https://datavizcatalogue.com/)

---

## 🎯 Next Steps

### For Job Applications
1. Add generated dashboards to your portfolio website
2. Include PNG images in presentations
3. Share HTML dashboards via GitHub Pages
4. Mention in resume: "Created interactive dashboards with Python/Plotly"

### For Further Enhancement
- [ ] Add more interactive features (filters, date ranges)
- [ ] Create animated visualizations
- [ ] Implement real-time data updates
- [ ] Add statistical annotations
- [ ] Create mobile-optimized version
- [ ] Deploy to web hosting platform

---

## ✅ Checklist

**Setup:**
- [ ] Install required packages
- [ ] Download survey data
- [ ] Verify file locations

**Execution:**
- [ ] Run `dashboard_builder.py`
- [ ] Run `pdf_generator.py`
- [ ] Run `create_html_dashboard.py`
- [ ] Verify all outputs created

**Review:**
- [ ] Open HTML dashboards in browser
- [ ] Review PNG images
- [ ] Check PDF presentation
- [ ] Test combined HTML dashboard

**Submission:**
- [ ] Take screenshots of dashboards
- [ ] Create GitHub link to PDFs
- [ ] Answer quiz questions
- [ ] Complete module documentation

---

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review the code comments in each script
3. Verify all dependencies are installed
4. Check the quiz answers for guidance

---

<div align="center">

## 🎊 Ready to Impress Employers!

**Module 05 demonstrates advanced Python skills beyond traditional BI tools.**

Created with ❤️ using Python | October 2025

</div>
