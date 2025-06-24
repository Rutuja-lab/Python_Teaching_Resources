   # Object Oriented Programming

'''
1. A problem is solved by creating objects.

Instead of writing everything step by step, a Class 
acts as a blueprint which is used to create
objects (real things).
A class is like a blank form and when that form
is filled by a particular person, it becomes an
object.

2. This approach is used in programming to 
organize code more effectively.

3. Big problems can be made easier to manage.

'''
class Student:  # class definition
    school = "Saraswati High School"
    standard = 10
# class attributes

Raju = Student() # object instantiation
Raju.marks = 88  # instance attribute
print(Raju.school,   Raju.standard,   Raju.marks)    
'''
1. When a class is defined, a template is defined.
Memory is allocated only after object instantiation
ie, after creating an object from that class.

2. Just like there are nouns in English grammar,
there are classes in OOP languages, similarly, 
attributes can be compared to adjectives, and 
methods to verbs.

3. ATTRIBUTES :
a) Class attributes are the attributes that belong 
to the class and not just to a particular instance
or object.

b) Instance attributes are the attributes that
belong to a particular instance (object) of a 
class.

During assignment and retreival, instance attribute 
takes preference over class attribute.

4. METHOD :
It is a function inside class that tells what its
object can do.

'''
class anything:
    a = 20
    
obj = anything()  
obj.a = 0
print(obj.a)  

class Student:  # class definition
    def greet():
        print("HELLO THERE!")


    school = "Saraswati High School"
    standard = 10
# class attributes

Raju = Student() # object instantiation
Raju.marks = 88  # instance attribute
Raju.greet()   # Student.greet(Raju)
print(Raju.school,   Raju.standard,   Raju.marks)

'''
Even though greet() doesnt't use self.standard 
or self.school, self should still be written as
the first parameter because, when Raju.greet()
is called, Python secretly does -
Student.greet(Raju)    
Here, Raju is passed as the self parameter.
So self is automatically passed even if we don't
use it.
'''

class Student:  # class definition
    @staticmethod
    def greet():
        print("HELLO THERE!")

    school = "Saraswati High School"
    standard = 10
# class attributes

Raju = Student() # object instantiation
Raju.marks = 88  # instance attribute
Raju.greet()   # Student.greet(Raju)
# print(Raju.school,   Raju.standard,   Raju.marks)

'''
When @staticmethod is used, Python doesn't pass
the object.
'''

class Student:  # class definition
    school = "Saraswati High School"
    standard = 10
# class attributes
    
    @staticmethod
    def greet():
        print("HELLO THERE!")

    # constructor
    def __init__(self,name,marks,age):
        self.name = name
        self.marks = marks
        self.age = age
        print(f"{self.name} scored {self.marks}")
        print(f"{self.name}'s age is {self.age}")

raju = Student("Raju",97,15)
raju.greet()

'''
__init__ constructor :
1. It is a method which runs first when an object is 
instantiated. This method runs automatically when 
an object is created which means there's no need 
to call that function exclusively.

2. It takes self argument and can also take many other
arguments as well. 
'''


# Write a class Train which has methods 
# to book a ticket, get status (no. of seats) 
# and get fare information of trains running 
# under Indian Railways.

# class Train:
#     def __init__(self,name,seats,fare):
#         self.name = name
#         self.seats = seats
#         self.fare = fare   

#     def get_status(self):
#         print(f"The name of the train is {self.name}.")           
#         print(f"No.of seats available in the train are {self.seats}.") 

#     def fare_info(self):
#         print(f"The fare of one ticket is {self.fare}.")   

#     def book_ticket(self):
#         if (self.seats > 0):
#             print("Tickets are available.") 
#             self.seats -= 1  
#         else:
#             print("Sorry, no ticktes available.")     

# Rajdhani = Train("Rajdhani Express",10,200)   
# Rajdhani.get_status()
# Rajdhani.fare_info()
# Rajdhani.book_ticket()                