"""
num = 12345
- reverse the digits to form new number - 54321

"""

num = 1234
copy = num
count = 0
result = 0

while(num>0):
    ld = num%10         
    num = num//10       
    count = count+1     

num = copy 

while(num>0):
    ld = num%10
    result = result + (ld * (10 ** (count-1)))
    num = num//10
    count=count-1
