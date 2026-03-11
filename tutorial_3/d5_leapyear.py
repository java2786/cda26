"""
2000 → leap year ✅
1900 → not a leap year ❌
2024 → leap year ✅
"""

year = 2024

if((year%100==0 and year%400==0) or year%4==0):
    print("leap year")