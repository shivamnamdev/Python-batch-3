

y = 10 # -> Global Variable
class Student:
    school_name = "SchoolName" # -> Class Variable
    def show(self,z): # -> Parameter/Local Variable
        print(y)
        self.name = z
        print(self.name) # -> Instance Variable
        

v1 = Student()
v1.show("Vipul")
v2 = Student()
v2.show("Poornima")
print(v1.school_name)
print(Student.school_name) # Class Variable use with class name