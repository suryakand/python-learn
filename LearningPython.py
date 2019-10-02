
# Example of import
import modules.utils as utils
utils.public_function('Surya')
utils._private_function('Surya')

# Example of wildcard import
from modules.utils import *
public_function('Surya')
#_private_function('Surya') <--- This will not work because wildcard import (i.e. import * ) will not import functions starting with _


# Example of class
class Employee():
    # Names that have both leading and trailing double underscores are reserved for special use in the language. 
    # This rule covers things like __init__ for object constructors, or __call__ to make an object callable.
    def __init__(self, name, age): # self should be first argument
        self.name = name
        self._age = age
        self.greeting = self._greenting()
        self.__designation = 'EMP'
    
    def _greenting(self): # variable and function name starting with _ are meant (not mandatrory) for internal use
        return 'Hello {}! Your current age is {}.'.format(self.name, self._age)
    
    def biography(self, class_): # a single trailing underscore (postfix) is used by convention to avoid naming conflicts with Python keywords
        return 'This {} is {}\'s biography'.format(class_, self.name)


emp =  Employee('Surya', 35)

print(emp.greeting)
print(emp.biography('Biography text'))
print('Hello {}!'.format(emp.name))

# Extending Class
class Director(Employee):
    def __init__(self, designation, salary):
        # A double underscore prefix causes the Python interpreter to rewrite the attribute 
        # name in order to avoid naming conflicts in subclasses.
        self.__designation = ('DIR', designation)[len(designation) > 1] 

    def __roles(self):
        return ['Management', 'Sales']
    
    def print_roles(self):
        # Besides its use as a temporary variable, “_” is a special 
        # variable in most Python REPLs that represents the result of the last expression evaluated by the interpreter.
        for _ in self.__roles(): 
            print( _ )
            _ + ' Modified'
            print( _ ) # Demo: print last evaludated expression using _


d = Director('', 10)

print(dir(d)) # dir() prints the class structure
print(d._Director__designation) # Access mangled (__) attributes
print(d._Director__roles()) # Access mangled (__) functions 
d.print_roles()

