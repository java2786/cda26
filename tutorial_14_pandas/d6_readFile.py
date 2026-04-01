import pandas as pd

try:
    std_report = pd.read_csv("report_card.csv")
    print(std_report)
except (FileNotFoundError):
    print("File not found")