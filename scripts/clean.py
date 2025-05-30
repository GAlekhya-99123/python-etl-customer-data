import pandas as pd

def clean():
    df = pd.read_csv('data/processed/ecommerce_extracted.csv')
    print(f"Starting cleaning with {df.shape[0]} rows.")
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['CustomerID', 'InvoiceNo'], inplace=True)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df = df[~df['InvoiceNo'].str.startswith('C')]  # remove cancelled orders
    print(f"Cleaned data has {df.shape[0]} rows.")
    df.to_csv('data/processed/customers_clean.csv', index=False)
    return df

if __name__ == "__main__":
    clean()
