# find all string numbers from 1 to 1000

for num in range(1, 1001):
    copy = num
    result = 0

    while(num > 0):
        # step 1
        ld = num % 10

        fact = 1
        for counter in range(1,ld+1):
            fact = fact * counter

        result = result + fact

        num = num // 10

    if(copy==result):
        print(f"{copy} is strong number")
