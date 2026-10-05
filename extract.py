# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:43:19 2026

@author: Data
"""

import pandas as pd


def extract_data():
    """Read raw contact data from Excel."""

    df = pd.read_excel("data/contacts_raw.xlsx")

    print("Contact data extracted successfully!")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    return df


if __name__ == "__main__":
    df = extract_data()