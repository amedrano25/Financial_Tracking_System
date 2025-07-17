import streamlit as st
import pandas as pd
import os
from src.variance_checker import detect_variance
from src.report_generator import generate_report

st.set_page_config(page_title="Financial Tracking System", layout="wide")

st.title("📊 Financial Tracking System")
st.write("Upload your payroll and expense files to generate a financial report with variance analysis.")

# File uploaders
payroll_file = st.file_uploader("Upload Payroll CSV", type=["csv"])
expenses_file = st.file_uploader("Upload Expenses CSV", type=["csv"])

if st.button("Generate Report"):
    if payroll_file and expenses_file:
        payroll_df = pd.read_csv(payroll_file)
        expenses_df = pd.read_csv(expenses_file)
        anomalies_df = detect_variance(expenses_df)

        output_path = os.path.join("reports", "financial_summary_streamlit.xlsx")
        generate_report(payroll_df, expenses_df, anomalies_df, output_path)

        st.success("✅ Report generated successfully!")
        with open(output_path, "rb") as file:
            st.download_button(
                label="📥 Download Report",
                data=file,
                file_name="financial_summary.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.error("⚠️ Please upload both payroll and expense files.")
