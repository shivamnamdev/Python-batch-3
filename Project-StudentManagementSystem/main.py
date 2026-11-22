from services.student_manager import StudentManager
from utils.helpers import print_menu, get_int_input

def main():
    manager = StudentManager()
    while True:
        print_menu()
        choice = get_int_input("Enter choice: ")
        if choice == 1: manager.add_student()
        elif choice == 2: manager.view_students()
        elif choice == 3: manager.search_student()
        elif choice == 4: manager.update_student()
        elif choice == 5: manager.delete_student()
        elif choice == 6: manager.student_report()
        elif choice == 7:
            print("Goodbye!")
            break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
