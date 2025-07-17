# financial-tracking-system/README.md

# Financial Tracking System

A Python-based system that automates payroll and expense tracking, detects anomalies in financial data, and generates a styled Excel report with charts.

## 📦 Features
- Reads payroll and expense data from CSV files
- Detects variances/anomalies in expenses
- Outputs an Excel report with charts (generated using xlsxwriter)
- Modular codebase for easy customization

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the project
```bash
python src/main.py
```

## 📂 Project Structure
```
financial-tracking-system/
│
├── data/
│   ├── payroll.csv
│   ├── expenses.csv
│
├── reports/
│   ├── financial_summary_<DATE>.xlsx
│
├── src/
│   ├── main.py
│   ├── data_loader.py
│   ├── variance_checker.py
│   ├── report_generator.py
│
├── requirements.txt
└── README.md
```

## 📊 Example Output
The Excel report includes:
- Payroll table
- Expense summary with variances
- Charts visualizing expenses

## 🔧 Tech Stack
- Python: pandas, matplotlib, openpyxl, xlsxwriter
- Data: CSV files

---

# financial-tracking-system/requirements.txt
pandas
openpyxl
xlsxwriter
matplotlib

---

# financial-tracking-system/data/payroll.csv
Employee,Month,Salary
Alice,2025-06,5000
Bob,2025-06,4800
Carol,2025-06,5200

---

# financial-tracking-system/data/expenses.csv
Category,Month,Amount
Rent,2025-06,2000
Utilities,2025-06,500
Supplies,2025-06,1200
Marketing,2025-06,3500

---

# financial-tracking-system/src/data_loader.py
import pandas as pd

def load_data(payroll_path, expenses_path):
    payroll_df = pd.read_csv(payroll_path)
    expenses_df = pd.read_csv(expenses_path)
    return payroll_df, expenses_df

---

# financial-tracking-system/src/variance_checker.py
def detect_variance(expenses_df, threshold=0.2):
    mean = expenses_df['Amount'].mean()
    expenses_df['Variance'] = (expenses_df['Amount'] - mean) / mean
    anomalies = expenses_df[expenses_df['Variance'].abs() > threshold]
    return anomalies

---

# financial-tracking-system/src/report_generator.py
import pandas as pd

def generate_report(payroll_df, expenses_df, anomalies_df, output_path):
    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        payroll_df.to_excel(writer, sheet_name='Payroll', index=False)
        expenses_df.to_excel(writer, sheet_name='Expenses', index=False)
        anomalies_df.to_excel(writer, sheet_name='Anomalies', index=False)

        workbook = writer.book
        worksheet = writer.sheets['Expenses']

        chart = workbook.add_chart({'type': 'column'})
        chart.add_series({
            'categories': ['Expenses', 1, 0, len(expenses_df), 0],
            'values':     ['Expenses', 1, 2, len(expenses_df), 2],
            'name':       'Expense Amounts'
        })
        chart.set_title({'name': 'Expenses Overview'})
        worksheet.insert_chart('E2', chart)

---

# financial-tracking-system/src/main.py
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
