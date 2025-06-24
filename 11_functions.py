# FUNCION IN PYTHON

# A function is a set of lines/instructions which
# performs specific task.
# A func. can be called in a program any number 
# of times and anywhere.
# Functions make it easy to handle big and complex
# programs.

# Example 1. Greet user hello using function
# print("Example 1. Greet user hello using function")
# #function definition
# def greet():
#     print("Hello!")
# #function calling
# greet()

# Example 2. Printing 5 to 1 using function
# print("\nExample 2. Printing 5 to 1 using function")
# def numbers():
#     for i in range(5,0,-1):
#         print(i)
# numbers()    

# Function with argument - It takes some input to 
# perform its task
# An argument is the actual value you pass into
# the function when you call it. 
# print("\nExamples using function with arguments")
# print("\nExample 1.")
# # func definition
# def greet(name):   #name is parameter (placeholder)  
#                     # here (acts like a label)
#     print("Hello ",name)
# #func calling    
# greet("Rutuja")    #"Rutuja" is the argument here(acts 
                     # like content stored in label).....
                     # it is the actual value passed
# print("\nExample 2.")
# # func definition   
# def add(a,b):
#     print(f"Sum of {a} and {b} is ",a+b)
# add(4,5)    #func calling 
# 
# def add(a,b):
#      return a+b
# add(3,5)          #( won't display anything)

# print("\nExample 3.") 
# def multiply(a,b):
#      return (a*b)      #(returns value of a*b when called) 
# # product = multiply(3,5)
# # print("Product of 3 & 5 is ",product)  
# print(f"Required product is {multiply(3,5)}") 
# 
# print("Example 4.")            
# def square(num):
#     return (num * num)
# print(f"Required square is {square(9)}")

# def square(num):
#      print(num * num)
# square(9)

# Program to convert inches in cm
# value_in_inches = float(input("Enter value in inches that " \
# "you want to convert to cm : "))

# def in_to_cm(value_in_inches):
#     return value_in_inches * 2.54

# print(f"The value of {value_in_inches} inches in cm is " \
#      f"{in_to_cm(value_in_inches)} cm")

