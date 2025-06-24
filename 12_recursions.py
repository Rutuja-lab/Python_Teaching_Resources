# RECURSION IN PYTHON

# Recursion is when a function calls itself.
# It is used to solve problems that repeat in smaller versions 
# of themselves.
# Every recursive function MUST have a 
# base case (to stop the function).

# Example 1: Print numbers from 5 to 1 using recursion
# print("Example 1: Print 5 to 1")
# def print_numbers(n):  
#     if(n == 0):    # base case
#         return     # stops calling the func right there
#     print(n)
#     print_numbers(n - 1)  #recursion

# print_numbers(5)

# Example 2: Factorial using recursion
# 2! = 2 * 1!          
# 3! = 3 * 2!
# 4! = 4 * 3!            n! = 1 * 2 * 3 *......* (n-1) * n
# n! = n * (n-1)!        n! = (n-1)! * n

# print("\nExample 2: Factorial")

# def factorial(n):
#     if(n == 0 or n == 1):
#         return 1
#     return n * factorial(n - 1)
    
# print("Factorial of 5 is", factorial(5))

# Example 3: Sum of n natural numbers using recursion
# sum_1 = 1
# sum_2 = 2 + 1 = 3
# sum_3 = 3 + sum_2
# sum_4 = 4 + sum_3
# sum_n = n + sum_(n-1)
# print("\nExample 3: Sum of first n natural numbers")
# def sum(n):
#     if(n == 1):
#         return 1
#     return n + sum(n - 1)

# print("Sum of first 5 numbers is", sum(5))

# # Example 4: Pattern printing using recursion
'''
*****
****
***
**
*
'''
# print("\nExample 4: Pattern printing")
# def pattern(n):
#     if(n == 0):
#         return
#     print("*" * n)
#     pattern(n - 1)

# pattern(5)

# # Example 5: Fibonacci series using recursion
# fibonacci series = (0, 1, 1, 2, 3, 5, 8, 13, 21,.....)
#     indexing ---->  0, 1, 2, 3, 4, 5, 6,  7,  8,
# print("\nExample 5: Fibonacci number")
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# print("7th Fibonacci number is", fibonacci(7))
