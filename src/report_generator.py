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
