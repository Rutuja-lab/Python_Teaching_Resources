# Loops are used to avoid repetition and to work with
# collections like list, tuple, etc.

# Example 1: Print numbers from 1 to 5 using a for loop
# print("Example 1: Numbers from 1 to 5")
# for i in range(1, 6):  (everything in a singl line)
#     print(i)


# n = 1 #initiate
# while(n<=1000): #condition
#     print(n)
#     n += 1 #n = n + 1 increment/decrement

# Example 3: Print even numbers between 1 to 10
# print("\nExample 3: Even numbers between 1 and 10")
# for i in range(1, 11):
#     if(i % 2 == 0):
#         print(i)

# Example 4: While loop to count down from 5 to 1
# print("\nExample 4: Countdown using while loop")
# count = 5
# while(count > 0):
#     print(count)
#     count -= 1 #count = count - 1

# Example 5: Using break to stop a loop early
# print("\nExample 5: Stop printing when number is 4 (using break)")
# for i in range(1, 6):
#     if i == 4:
#         break  # Loop stops here
#     print(i)

# Example 6: Using continue to skip number 3
# print("\nExample 6: Skip number 3 (using continue)")
# for i in range(1, 6):
#     if i == 3:
#         continue  # Skip the rest of the loop for i = 3
#     print(i)

# Example 7: Use of pass in loop (placeholder)
# print("\nExample 7: Loop with pass (does nothing inside the loop)")
# for i in range(1, 6):
#     if i == 3:
#         pass  # Placeholder: Nothing happens here
#     else:
#         print(f"{i} is not 3")

# Example 8: While loop with condition check and pass
print("\nExample 8: While loop with pass")
x = 1
while x <= 5:
    if x == 3:
        pass  # Do nothing when x is 3
    else:
        print(f"x = {x}")
    x += 1

