# Property Decorator, Getter & Setter

'''
I) PROPERTY DECORATOR :

@property is a built-in decorator in Python used to 
define a method as a property. It allows us to access methods 
like attributes (without parentheses). 
'''

# GETTER IS USED TO CONTROL WHAT USER SEES

print("GETTER")
'''
II) Getter :
 1. A getter is a method (function inside a class) which is used to 
access or read the value of a private variable safely, because sometimes
we don't want others to mess with a variable directly from outside 
the class. '''

class Student: 
    def __init__(self, marks): 
        self._marks = marks   # self._marks is a private attribute
                              # _ is used to make it private and thus we
                              # don't want others to do print(s1._marks)

    @property             # Thus this getter is created and now simply 
    def marks(self):      # by doing print(s1.marks), it looks like we
        return self._marks  # are accessing an attribute, but actually,
                          # it's calling a method.
s1 = Student(80)
print(s1.marks)

'''2. A getter gives us the power to customize what should be shown.'''
class Student: 
    def __init__(self, marks): 
        self._marks = marks

    @property                     
    def grade(self):
        if self._marks >= 90:
            return "A"            
        else:
            return "Keep improving!"
             

s1 = Student(80)
print(s1.grade)         

'''3. Cleaner syntax -
Instead of calling a method like: s1.get_marks()
we can do: s1.marks
It looks like variable but works like a function'''

# SETTER IS USED TO CONTROL WHAT USER ENTERS.
'''
III) Setter :
1. A setter is used to control what value is being set.'''

print("\nSETTER")

class Student: 
    def __init__(self, marks): 
        self._marks = marks

    @property
    def marks(self):             
        return self._marks                   

    @marks.setter
    def marks(self,value):
        if value<0 or value>100:
            print("Invalid marks entered! Enter marks between 0 and 100")
        else:
            self._marks = value
      
'''2. A setter gives us the power to check the value before
setting it, like if someone tries to set -100 we can stop that'''
    
'''3. Cleaner syntax - 
Instead of calling a method like s1.set_marks(90) we can simply
do: s1.marks = 90

It looks like we are setting a variable but actually, setter is
doing the work
'''
s1 = Student(88)  # Getter used here
print(s1.marks)

s1.marks = 95     # Setter used here
print(s1.marks)

s1.marks = -100

# DELETER IS USED TO CONTROL WHAT USERS CAN DELETE

print("\nDELETER")
class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if value < 0 or value > 100:
            print("Marks must be between 0 and 100")
        else:
            self._marks = value

    @marks.deleter
    def marks(self):
        print("Marks deleted!")
        del self._marks

s1 = Student(90)
print(s1.marks)     # Uses getter
del s1.marks        # Uses deleter
# print(s1.marks)     # Gives error since _marks is deleted
'''
DELETER :

1. A deleter is used to delete a private attribute of an object safely.

2. Just like we use getter and setter to access and modify private 
variables,deleter is used to control what happens when we delete it.

3. It can also be used to perform some cleanup work before deleting, 
or show a message.

Note : We use @marks.deleter (if marks is the property name)
'''


# WAP to convert temperature in celsius to fahrenheit using gette, setter
# and @property decorator

print("\n Program for example")
class Temperature:
    def __init__(self, celsius): 
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, f):
        self._celsius = (f - 32) * 5/9

# Creating object
weather = Temperature(0) 
print(f"Celsius to Fahrenheit: {weather.fahrenheit}F")

weather.fahrenheit = 98.6 
print(f"Fahrenheit to Celsius: {weather._celsius}C")

