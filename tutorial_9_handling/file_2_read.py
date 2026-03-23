filename = "student_data.txt"
stdList = []
with open(filename) as obj:
    for line in obj.readlines():
        # print(line,end="")
        if(line.endswith("\n")):
            line = line[:-1]    
        stdList.append(line.split("|"))
    print()

print(len(stdList))
for i in range(len(stdList)):
    if(i!=0):
        print(f"Name: {stdList[i][0]}, Age: {stdList[i][1]}, Address: {stdList[i][2]}")
