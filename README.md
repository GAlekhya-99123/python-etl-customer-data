# Python ETL Pipeline for Customer Data

This repo contains an end-to-end data pipeline using Python for extracting, cleaning, and loading customer records.

## Features:
- Cleans nulls, duplicates, and inconsistent types
- Aggregates data by behavior segments
- Exports clean datasets for BI tools (CSV/SQL)

## Technologies:
- Python, Pandas, SQLAlchemy, Jupyter

## Sample Output:
`data_cleaned/customers_clean.csv`
Repo Structure
├── README.md
├── requirements.txt
├── scripts/
│   ├── extract.py
│   ├── clean.py
│   └── load.py
└── data/
    └── sample_input.csv
