import pandas as pd
# import numpy as np

# print(np.__version__)
# print(pd.__version__)

# simple data
std_data = {
    "Name": ["Ramesh", "Sita", "Dinesh", "Gita"],
    "Age": [13, 12, 13, 11],
    "Male": [True, False, True, False],
    "Class": ["8th", "7th", "7th", "6th"],
    "Marks": [87, 93, 88, 64],
    "Address": ["Delhi", "Chennai", "Pune", "Delhi"]
}

print("Student data")
print(std_data)

df = pd.DataFrame(std_data)
print("Data in dataFrame")
print(df)

print("========")
print(df.info())