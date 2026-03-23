# filename = "abc.txt"
filename = "student_data.txt"
mode = "a"

with open(filename, mode) as obj:
    print("file is openned")
    # obj.write(f"\ngukesh|23|chennai")
    name = input("Enter std name: ")
    age = input("Enter std age: ")
    address = input("Enter std address: ")
    obj.write(f"\n{name}|{age}|{address}")
