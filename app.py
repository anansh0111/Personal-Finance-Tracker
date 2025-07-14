import streamlit as st
from utils.charts import show_charts
from utils.reports import generate_pdf
import pandas as pd

st.set_page_config(page_title="Personal Finance Tracker", layout="wide")

st.title("💰 Personal Finance Tracker")
menu = st.sidebar.selectbox("Menu", ["Add Transaction", "Dashboard", "Monthly Report"])

df = pd.read_csv("data/transactions.csv")

if menu == "Add Transaction":
    with st.form("entry_form"):
        date = st.date_input("Date")
        amount = st.number_input("Amount", min_value=0.0)
        category = st.selectbox("Category", ["Food", "Rent", "Travel", "Shopping", "Others"])
        note = st.text_input("Note")
        submit = st.form_submit_button("Add")
        if submit:
            df.loc[len(df)] = [str(date), amount, category, note]
            df.to_csv("data/transactions.csv", index=False)
            st.success("Transaction added!")

elif menu == "Dashboard":
    show_charts(df)

elif menu == "Monthly Report":
    if st.button("Generate PDF Report"):
        generate_pdf(df)
        st.success("PDF saved to 'monthly_report.pdf'")
