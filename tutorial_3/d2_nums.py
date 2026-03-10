# Take three numbers and print max, min, sum and average

a = 15
b = 21
c = 15

if(a>b):
    # a is greater than b
    if(a>c):
        # a is greater than c and b
        print(f"{a} is max") 
    else:
        # a is not greater than c
        print(f"{c} is max") 
else:
    # a is not greater than b
    if(b>c):
        # a is greater than c and b
        print(f"{b} is max") 
    else:
        # a is not greater than c
        print(f"{c} is max") 
