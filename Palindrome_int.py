# Palindrome number using while loop 
n = int(input("Enter a number : "))
original_n = n
rev_n = 0
while(n>0):
    rem = n%10 
    rev_n = (rev_n*10)+rem
    n = n//10     #numbers after point are not shown (floor division)
if(rev_n==original_n):
    print(f"{original_n} is a palindrome number")
else:
    print(f"{original_n} is not a palindrome number")