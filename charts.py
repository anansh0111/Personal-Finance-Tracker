import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

def show_charts(df):
    st.subheader("📊 Spending Overview")

    df['Date'] = pd.to_datetime(df['Date'])
    monthly = df.groupby(df['Date'].dt.month)['Amount'].sum()
    categories = df.groupby('Category')['Amount'].sum()

    fig1, ax1 = plt.subplots()
    ax1.pie(categories, labels=categories.index, autopct='%1.1f%%')
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    monthly.plot(kind='bar', ax=ax2)
    ax2.set_title("Monthly Expenses")
    st.pyplot(fig2)
