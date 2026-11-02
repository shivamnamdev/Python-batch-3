# Access Specifier:
# 1. Public - Can be used within or outside the class without specifying anything
# 2. Private - Can only be used within Class - need to start with __ (double underscore in the beginning)
#  (__variable, __method())
# 3. Protected - It is public in nature + private in representation - It is a convention not a rule
#  (_variable, _method())

class Student:
    
    def __init__(self, name, age, address):
        self.name = name # Public Variable
        self.__age = age # Private Variable
        self._address = address # Protected Variable
        
    def __private_function(self):    # Private Function
        print("This is my private_function")    
        
    def _protected_function(self):
        print("This is my protected function")    
        
    def show(self):
        print(f"My name is {self.name} and my age is {self.__age}")   
        self.__private_function() 
        
    
class ChildClass(Student):
    
    _ChildClass__age = 45
    
    def _ChildClass__private_function(self):
        print("working")
        
    def child_jump_method(self):
        print(self.__age)
        print(self._address)
        self._protected_function()
        self.__private_function()     
        self.show()

# s1 = Student("Vipul", 28, "Indore")
# print(s1.name, s1._address) 
# # s1.__private_function() private method calling
# s1.show()
# s1._protected_function()

c1 = ChildClass("Poornima", 29, "Pune")
c1.child_jump_method()