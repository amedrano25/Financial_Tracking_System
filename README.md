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
