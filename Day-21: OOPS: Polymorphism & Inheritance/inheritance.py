# Inheritance: One class can use properties(Variable, and functions) of another class.
# Class Properties: Variables, Functions, Constructor
# Purpose: To reuse data and functions without implementing again and again

class Parent:
    name = "Testing"
    
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print("This is the parent class")
        
        
class Child(Parent):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def study(self):
        print("This is child's study function")
        
    def show(self):
        super().show()
        print("This is the child class")    

c = Child("Amitabh Bacchan", 60)
c.show()     
print(c.name) 
c.study()

p = Parent("Jaya Bacchan")
p.show()
# p.study() AttributeError: 'Parent' object has no attribute 'study'


# Types of Inheritance:
# Single: Parent -> Child
# Multi-level: Grandparent -> Parent -> Child
# Multiple: When Child has more than 1 Parent
# Heirarichal: When Parent has more than 1 Child
# Hybrid: Diamond shape inheritance - Start with Heirarichal and ends with Multiple inheritance

# Benefit:
# Reduce the code duplicacy -> Code reusability
# Access the Broader Functions
# Easy Maintance( Using the exiting code)
# Real-World Modeling
# Cleaner Structure

# Parent -> Base Functionality
# Child -> Specific Functionality

# Multi-Level Inheritance
class GrandDog:
    def eat(self):
        print("Animal eats")
        
class Dog(GrandDog):
    def bark(self):
        print("Dog Barks")
        
class Puppy(Dog):
    def weep(self):
       print("puppy weeps")                 
       
       
p = Puppy()
p.eat()
p.bark()
p.weep()       


# Multiple Inheritance
class Father:
    def skills(self):
        print(__class__)
        print("Good with Cooking")
        
class Mother:
    def skills(self):
        print(__class__)
        print("Good Communication Skills")
        
class Child(Mother, Father):
    def skills(self):
        super().skills()
        print(__class__)
        print("Programmer")  
        
        
c = Child()
c.skills()       


# Heirarichal Inheritance

class Animal:
    def eat(self):
        print("Animal eats")
        
class Dog(Animal):
    def bark(self):
        print("Dog Barks")
        
class Cat(Animal):
    def meow(self):
       print("Cat Meows") 
       
c = Cat()
d = Dog()

c.eat()
d.eat()   
c.meow()
d.bark()