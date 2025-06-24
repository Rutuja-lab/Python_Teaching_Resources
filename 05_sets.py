# Sets store unique elements and duplicate ones.
# are removed automatically and sets are unordered.
# Also, sets are unindexed.

my_set = {356, "Meeting", 12.78, True, 356, "Computer"}
print(my_set, type(my_set))

#1. adding element in a set
my_set.add("False")
print(my_set)

#2. discard(element)
# removes that element if present in the set but does not give 
# an error if that element is absent in the set
my_set.discard(True)
print(my_set)
my_set.discard(False)
print(my_set)


#3. remove(element)
# removes that element if present in the set but gives an error
# if that element is absent in the set
my_set.remove(356)
print(my_set)
my_set.remove(False)
print(my_set)


s1 = {356, "Meeting", 12.78, True, 356, "Computer"}
s2 = {78, 356, 12, "Computer", 567}


#4. union of two sets
# combines all the elements of more than 1 set without 
#repeating the same elements

union_set = s1.union(s2)
print(union_set)

#OR

print(s1.union(s2))

#5. intersection of two sets
#prints the common elements from both the sets

intersection_set = s1.intersection(s2)
print(intersection_set)

#OR

print(s1.intersection(s2))

#6. clear()
#clears the set
s1.clear()
print(s1)
s2.clear()
print(s2)
s = set()
print(s)