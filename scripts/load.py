import pandas as pd

def load():
    df = pd.read_csv('data/processed/customers_clean.csv')
    print(f"Loaded cleaned data with {df.shape[0]} rows and {df.shape[1]} columns.")

if __name__ == "__main__":
    load()
