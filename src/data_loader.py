import pandas as pd

def load_data(payroll_path, expenses_path):
    payroll_df = pd.read_csv(payroll_path)
    expenses_df = pd.read_csv(expenses_path)
    return payroll_df, expenses_df
