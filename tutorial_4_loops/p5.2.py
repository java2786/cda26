"""
num = 12345
- reverse the digits to form new number - 54321

"""

num = 426
result = 0 

while(num!=0):
    ld = num%10
    result = (result*10)+ld 
    num = num//10