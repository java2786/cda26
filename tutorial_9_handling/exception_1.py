try:
    num = int("43two")
except(ValueError):
    print("Input is wrong")

    a = 5
    b = 0
try:
    result = a//b

    print(f"Result is {result}")    
except(ZeroDivisionError):
    print("divide by zero is not possible")
