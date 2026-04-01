import pandas as pd

# showing progress of single student wrt different tests
# 1st Term, 2nd Term, Final
terms_progress = pd.Series(
    [64, 89, 85],
    index=["1st Term", "2nd Term", "Final"],
    name = "Report Card"
)

print(terms_progress)


sales = pd.Series(
    [120000, 230000, 190000, 175000],
    index = ["Jan-Mar", "Apr-Jun","Jul-Sep", "Oct-Dec"],
    name = "Revenue"
)

# print(sales)
# print(sales.info())

print("Quarter wise sale")
print("2nd Quarter sales:", sales["Apr-Jun"])
print("Average sale:", sales.mean())
print("Total sale:", sales.sum())
