# A collection of key value pairs is known as a dictionary
marks = {"Science":93,
         "Maths":95,
         "C++, Js":[90,95]
}
print(marks)

print(marks["Maths"])
print(marks["C++, Js"])

#1. update({key:value})
# Keys are unique, if a same key is added again then the
# value of the updates
marks.update({"GK":100})
print(marks)
marks.update({"Science":98})
print(marks)

#2. get(key)
#prints the value of the given key
print(marks.get("Maths"))

#3. items()
#prints the elements/items in the dictionary in the form
#of a list
print(marks.items())

#4. keys()
#prints all the keys in the form of a list
print(marks.keys())

#5. values()
#prints all the values in the form of a list
print(marks.values())

# get method does not give an error even though the value
# of a non-existing key is asked unlike dict[key] method

print(marks.get("Science"))
print(marks["Science"])

print(marks.get("English"))
# print(marks["English"])

# empty dict can also be created
dict = {}
print(dict)


# Write a program to create a dictionary of Hindi words 
# with values as their english translation. Provide user 
# with an option to look it up! 

words = {
      "chaabi":"key",
"darvaja":"door", 
 "madat":"help"
 }
word = input("Enter the word you want meaning of : ")
print(words[word])