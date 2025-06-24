'''
READING A FILE FUNCTION
'''

# A file can be opened and read using this function.
# Open function is a built-in function.
# This function allows two arguments to be passed.
# First one is the name of the file and the second one is 
# for the specification of the mode in which we want the file to 
# open.
# | Mode | Description        |
# | ---- | ------------------ |
# | "r"  | open for reading   |
# | "w"  | open for writing   |
# | "+"  | open for updating  |
# | "a"  | open for appending |


# f.read() - Reads the whole file as one string
# text = f.read()

# Example 1. Reading a file

# print("Example 1. Reading a file")

# f = open("to_be_read.txt","r")
# text = f.read()   # The no.of characters to be read can be 
# print(text)       # specified in the parentheses           
# f.close()

# f.readline() - Reads one line at a time

# Returns an empty string ('') if called after the last line of 
# the file

# Example 2. Reading a file line by line

# print("\nExample 2. Reading a file line by line")

# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# line3 = f.readline()
# print(line3)
# line4 = f.readline()
# print(line4)

#  Using with Statement (Best Practice)
# with open("to_be_read.txt", "r") as f:
#     text = f.read()
# print(text)

'''
WRITING TO A FILE
'''

# "w"  - open for writing to a file
# To write to a file, we first open it in write or append mode
# after which we use f.write() method to write to the file
# f.write only writes string to a file

# Example 1. Writing to a file
# print("Example 1. Writing to a file")
# f = open("to_write.txt", "w")
# f.write("\nI am praying for your well being")
# f.close


# When a file is opened in "w" mode, the already existing
# content in the file is replaced by the content written
# to it using write function
# But when some content is to be added in the file while
# not letting the previous content wiped out, "a" mode
# should be used

# Example 2.Writing to a file using append mode ("a")

# print('''Example 2.Writing to a file using append
#  mode ("a")''')

# f = open("to_write.txt", "a")
# f.write("Hello! How are you?")
# f.close


# Opening a file in write mode and writing nothing wipes
# out the content of the file

# Example 3. Wiping out content from a file

# print("Example 3. Wiping out content from a file")

# with open("to_write.txt","w") as f:
#     f.write("")