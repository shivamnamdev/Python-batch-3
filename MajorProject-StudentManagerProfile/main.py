from model.student import graduate_student, post_student
  
    
class Student_manager:
    
    id = 101
    
    def add_student(self):  
        print("Add Student")
        self.name = input("Enter student's name: ")
        self.email = input("Enter student's email: ")
        self.age = int(input("Enter Student's age: "))
        self.course = input("Enter which course is in student: ")
        self.student_id = Student_manager.id
        Student_manager.id += 1
        self.marks = int(input("Enter progress marks: "))
        kind = input("Is student from graduate or post graduate class: ")
        if kind == "graduate":
            student_class = graduate_student
        else:
            student_class = post_student
        
        student = student_class(
          self.id, self.name, self.age, self.course, self.email, self.marks  
        )
        print("Student successfully added")
            
    def view_student(self):
        pass
    
    def search_student(self):
        pass
    
    def update_student(self):
        pass
    
    def delete_student(self):
        pass  
    
    
    
    
# from modules.student_data import get_student_data
# from modules.profile_generation import generate_profile


def print_menu():
    print("   Student Management System    ")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit") 


def main():
    # # Reading the json file
    # student = get_student_data() #getter functions
    # # Writing the profile of the student
    # generate_profile(student) # setter functions
    manager = Student_manager()
    while True:
        print_menu()
        choice = int(input("Enter your choice="))
        if choice == 1:
            manager.add_student()
        elif choice == 2:
            manager.view_student()  
        elif choice == 3:
            manager.search_student()
        elif choice == 4:
            manager.update_student()            
        elif choice == 5:
            manager.delete_student()
        elif choice == 6:
            break
        else: 
            print("Invalid choice, Please choose from below options")   

if __name__ == "__main__":
    main()    