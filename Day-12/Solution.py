# ==========================================
# LIST Scenario – SOLUTIONS
# ==========================================
# ------------------------------------------

marks = [45, 78, 32, 90, 67]

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

passed_students = 0

for mark in marks:
    if mark >= 40:
        passed_students += 1

print("Total marks:", total)
print("Average marks:", average)
print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Number of students:", len(marks))
print("Passed students:", passed_students)

# ------------------------------------------

cart = ["Laptop", "Mouse", "Keyboard"]

choice = input("What do you want to do? add/remove/search/view: ").lower()

if choice == "add":
    product = input("Enter product name: ")
    cart.append(product)
    print("Product added")

elif choice == "remove":
    product = input("Enter product name: ")

    if product in cart:
        cart.remove(product)
        print("Product removed")
    else:
        print("Product not found")

elif choice == "search":
    product = input("Enter product name: ")

    if product in cart:
        print("Product exists")
    else:
        print("Product does not exist")

elif choice == "view":
    print(cart)

print("Total products:", len(cart))

# ------------------------------------------

numbers = [10, 20, 30, 20, 40, 10, 50]

duplicates = []

for number in numbers:
    if numbers.count(number) > 1:
        if number not in duplicates:
            duplicates.append(number)

print("Duplicate values:", duplicates)

# ------------------------------------------

attendance = ["P", "A", "P", "P", "A", "P"]

present = attendance.count("P")
absent = attendance.count("A")

percentage = (present / len(attendance)) * 100

print("Present:", present)
print("Absent:", absent)
print("Attendance percentage:", percentage)

if percentage >= 75:
    print("Attendance is acceptable")
else:
    print("Attendance is not acceptable")

# ------------------------------------------

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

search = input("Enter product to search: ").lower()

found = False

for index in range(len(products)):
    if products[index].lower() == search:
        print("Product found")
        print("Product position:", index)
        found = True

if not found:
    print("Product not found")

# ------------------------------------------

numbers = [10, 15, 22, 31, 40, 55, 60]

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# ------------------------------------------

numbers = [1, 2, 2, 3, 4, 4, 5, 1]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)

# ------------------------------------------

password_history = [
    "Password@123",
    "Hello@123",
    "Python@123"
]

new_password = input("Enter new password: ")

if new_password in password_history:
    print("You have already used this password")
else:
    password_history.append(new_password)
    print("Password accepted")

print(password_history)

# ------------------------------------------

marks = [95, 82, 71, 65, 48, 30]

grades = []

for mark in marks:
    if mark >= 90:
        grades.append("A")
    elif mark >= 75:
        grades.append("B")
    elif mark >= 50:
        grades.append("C")
    else:
        grades.append("Fail")

print(grades)

# ------------------------------------------

data = [10, "Python", 20.5, True, "Hello", False, 100]

integers = []
strings = []
floats = []
booleans = []

for value in data:

    if type(value) == bool:
        booleans.append(value)

    elif type(value) == int:
        integers.append(value)

    elif type(value) == str:
        strings.append(value)

    elif type(value) == float:
        floats.append(value)

print("Integers:", integers)
print("Strings:", strings)
print("Floats:", floats)
print("Booleans:", booleans)