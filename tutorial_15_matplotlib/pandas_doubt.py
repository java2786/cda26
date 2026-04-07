import pandas as pd

"""
			Math	Eng
Ramesh		87		64
Suresh		47		56
Dinesh		62		71
"""

# create DataFrame
df = pd.DataFrame({
    "Name": ["Ramesh", "Suresh", "Dinesh"],
    "Math": [87, 47, 62],
    "Eng": [64, 56, 71]
})

# filter
result = df[df["Math"] > 80]["Name"]
print(result.tolist())  # ['Ramesh']