# OOPS Concept: Object Oriented Programming Language
    # Class - Like a Blueprint - Encapsulate data(variable) and behaviour(method)
    # Objects - is an instance of a class, hold real values in the memory
    # Constructor - job is to initialise the values
    # Inheritance
    # Polymorphisms - Same name but different functionality
    # Encapsulation
    # Abstraction 
    
    
class student:
    name = "unknown"
    age = 25
  
    def __init__(self,name,age): # constructor
        self.name = name
        self.age = age

    def update_age(self, age): # method 
        self.age = age

    def print_values(self): 
        print(self.name, "has", self.age, "age, so he is eligible now") 
           
    # def add_student(my,name,age): # method
    #     print(student.name)
    #     print(student.age)
    #     print(my)
    #     name = name[:3]
    #     my.name = name
    #     my.age = age
    #     my.id = name+str(age)
    

s1 = student("Vipul",29)
s2 = student("Poornima", 25)
print(s1)
# s1.add_student("Vipul",29)
# ----> add_student(s1,"Vipul",29)
# s2.add_student("Poornima") --> TypeError: add_student() missing 1 
# required positional argument: 'age'
# ----> add_student(s2,"Poornima")

print(s1.name)
print(s1.age)

print(s2.name)
print(s2.age)

s1.update_age(30)
s1.print_values()
s2.print_values()