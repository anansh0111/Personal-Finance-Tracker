from fpdf import FPDF
import pandas as pd

def generate_pdf(df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Monthly Finance Report", ln=True, align="C")
    
    total_spent = df["Amount"].sum()
    pdf.ln(10)
    pdf.cell(200, 10, f"Total Spent: ₹{total_spent}", ln=True)

    by_category = df.groupby("Category")["Amount"].sum()
    for cat, amt in by_category.items():
        pdf.cell(200, 10, f"{cat}: ₹{amt}", ln=True)

    pdf.output("monthly_report.pdf")
