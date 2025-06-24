# sum(1) = 1
# sum(2) = 1+2
# sum(3) = 1+2+3
# sum(4) = 1+2+3+4
# sum(n) = 1+2+3+4+....+(n-1)+n
# sum(n) = sum(n-1)+n


n = int(input("Enter any number : "))
def sum(n):
    if(n==1):
        return 1
    elif(n<=0):
        print("Invalid input")
    else:
        return sum(n-1)+n
s = sum(n)
print(s)   
        