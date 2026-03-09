"""
Conditional Operators

operations perform - class <int>
isSame ->               ==
not same ->             !=
less than ->            <
less than equals ->     <=
greater than ->         >
greater than equals ->  >=

"""

a = 6
b = 6

if(a>b):
    print(f"{a} is greater than {b}")
elif(a<b):
    print(f"{b} is greater than {a}")
else:
    print(f"Both values are same, {b}")
    