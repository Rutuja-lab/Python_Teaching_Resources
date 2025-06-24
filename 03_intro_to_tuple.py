'''A tuple can also contain elements of diffeent data types 
but it is non-changeable unlike list and is written in parenthesis'''

t = (123, 500, "Coding", "Python", 123, 45.09, False)
print(t)

print(t[1:] , t[4])

a = len(t)
print(a) #prints the length of the tuple

t1 = () #This is an empty tuple
print(len(t1))

#1. count(element)
#counts the number of occurences of an element
print(t.count(123))
print(t.count(12))
print(t.count(False))

#2. index(element)
#returns the index of the first occurrence of an element
print(t.index(500))

l = [123, 500, "Coding", "Python", 123, 45.09, False]
l[0] = 345
print(l)
# t[1] = 345
# print(t)
# This will give an error

# If there's only 1 element in a tuple then there should be a
# comma after that element or else it becomes an integer
t1 = (3,)
print(type(t1))
t2 = (3)
print(type(t2))