import array 

myArr = array.array('i')

myArr.append(4)
myArr.append(55)
# myArr.append("six")

print(myArr)
print(len(myArr))

myArr.remove(4)
print(myArr)
print(len(myArr))
