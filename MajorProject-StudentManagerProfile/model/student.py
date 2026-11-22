from abc import ABC, abstractmethod

class Student(ABC):
    total_student = 0
    institute_name = "TechMastery Institute"
    
    def __init__(self, student_id=0, name="", age=0, course="", email="@gmail.com", progress=0):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.__progress = progress
        self.__email = email
        
        Student.total_student += 1
        
    
    @abstractmethod
    def display_detail(self):
        print(f"ID:")
        print(f"Name:")
        print(f"Age:")
    
    @abstractmethod
    def update_detail(self, name):
        self.name = name
    
    @abstractmethod
    def calculate_fees(self):
        self.base_fees = 50000
    
class graduate_student(Student):
    skill = ["Java", "Data Structure"]
    graduate_addon = 30000
    def display_detail(self):
        print(f"ID:",self.student_id)
        print(f"Name:", self.name)
        print(f"Age:", self.age)
    
    def update_detail(self, name):
        self.name = name
    
    def calculate_fees(self):
        self.base_fees = self.base_fees + graduate_student.graduate_addon
    
    def display_skills(self):
        print(graduate_student.skill)
    
    
class post_student(Student):
    skill = ["Python"]
    postgrad_addon = 40000
    def display_detail(self):
        print(f"ID:",self.student_id)
        print(f"Name:", self.name)
        print(f"Age:", self.age)
    
    def update_detail(self, name):
        self.name = name
    
    def calculate_fees(self):
        self.base_fees = self.base_fees + post_student.graduate_addon    
    
    def display_skills(self):
        print(post_student.skill)
    
      