#guess the number
num=60
x=int(input("enter a integet between 1 and 100:"))
if(x<100 and x>0):
    if(num==x):
        print("your guess is correct")
    if(num>x):
        print("guess higher")
    else:
        print("guess lower")
else:
    print("number is out of range") 

