import pandas as pd
# import numpy as np

# print(np.__version__)
# print(pd.__version__)

railway_data = [
    ['Mumbai-Delhi', 1250, 'AC-1'],
    ['Chennai-Bangalore', 930, 'AC-2'],
    ['Jaipur-Delhi', 1100, 'Sleeper'],
    ['Pune-Delhi', 570, 'AC-3']
]

df = pd.DataFrame(
    railway_data,
    columns=["Route", "Price", "Class"]
)

print(df)