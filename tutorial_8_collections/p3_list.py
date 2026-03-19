marks = []

marks.append(54)
marks.append(76)
marks.append(42.6)
marks.append(53)
marks.append(49)
marks.append("ninty two")

print(marks)


sum = 0
min = marks[0]
for i in range(len(marks)):
    sum = sum + marks[i]
    if(min > marks[i]):
        min = marks[i]

print(sum/len(marks))
print(min)