from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle

def generate_report():
    doc=SimpleDocTemplate(
        "output/World_bank_Analysis_Report.pdf", 
        pagesize=letter
    )
    story=[]
    styles=getSampleStyleSheet()

    # Cover Page
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("Global Economic Health Analyzer", styles['Title']))
    story.append(Spacer(1, 12))
    story.append(Paragraph("A Data Analysis of World Bank GDP Growth Data", styles['Heading2']))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Period: 1990 – 2023 | 266 Countries", styles['Normal']))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Data Source: World Bank Open Data", styles['Normal']))
    story.append(PageBreak())
    # Section 1: Project Overview
    story.append(Paragraph("1. Project Overview", styles['Heading1']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "This project analyzes GDP growth data for 266 countries from 1990 to 2023 "
        "using World Bank Open Data. The goal is to identify economic trends, compare "
        "regional performance, and examine the impact of major global events such as "
        "the 2008 Financial Crisis and the COVID-19 pandemic.",
        styles['Normal']
    ))
    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "The analysis covers five key questions: regional GDP performance, crisis impact, "
        "income group comparison, country volatility, and COVID-19 economic impact.",
        styles['Normal']
    ))
    #story.append(PageBreak())
    # Section 2: Data Pipeline
    story.append(Paragraph("2. Data Pipeline", styles['Heading1']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "Before any analysis could begin, the raw World Bank CSV required significant "
        "wrangling. The data arrived in a wide format with years as columns, metadata "
        "rows at the top, and multiple files that needed to be joined together.",
        styles['Normal']
    ))
    story.append(Spacer(1, 12))

    pipeline_steps = [
        ["Step", "Operation", "Description"],
        ["1", "Loading", "Used skiprows=4 to skip World Bank metadata rows before the real header"],
        ["2", "Cleaning", "Dropped unnamed ghost column, filtered years to 1990-2023"],
        ["3", "Merging", "Joined GDP data with Metadata_Country on Country Code (left join)"],
        ["4", "Reshaping", "Used melt() to transform wide format into tidy format"],
        ["5", "Type fixing", "Converted Year column from string to integer"],
    ]
    table = Table(pipeline_steps, colWidths=[0.5*inch, 1.2*inch, 4.5*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
        ('FONTSIZE', (0,0), (-1,-1), 9),
    ]))
    story.append(table)
    #story.append(PageBreak())
    # Section 3: Key Findings
    story.append(Paragraph("3. Key Findings", styles['Heading1']))
    story.append(Spacer(1, 12))

    findings = [
        ("Regional GDP Growth (1990–2023)",
        "South Asia leads with 5.41% average growth. North America trails at 1.95%. "
        "The Catch-up Effect explains this — poorer regions grow faster by adopting "
        "existing technology rather than inventing new ones."),

        ("2008 Financial Crisis Impact",
        "Europe & Central Asia was hit hardest (-4.67%), worse than North America (-4.11%), "
        "due to the double blow of the 2008 crash and the Eurozone sovereign debt crisis "
        "(2010-2012). South Asia was most resilient with only a -0.16% difference, "
        "protected by domestic demand and limited exposure to Western financial markets."),

        ("Income Group Analysis",
        "High-income countries grow slowest at 2.55%. Lower-middle income countries "
        "grow fastest at 4.00%. This confirms the Catch-up Effect theory."),

        ("Most Volatile Economies",
        "Equatorial Guinea tops both highest average growth AND highest volatility — "
        "classic oil-dependent boom/bust cycle. Conflict nations (Iraq, Libya, South Sudan) "
        "show extreme volatility due to war destroying infrastructure and investment."),

        ("COVID-19 Impact (2020)",
        "Macao SAR, China collapsed -54% as casino tourism dropped 99.7%. "
        "Guyana grew +43% by beginning commercial oil extraction for the first time — "
        "completely unrelated to COVID, a reminder that context always matters in analysis."),
    ]

    for title, content in findings:
        story.append(Paragraph(title, styles['Heading2']))
        story.append(Spacer(1, 6))
        story.append(Paragraph(content, styles['Normal']))
        story.append(Spacer(1, 12))

    #story.append(PageBreak())
    # Section 4: Visualizations
    story.append(Paragraph("4. Visualizations", styles['Heading1']))
    story.append(Spacer(1, 12))

    charts = [
        ("output/Regional_AVG_GDP_growth.png", 
        "Chart 1: Regional Average GDP Growth Rate (1990-2023)"),
        ("output/GDP_Growth_Rate_Before_After_Crisis.png", 
        "Chart 2: GDP Growth Rate Before and After 2008 Crisis"),
        ("output/Covid19_Impact_GDP_Growth_2020.png", 
        "Chart 3: COVID-19 Impact — Top 10 Worst Affected Countries (2020)"),
        ("output/GDP_Growth_Rate_Trends_Selected_Countries.png", 
        "Chart 4: GDP Growth Trends — Guyana vs Macao vs Germany"),
    ]

    for image_path, caption in charts:
        story.append(Paragraph(caption, styles['Heading2']))
        story.append(Spacer(1, 6))
        story.append(Image(image_path, width=6*inch, height=3*inch))
        story.append(Spacer(1, 20))
    # Section 5: Conclusions
    #story.append(PageBreak())
    story.append(Paragraph("5. Conclusions", styles['Heading1']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "This analysis of World Bank GDP growth data across 266 countries from 1990 to 2023 "
        "reveals several important economic patterns:",
        styles['Normal']
    ))
    story.append(Spacer(1, 12))

    conclusions = [
        "Regional inequality persists — South Asia consistently outperforms Western economies due to the Catch-up Effect.",
        "Financial crises hit integrated economies hardest — Europe suffered more than emerging markets in 2008 due to deeper exposure to Western financial systems.",
        "Economic structure determines resilience — tourism-dependent and oil-dependent economies are highly vulnerable to external shocks.",
        "Context is everything — Guyana's +43% in 2020 had nothing to do with COVID resilience. Always investigate anomalies before drawing conclusions.",
        "Volatility and growth are not the same thing — a high average GDP growth rate means nothing without examining the standard deviation behind it.",
    ]

    for point in conclusions:
        story.append(Paragraph(f"• {point}", styles['Normal']))
        story.append(Spacer(1, 8))
    doc.build(story)
    print("Report generated successfully!")

if __name__ == "__main__":
        generate_report()
