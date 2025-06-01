import pandas as pd
import os

def analyze():
    df = pd.read_csv('data/processed/customers_clean.csv')
    print(" Starting analysis...")

    df['Revenue'] = df['Quantity'] * df['UnitPrice']

    # 1. Total Revenue
    total_revenue = df['Revenue'].sum()

    # 2. Average Order Value
    order_values = df.groupby('InvoiceNo')['Revenue'].sum()
    avg_order_value = order_values.mean()

    # 3. Top 5 Products by Revenue
    top_products = df.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(5)

    # 4. Top 5 Customers by Revenue
    top_customers = df.groupby('CustomerID')['Revenue'].sum().sort_values(ascending=False).head(5)

    # 5. Monthly Sales Trend
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    monthly_sales = df.groupby('Month')['Revenue'].sum().reset_index()
    monthly_sales['Month'] = monthly_sales['Month'].astype(str)

    # Create folder for analysis outputs if not exists
    os.makedirs('data/analysis', exist_ok=True)

    # Save to CSV
    top_products.to_csv('data/analysis/top_products.csv')
    top_customers.to_csv('data/analysis/top_customers.csv')
    monthly_sales.to_csv('data/analysis/monthly_sales_trend.csv', index=False)

    # Save a summary metrics file
    summary = pd.DataFrame({
        'Metric': ['Total Revenue', 'Average Order Value'],
        'Value': [total_revenue, avg_order_value]
    })
    summary.to_csv('data/analysis/summary_metrics.csv', index=False)

    print(" Analysis complete. CSVs saved in 'data/analysis/'.")

if __name__ == "__main__":
    analyze()
