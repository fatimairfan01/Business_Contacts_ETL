# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 12:27:21 2026

@author: Data
"""

from extract import extract_data
from transform import transform_data
from validate import validate_data


# Step 1: Extract
df = extract_data()


# Step 2: Transform
df = transform_data(df)


# Step 3: Validate transformed data
if validate_data(df):

    # Step 4: Load
    df.to_csv("data/contacts_cleaned.csv", index=False)

    print("Cleaned data loaded successfully!")
    print("ETL Pipeline completed successfully!")

else:
    print("ETL Pipeline stopped because validation failed.")