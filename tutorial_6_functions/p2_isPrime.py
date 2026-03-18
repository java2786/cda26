# find if given number is prime
# num = 65497
def isPrime(num):
    factors = 0

    for d in range (2, (num//2)+1):
        if(num%d==0):
            factors = factors + 1
            # print("factor found")
            break
        # else:
        #     print(num,"is not divided by",d)

    # print("Factors:",factors)
    if(factors>0):
        # print("Not prime")
        return False
    else:
        # print("Prime")
        return True 
    
    
print(f"4: {isPrime(4)}")
print(f"17: {isPrime(17)}")
print(f"89: {isPrime(89)}")
