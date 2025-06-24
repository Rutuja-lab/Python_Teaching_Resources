#A list can contain elements of any data type & it is changeable

l1 = ["1", "23", "8673", True, 300, 87.99]
#ind:  0    1       2      3    4    5    (indexing is shown)

print(l1)

a = len(l1)
print(a) #prints the length of the list

#list can be indexed just like strings
print(l1[1])
print(l1[0:]) #print(l1[0:6])

l1.remove("23") #removes that element
l1[0] = 4567 #changes that element to 4567
print(l1[0:5]) #prints elements indexed from 0 to 4

#A list can contain list, tuple, dictionary and set as an element
# for eg:
my_list = [["Riya",100],("Hari",99),{100:"Hello"},{2,3,4}]
print(my_list)

#1. reverse()
# order of elements is reversed
l2 = [89,6784,334,1]
l2.reverse()
print(l2)
l1.reverse()
print(l1)

l1 = [1007,"Rutuja",1007,35.98,True,0]
print(sum(l1))

#2. append method adds a new element to list l1
l1.append(56)
print(l1) 


#3. insert(index, element)
l1.insert(2, "YES")
print(l1)

#4. remove(element)
#This removes first occurence of the element
l1.remove(1007)
print(l1)

#5. count(element)
print(l1.count(1007))

#6. pop(index =)
print(l1.pop())

#7. sort()
l2 = [89,6784,334,1]
l2.sort()
print(l2)

#8. clear()
l2.clear()
l1.clear()
print(l1,l2)

'''Write a program to accept marks of 6 students
 and display them in a sorted manner.'''

# MARKS = []
# #convert strings to integers
# m1 = int(input("1. ENTER YOUR MARKS : "))
# MARKS.append(m1)
# m2 = int(input("2. ENTER YOUR MARKS : "))
# MARKS.append(m2)
# m3 = int(input("3. ENTER YOUR MARKS : "))
# MARKS.append(m3)
# m4 = int(input("4. ENTER YOUR MARKS : "))
# MARKS.append(m4)
# m5 = int(input("5. ENTER YOUR MARKS : "))
# MARKS.append(m5)
# m6 = int(input("6. ENTER YOUR MARKS : "))
# MARKS.append(m6)
# print(MARKS)
# MARKS.sort()
# print(MARKS)