# Student, Employee, Payment, Bank, Car, Item, ...


class Student:
    # constructor
    def __init__(self, n, a):
        self.name = n
        self.age = a 
        print("i am in const")
    
    def getDetails(self):
        print(f"Name: {self.name}, Age: {self.age}")

# s1 = Student()  
    
s1 = Student("ramesh", 21)
s2 = Student("mahesh", 23)

s1.getDetails()

name = "kamlesh"
name.upper()
