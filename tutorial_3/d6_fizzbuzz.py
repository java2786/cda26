"""
L412

Given an integer n, print a string :

answer == "FizzBuzz" if n is divisible by 3 and 5.
answer == "Fizz" if n is divisible by 3.
answer == "Buzz" if n is divisible by 5.
 

Example 1:
    Input: n = 3
    Output: Fizz

Example 2:
    Input: n = 10
    Output: Buzz

Example 3:
    Input: n = 15
    Output: FizzBuzz
"""


input_str = input("Enter a number: ") # sequence of chars - 432
n = int(input_str) # input is converted into digits - num

# if(n%3==0):
#     print("Fizz",end="")
# if(n%5==0):
#     print("Buzz",end="")


# print()



if(n%3==0 and n%5==0):
    print("FizzBuzz")
elif(n%3==0):
    print("Fizz")
elif(n%5==0):
    print("Buzz")

