n = int(input("Enter a number : "))

# upper part
for i in range(1, (n+1)//2 + 1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))
# lower part    
for i in range((n-1)//2, 0, -1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))    