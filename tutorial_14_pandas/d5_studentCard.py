import pandas as pd 
import numpy as np

marks = np.random.randint(40, 95, (5, 4))
# print(marks)
students = ["Ramesh", "Suresh", "Dinesh", "Gukesh", "Mukesh"]
subjects = ["Physics", "Maths", "English", "Computer"]

dfMarks = pd.DataFrame(marks, index=students, columns=subjects)
print(dfMarks)

# pip install openpyxl - to save excel file
# Save data into file
# dfMarks.to_excel("report_card.xlsx", index=False)


dfMarks.to_csv("report_card.csv", index=False)