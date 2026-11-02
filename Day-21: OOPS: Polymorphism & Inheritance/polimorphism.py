# Polymorphism:
# - Method Overriding - supported in python - implementing the new functionality over the old one
# - Method Overloading - not supported in python - keeping different functionality under the same name but different arguements

class TestingPolymorphism:
    
    def polyfunction(self):
        print("The first function")
        
    def polyfunction(self, a, b):
        print("The second function")
        
    def polyfunction(self, a: int, b: int, c: int):
        print("The third function") 
        
    def polyfunction(self, a: str, b: str, c: str):
        print("The forth function")     
        
            
        

t = TestingPolymorphism()
# t.polyfunction(2,3)   TypeError: polyfunction() missing 1 required positional argument: 'c'
#  ----> polyfunction(t)
t.polyfunction(3,4,5)
t.polyfunction("a","b","c")



# Work Around
class multivalue:
    
    # def calc(self, a, b):
    #     return a + b
    
    def calc(self, a=8, b=4, c=9):
        print( a + b + c)
    

m = multivalue()
m.calc(2,3,4)
# m.calc(5,3)    TypeError: calc() missing 1 required positional argument: 'c'
m.calc(5,3)
m.calc(1)
m.calc()

class args:
    def calc(self, *numbers):
        sum = 0
        for i in numbers:
            sum += i
        print(sum)    
            
a = args()
a.calc(2,3,4)
a.calc(5,3)
a.calc(1)
            
# Utilization of polymorphism with multiple classes having same name of the function
            
class Student:
    def show(self):
        print("I am a student")
        
class Teacher:   
    def show(self):
        print("I am a teacher") 
        
        
school_object_init = [Student(), Teacher()]

for sod in school_object_init:
    sod.show()                      