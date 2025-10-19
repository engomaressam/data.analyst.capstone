"""
Module 05: PDF Presentation Generator
======================================

Creates a professional PDF presentation from the dashboard images.
Uses ReportLab to create a polished PDF document.

Author: Diaa
Date: October 2025
"""

from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors
from datetime import datetime
import os

# Configuration
OUTPUT_DIR = './outputs/'
PDF_OUTPUT = f'{OUTPUT_DIR}Dashboard_Presentation.pdf'

def create_cover_page(elements, styles):
    """Create the cover page for the presentation."""
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=32,
        textColor=colors.HexColor('#1a76ff'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    elements.append(Spacer(1, 2*inch))
    elements.append(Paragraph("Data Analyst Capstone Project", title_style))
    
    # Subtitle
    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Heading2'],
        fontSize=24,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=20,
        alignment=TA_CENTER
    )
    elements.append(Paragraph("Module 05: Dashboard Visualizations", subtitle_style))
    
    # Description
    desc_style = ParagraphStyle(
        'Description',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#34495e'),
        spaceAfter=30,
        alignment=TA_CENTER
    )
    elements.append(Paragraph("Stack Overflow Developer Survey Analysis", desc_style))
    
    # Author and date
    info_style = ParagraphStyle(
        'Info',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.grey,
        alignment=TA_CENTER
    )
    elements.append(Spacer(1, 1.5*inch))
    elements.append(Paragraph(f"Author: Diaa", info_style))
    elements.append(Paragraph(f"Date: {datetime.now().strftime('%B %Y')}", info_style))
    
    # Technology stack
    elements.append(Spacer(1, 0.5*inch))
    tech_text = "Built with Python • Plotly • Pandas • ReportLab"
    elements.append(Paragraph(tech_text, info_style))
    
    elements.append(PageBreak())

def create_section_page(elements, styles, title, description):
    """Create a section divider page."""
    section_style = ParagraphStyle(
        'Section',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=colors.HexColor('#e74c3c'),
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    desc_style = ParagraphStyle(
        'SectionDesc',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#7f8c8d'),
        alignment=TA_CENTER
    )
    
    elements.append(Spacer(1, 2.5*inch))
    elements.append(Paragraph(title, section_style))
    elements.append(Spacer(1, 0.3*inch))
    elements.append(Paragraph(description, desc_style))
    elements.append(PageBreak())

def add_dashboard_image(elements, styles, image_path, title, description):
    """Add a dashboard image to the PDF with title and description."""
    # Title
    img_title_style = ParagraphStyle(
        'ImageTitle',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=10,
        alignment=TA_CENTER
    )
    elements.append(Paragraph(title, img_title_style))
    
    # Description
    if description:
        desc_style = ParagraphStyle(
            'ImageDesc',
            parent=styles['Normal'],
            fontSize=11,
            textColor=colors.HexColor('#7f8c8d'),
            spaceAfter=15,
            alignment=TA_CENTER
        )
        elements.append(Paragraph(description, desc_style))
    
    # Image
    if os.path.exists(image_path):
        img = Image(image_path, width=10*inch, height=5.625*inch)
        elements.append(img)
    else:
        elements.append(Paragraph(f"<i>Image not found: {image_path}</i>", styles['Normal']))
    
    elements.append(PageBreak())

def create_summary_page(elements, styles):
    """Create a summary page with key insights."""
    summary_style = ParagraphStyle(
        'SummaryTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#27ae60'),
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    elements.append(Paragraph("Dashboard Summary", summary_style))
    elements.append(Spacer(1, 0.3*inch))
    
    # Key findings
    findings = [
        ["Dashboard", "Key Visualizations"],
        ["Current Technology Usage", "Top 10 Languages, Databases, Platforms, Web Frameworks"],
        ["Future Technology Trends", "Desired Languages, Databases, Platforms, Web Frameworks"],
        ["Demographics", "Age Distribution, Country, Education Level, Age×Education"]
    ]
    
    table = Table(findings, colWidths=[3*inch, 5*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(table)
    elements.append(Spacer(1, 0.5*inch))
    
    # Skills demonstrated
    skills_style = ParagraphStyle(
        'Skills',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#e74c3c'),
        spaceAfter=15
    )
    elements.append(Paragraph("Skills Demonstrated", skills_style))
    
    skills = [
        "• Python dashboard creation with Plotly",
        "• Data visualization best practices",
        "• PDF generation with ReportLab",
        "• HTML interactive dashboards",
        "• Professional presentation design",
        "• Data analysis and interpretation"
    ]
    
    for skill in skills:
        elements.append(Paragraph(skill, styles['Normal']))
    
    elements.append(PageBreak())

def generate_pdf_presentation():
    """Generate the complete PDF presentation."""
    print("\n" + "="*60)
    print("GENERATING PDF PRESENTATION")
    print("="*60)
    
    # Create PDF document
    doc = SimpleDocTemplate(
        PDF_OUTPUT,
        pagesize=landscape(A4),
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )
    
    elements = []
    styles = getSampleStyleSheet()
    
    # Cover page
    print("Creating cover page...")
    create_cover_page(elements, styles)
    
    # Dashboard 1: Current Technology Usage
    print("Adding Current Technology Usage dashboard...")
    create_section_page(
        elements, styles,
        "Dashboard 1: Current Technology Usage",
        "Analyzing current technology adoption among developers"
    )
    add_dashboard_image(
        elements, styles,
        f"{OUTPUT_DIR}dashboard_1_current_tech.png",
        "Current Technology Usage",
        "Top programming languages, databases, platforms, and web frameworks currently in use"
    )
    
    # Dashboard 2: Future Technology Trends
    print("Adding Future Technology Trends dashboard...")
    create_section_page(
        elements, styles,
        "Dashboard 2: Future Technology Trends",
        "Exploring technologies developers want to learn"
    )
    add_dashboard_image(
        elements, styles,
        f"{OUTPUT_DIR}dashboard_2_future_tech.png",
        "Future Technology Trends",
        "Technologies developers want to work with in the coming year"
    )
    
    # Dashboard 3: Demographics
    print("Adding Demographics dashboard...")
    create_section_page(
        elements, styles,
        "Dashboard 3: Demographics",
        "Understanding the developer community demographics"
    )
    add_dashboard_image(
        elements, styles,
        f"{OUTPUT_DIR}dashboard_3_demographics.png",
        "Demographics Analysis",
        "Age distribution, geographic spread, and education levels of respondents"
    )
    
    # Summary page
    print("Creating summary page...")
    create_summary_page(elements, styles)
    
    # Build PDF
    print("Building PDF document...")
    doc.build(elements)
    
    print("="*60)
    print(f"✅ PDF PRESENTATION CREATED: {PDF_OUTPUT}")
    print("="*60)

if __name__ == "__main__":
    generate_pdf_presentation()
    print("\nPDF generation complete!")
    print(f"Output: {os.path.abspath(PDF_OUTPUT)}")
