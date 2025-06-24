# MORE ON OOPs

'''
RECAP :
       Class = Blueprint
       Object = Real thing based on the class
       Attribute = Object's properties
       Method = Object's action
'''

'''
INHERITANCE :
A process in which a class (called child or subclass) can acquire
the properties and methods of another class (called parent
or superclass)
'''

# Example 1. This is an example of single inheritance
print("Example 1. This is an example of single inheritance")


class Student:    # parent class or superclass
    College = "R. S. Jr. College"

    def study(self):
        print(f"{self.name} is studying...")
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print(f"{self.name} scored {self.marks} marks.")
        
    
class  Topper(Student):  # base/child class or subclass
    def praise(self):
        print(f"{self.name} is a Topper!")

Aman = Student("Aman",80)
Aman.study()
print(Aman.College)

print("_________________________________")
Nita = Topper("Nita",100)
Nita.study()
Nita.praise()
print(Nita.College)

# TYPES OF INHERITANCE :

'''
1. Single inheritance - One child class is created from one parent class.

2. Multiple inheritance - One child class is created from multiple
parent classes.

3. Multilevel inheritance - A class is created from a child class 
which was created from a parent class.

4. Hierarchal inheritance - Multiple child classes are created from
a single parent class.

5. Hybrid inheritance - Combination of 2 or more inheritance in one
program.
'''

# Example 2. This is an example of multiple inheritance
print("\nExample 2. This is an example of multiple inheritance")

class Student:    # parent class or superclass
    College = "R. S. Jr. College"

    def study(self):
        print(f"{self.name} is studying...")
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print(f"{self.name} scored {self.marks} marks.")

class EleventhGrade:
    def grade(self):
        
        print("This student studies in eleventh grade.")

class LazyStudent(Student,EleventhGrade):
    def study(self):
        print(f"{self.name} will study tomorrow....")

    # This is an overridden method wherein LazyStudent rewrote
    # its own version of already existing study() method in Student    

    def excuse(self):
        print(f"{self.name} doesn't study because she feels sleepy.")    

Reshma = Student("Reshma",88)
Reshma.study()

print("__________________________________")
Daksh = EleventhGrade()
# Daksh.study() # returns an error
Daksh.grade()


print("__________________________________")
Himani = LazyStudent("Himani",60)
Himani.grade()
Himani.study()
Himani.excuse()

# Example 3. This is an example of multilevel inheritance
print("\nExample 3. This is an example of multilevel inheritance")

class Student:    # parent class or superclass
    College = "R. S. Jr. College"

    def study(self):
        print(f"{self.name} is studying...")
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print(f"{self.name} scored {self.marks} marks.")

class RegularStudent(Student):

    def homework(self):
        print(f"{self.name} does homework regularly")

class SincereStudent(RegularStudent):

    def routine(self):
        print("Prepares for exam in advance, also helps others.")  

rohan = SincereStudent("Rohan",95)
rohan.study()
rohan.homework()
rohan.routine()              