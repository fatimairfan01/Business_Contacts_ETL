# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:45:57 2026

@author: Data
"""

import pandas as pd


def transform_data(df):

    # Name ke extra spaces remove karo
    df["Name"] = df["Name"].str.strip()

    # Designation ke extra spaces remove karo
    df["Designation"] = df["Designation"].str.strip()

    # Company ke extra spaces remove karo
    df["Company_Name"] = df["Company_Name"].str.strip()

    # Email ko lowercase karo
    df["Email"] = df["Email"].str.lower()

    # Phone number clean karo
    df["Phone_No"] = (
        df["Phone_No"]
        .astype(str)
        .str.replace("-", "", regex=False)
        .str.strip()
    )

    # Landline clean karo
    df["Landline"] = (
        df["Landline"]
        .astype(str)
        .str.replace("-", "", regex=False)
        .str.strip()
    )

    # Salutation ko clean aur consistent karo
    df["Salutation"] = df["Salutation"].str.strip().str.title()

    # Missing Email ko handle karo
    df["Email"] = df["Email"].fillna("Not Available")

    # Missing Phone Number ko handle karo
    df["Phone_No"] = df["Phone_No"].fillna("Not Available")

    # Duplicate records remove karo
    df = df.drop_duplicates()

    print("Data transformed successfully!")
    print("Rows after cleaning:", len(df))
    print("Duplicate rows:", df.duplicated().sum())
    print("Missing values:", df.isnull().sum().sum())

    return df


if __name__ == "__main__":

    df = pd.read_excel("data/contacts_raw.xlsx")
    df = transform_data(df)