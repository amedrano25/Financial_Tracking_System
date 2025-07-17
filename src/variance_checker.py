def detect_variance(expenses_df, threshold=0.2):
    mean = expenses_df['Amount'].mean()
    expenses_df['Variance'] = (expenses_df['Amount'] - mean) / mean
    anomalies = expenses_df[expenses_df['Variance'].abs() > threshold]
    return anomalies
