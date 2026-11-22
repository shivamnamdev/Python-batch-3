def print_menu():
    print("\n" + "=" * 40)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Report")
    print("7. Exit")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a valid integer.")

def get_text_input(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("This cannot be blank.")
