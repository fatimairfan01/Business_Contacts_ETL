# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:33:47 2026

@author: Data
"""

import pandas as pd
import random

names = [
    "Ali Khan",
    "Sara Ahmed",
    "Usman Raza",
    "Fatima Noor",
    "Hassan Ali",
    "Ayesha Malik",
    "Bilal Ahmed",
    "Mariam Khan"
]

designations = [
    "Manager",
    "Director",
    "HR Manager",
    "Sales Manager",
    "CEO",
    "Marketing Manager",
    "Accountant"
]

companies = [
    "ABC Pvt Ltd",
    "XYZ Solutions",
    "Tech World",
    "Pak Enterprises",
    "Digital Hub"
]

cities = [
    "Karachi",
    "Lahore",
    "Islamabad",
    "Faisalabad"
]

salutations = [
    "Mr.",
    "Ms.",
    "Mrs."
]

data = []

for i in range(1000):

    name = random.choice(names)
    designation = random.choice(designations)
    company = random.choice(companies)
    city = random.choice(cities)

    email_name = name.lower().replace(" ", ".")
    email = email_name + "@example.com"

    phone = "03" + str(random.randint(100000000, 999999999))
    landline = "021" + str(random.randint(10000000, 99999999))

    website = "www." + company.lower().replace(" ", "") + ".com"

    salutation = random.choice(salutations)

    address = "Main Road, " + city

    data.append([
        name,
        designation,
        company,
        email,
        address,
        phone,
        landline,
        website,
        salutation
    ])


columns = [
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

df = pd.DataFrame(data, columns=columns)


# -----------------------------
# INTENTIONALLY MAKE DATA MESSY
# -----------------------------

# Extra spaces
df.loc[5, "Name"] = "  " + df.loc[5, "Name"] + "  "
df.loc[10, "Company_Name"] = "  " + df.loc[10, "Company_Name"] + "  "

# Uppercase email
df.loc[15, "Email"] = df.loc[15, "Email"].upper()

# Phone number mein hyphens
df.loc[20, "Phone_No"] = "0300-1234567"

# Landline mein hyphens
df.loc[25, "Landline"] = "021-12345678"

# Missing email
df.loc[30, "Email"] = None

# Missing phone
df.loc[35, "Phone_No"] = None

# Duplicate record
df.loc[40] = df.loc[41]


# Save raw data
df.to_excel("data/contacts_raw.xlsx", index=False)

print("Messy raw contacts data created successfully!")
print("Total rows:", len(df))
print("Total columns:", len(df.columns))