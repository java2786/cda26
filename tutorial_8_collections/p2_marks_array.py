import array 

marks = array.array('i')
"""
0 index - Math
1 index - SSt
2 index - Science
3 index - English
4 index - Computer

"""
marks.append(54)
marks.append(76)
marks.append(82)
marks.append(53)
marks.append(49)


# print(f"Third subject score: {marks[2]}")
# print(marks[-1])

sum = 0
min = marks[0]
for i in range(len(marks)):
    sum = sum + marks[i]
    if(min > marks[i]):
        min = marks[i]

print(sum/len(marks))
print(min)