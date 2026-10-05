# Business Contacts ETL Pipeline

A Python-based ETL (Extract, Transform, Load) pipeline for cleaning, validating, and processing business contact data.

## Project Overview

This project demonstrates a basic data engineering workflow using Python and Pandas.

The pipeline takes raw business contact data from an Excel file, cleans and transforms the data, validates the processed dataset, and finally exports the cleaned data as a CSV file.

## ETL Process

The project follows three main ETL stages:

### 1. Extract
Reads raw business contact data from an Excel file using Pandas.

### 2. Transform
The data is cleaned and standardized by:

- Removing extra spaces
- Converting emails to lowercase
- Cleaning phone and landline numbers
- Standardizing salutations
- Handling missing email and phone values
- Removing duplicate records

### 3. Load
After successful validation, the cleaned dataset is exported to a CSV file.

## Data Validation

The pipeline validates the processed data by checking:

- Required columns
- Duplicate records
- Missing values
- Number of rows and columns

The pipeline stops if validation fails.

## Technologies Used

- Python
- Pandas
- Excel
- CSV
- GitHub

## Project Structure

```text
Business_Contacts_ETL/
│
├── generate_data.py
├── extract.py
├── transform.py
├── validate.py
├── pipeline.py
│
└── data/
    ├── contacts_raw.xlsx
    └── contacts_cleaned.csv
