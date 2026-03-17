"""
w - 6
h - 8

* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *

"""

height = int(input("Enter height: "))
width = int(height * .70) 

for h in range(height):

    for w in range(width):
        print("* ",end="")
        # print(h," ",end="")
        # print(w," ",end="")
        # print(h,w," ",end="",sep="")
    print()

