# - Input two numbers and swap them using a third variable.  

# a = input("Enter first number")
# b = input("Enter second number")

# print(f"Before swap-> A: {a}, B: {b}")
# c = a 
# a = b 
# b = c 
# print(f"After swap-> A: {a}, B: {b}")



# swap without third variable
# a = int(input("Enter first number")) # 4
# b = int(input("Enter second number")) # 5

# print(f"Before swap-> A: {a}, B: {b}")
# a = a + b 
# b = a - b 
# a = a - b 
# print(f"After swap-> A: {a}, B: {b}")


a = int(input("Enter first number: ")) # 4
b = int(input("Enter second number: ")) # 5

print(f"Before swap-> A: {a}, B: {b}")
a = a * b # 20
b = a / b # 4
a = a / b # 5
print(f"After swap-> A: {a}, B: {b}")

