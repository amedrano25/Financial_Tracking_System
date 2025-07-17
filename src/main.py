from data_loader import load_data
from variance_checker import detect_variance
from report_generator import generate_report
import os

if __name__ == "__main__":
    payroll_path = os.path.join('data', 'payroll.csv')
    expenses_path = os.path.join('data', 'expenses.csv')
    output_path = os.path.join('reports', 'financial_summary_2025_07.xlsx')

    payroll_df, expenses_df = load_data(payroll_path, expenses_path)
    anomalies_df = detect_variance(expenses_df)
    generate_report(payroll_df, expenses_df, anomalies_df, output_path)

    print(f"Report generated successfully: {output_path}")
