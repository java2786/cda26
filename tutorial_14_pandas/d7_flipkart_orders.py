import pandas as pd 
import numpy as np

count = 200
startId = 101

orders = {
    "OrderId": np.arange(startId, startId+count),
    "CustomerName": ["Ramesh", "Suresh", "Dinesh", "Gukesh", "Mukesh"] * (count//5),
    "City": ["Delhi", "Chennai", "Pune", "Delhi", "Jaipur"] * (count//5),
    "ProductCategory": ["Electronics", "Home", "Fashion", "Accessories", "Toys"] * (count//5),
    "Amount": np.random.randint(200, 10001, count),
    "Discount": np.random.randint(1, 11, count),
    "PaymentMode": ["UPI", "Card", "Online", "COD", "Wallet"] * (count//5)
}

# print(orders)
df = pd.DataFrame(orders)
print(df)


print("="*70)
print("\t\t\t\tData Analysis")
print("="*70)

# 1. view first n records
print("\nFirst 3 rows:")
print(df.head(3))

# 2. view first n records
print("\nLast 3 rows:")
print(df.tail(3))

# 3. shape (row, column)
print(f"\nShape: {df.shape[0]} rows x {df.shape[1]} columns")

# 4. column name and datatype
print(f"\n{df.dtypes}")


# 5. Basic Statistics
print(f"\nStatistical Summary")
print(df.describe())

# 6. Check for missing data
print(f"\nMissing data")
print(df.isnull().sum())


""" 
write the data into csv file
delete some random cells
and read data from csv file 

find how many missing values are there
"""


# 7. Unique cities:
print(f"\nUnique Cities:")
print(df['City'].unique())

# 8. Count by cities: (Group by)
print(f"\nSales data by Cities:")
print(df['City'].value_counts())

