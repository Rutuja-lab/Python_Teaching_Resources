# Write a program to mine a log file and 
# find out whether it contains the word 
# "python".

with open("log.txt","r") as f:
    lines = f.readlines()

for line in lines:
    if "python" in line:
        print("Yes the word python is present")
        break
else:
    print("No the word python is not present")


# WAP to find the line number where python is present
# in previous question 

with open("log.txt","r") as f:
    lines = f.readlines()

lineno = 1

for line in lines:
    if "python" in line:
        print("Yes the word python is present")
        print(f"Line number : {lineno}")
        break
    lineno += 1
else:
    print("No the word python is not present")    