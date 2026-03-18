name = "super"

name = name.upper()

print(f"Last char: {name[-1]}")
print(f"2nd Last char: {name[-2]}")
print(f"3rd Last char: {name[-3]}")
print(f"4th Last char: {name[-4]}")
print(f"5th Last char: {name[-5]}")


print(f"1st char: {name[0]}")
print(f"2nd char: {name[1]}")
print(f"3rd char: {name[2]}")
print(f"4th char: {name[3]}")
print(f"5th char: {name[4]}")



print(f"Last char: {name[len(name)-1]}")
print(f"2nd Last char: {name[len(name)-2]}")
print(f"3rd Last char: {name[len(name)-3]}")
print(f"4th Last char: {name[len(name)-4]}")
print(f"5th Last char: {name[len(name)-5]}")

print(f"Last char: {name[len(name)-6]}")
print(f"2nd Last char: {name[len(name)-7]}")
print(f"3rd Last char: {name[len(name)-8]}")
print(f"4th Last char: {name[len(name)-9]}")
print(f"5th Last char: {name[len(name)-10]}")

# print(f"6th Last char: {name[len(name)-11]}") # out of range



# find all characters from 2 - super
print(f"substring: {name[1:4]}")
print(f"substring: {name[1:]}")

# find all characters till 3 - super
# slicing
print(f"substring: {name[2:4]}")

