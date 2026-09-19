# ==========================================
# PYTHON FILE HANDLING – SOLUTIONS
# ==========================================

# ------------------------------------------
# Q1. Create a file and write student names

file = open("students.txt", "w")

file.write("Rahul\n")
file.write("Shivam\n")
file.write("Aman\n")
file.write("Priya\n")
file.write("Neha\n")

file.close()

print("Student names written successfully")

# ------------------------------------------
# Q2. Read entire file content

file = open("students.txt", "r")

content = file.read()

print(content)

file.close()

# ------------------------------------------
# Q3. Append new student name

file = open("students.txt", "a")

file.write("Rohit\n")

file.close()

print("New student name appended successfully")

# ------------------------------------------
# Q4. Count total number of characters

file = open("sample.txt", "r")

content = file.read()

print("Total characters:", len(content))

file.close()

# ------------------------------------------
# Q5. Demonstrate tell()

file = open("sample.txt", "r")

print("Initial cursor position:", file.tell())

file.read(5)

print("Cursor position after reading:", file.tell())

file.close()

# ------------------------------------------
# Q6. Demonstrate seek()

file = open("sample.txt", "r")

print(file.read(5))

file.seek(0)

print(file.read())

file.close()

# ==========================================
# KEY LEARNINGS
# ==========================================

# 'w'  --> write mode
#         Creates new file
#         Removes old data

# 'r'  --> read mode
#         Reads file content

# 'a'  --> append mode
#         Adds new data
#         Keeps old data safe

# read() --> reads entire file

# tell() --> gives current cursor position

# seek(0) --> moves cursor to beginning

# Always close files after use.
# ==========================================