import pandas as pd
import os

def extract():
    # Ensure the processed directory exists
    os.makedirs('data/processed', exist_ok=True)

    # Read the raw data
    df = pd.read_csv('data/raw/data.csv', encoding='ISO-8859-1')
    print(f"Extracted {df.shape[0]} rows and {df.shape[1]} columns.")

    # Save to processed path
    df.to_csv('data/processed/ecommerce_extracted.csv', index=False)
    return df

if __name__ == "__main__":
    extract()
