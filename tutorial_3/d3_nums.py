# Take three numbers and print max, min, sum and average

a = 21
b = 21
c = 71

if(a>b and a>c):
    print(f"{a} is max") 
elif(a>b and a<c):
    print(f"{c} is max") 
elif(a<b and b>c):
    print(f"{b} is max") 
elif(a<b and b<c):
    print(f"{c} is max")
elif(a==c and a>b):
    print(f"{c} is max")
elif(a==c and a<b):
    print(f"{b} is max")
    
