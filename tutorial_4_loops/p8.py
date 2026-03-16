num = 9456

sum = 0
while(num>0):
    sum = sum + (num%10)
    num = num // 10
    # print(f"sum: {sum}")
    if(num==0 and sum>9):
        # print("repeat")
        num = sum
        sum = 0
    elif(num==0 and sum<10):
        print("Answer:",sum)