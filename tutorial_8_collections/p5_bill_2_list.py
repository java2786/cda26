'''
Sohan's Restaurant, show menu
    Dosa - 80
    Idli - 35
    ColdDrink - 60

Mohan -> 2 Dosa, 5 Idli, 1 ColdDrink 
find total bill
'''

items = ["dosa","idli","coldDrink"]
prices = [50,25,35]
quantities = []
bills = []
totalBill = 0
len = len(items)


print("Welcome to Sohan's Restaurant")
print("Our menu")
for i in range(len):
    print(f"{i+1}. {items[i]} - Rs{prices[i]}")


for i in range(len):
    quantities.append(int(input(f"{items[i]} Quantity: ")))
    bills.append(prices[i]*quantities[i])
    totalBill = totalBill + (prices[i]*quantities[i])


print("\n\n===========Mohan's Bill=============")
for i in range(len):
    print(f"{items[i]}: {quantities[i]}x Rs {prices[i]} = {bills[i]}")
print("--------------------------------------------------------------------")
print(f"Total bill: Rs {totalBill}")
print("Thank you")