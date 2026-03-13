# num = 76543, count digits

num = 524
count = 0

# while(num!=0):
while(num>0):
    ld = num%10         # 5
    num = num//10       # 34
    count = count+1     # 1

print(count)


