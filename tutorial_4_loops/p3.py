# find if given number is prime
num = 65497
factors = 0

for d in range (2, num//2):
    if(num%d==0):
        factors = factors + 1
        print("factor found")
        break
    else:
        print(num,"is not divided by",d)

print("Factors:",factors)
if(factors>0):
    print("Not prime")
else:
    print("Prime")
    