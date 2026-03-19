num = 22345666

list = []

for i in range(10):
    list.append(0)

while(num>0):
    ld = num % 10
    num = num //10
    list[ld] = list[ld] + 1

for i in range(10):
    if(list[i]!=0):
        print(f"{i} occurrance is {list[i]}")