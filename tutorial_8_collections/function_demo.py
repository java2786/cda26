# simple function
def getUserInfo():
    name = input("Enter your name: ")
    print("Welcome",name.capitalize())
    
# arguments in function
# function can return 
def add(a,b):
    sum = a+b
    return sum 

# default arguments in function
def mul(a,b=1):
    result = a*b
    return result 

mul(3)
mul(4,2)


# keyword arguments
def studentInfo(**kwargs):
    print(type(kwargs))
    print(kwargs)

print("===============")    
marks = [76,81,84]
# studentInfo(marks)
studentInfo(name="Ramehs", age=43, address="Pune")

def studentDetails(*args, **kwargs):
    print(type(args)) # data is stored in tuple
    print(args[0][1])    
    print(type(kwargs)) # data is stored in dictionary

print("**********************")
studentDetails(marks, "abc", name="Ramehs", age=43, address="Pune")
