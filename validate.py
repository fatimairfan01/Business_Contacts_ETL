# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 12:19:57 2026

@author: Data
"""

import pandas as pd


def validate_data(df):

    print("Validation started...")

    # Rows aur columns check karo
    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    # Duplicate records check karo
    duplicate_rows = df.duplicated().sum()
    print("Duplicate rows:", duplicate_rows)

    # Missing values check karo
    missing_values = df.isnull().sum().sum()
    print("Missing values:", missing_values)

    # Required columns check karo
    required_columns = [
        "Name",
        "Designation",
        "Company_Name",
        "Email",
        "Address",
        "Phone_No",
        "Landline",
        "Website",
        "Salutation"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    # Validation conditions
    if missing_columns:
        print("Missing columns:", missing_columns)
        return False

    if duplicate_rows > 0:
        print("Validation failed: Duplicate rows found.")
        return False

    if missing_values > 0:
        print("Validation failed: Missing values found.")
        return False

    print("Validation successful!")

    return True


if __name__ == "__main__":

    df = pd.read_excel("data/contacts_raw.xlsx")

    validate_data(df)