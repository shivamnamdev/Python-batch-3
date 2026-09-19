# File Handling covers:
# file create
# file edit
# file execute
# file read

# Primary vs Secondary memory
# RAM -> Primary memory -> Temporary memory -> Volatile memory
# HDD/SSD -> Secondary memory -> Permanent memory -> Non-volatile memory


# Data Structures -> so far we have covered are nothing but for primary memory. If we want to store data permanently we need to use secondary memory.   
# File -> A file is a collection of data stored in secondary memory. It can be a text file, image file, video file, etc. Files are used to store data permanently so that it can be accessed later.


# File is a container that stores the data permanently.
# Example: data.txt, data.csv, data.json, data.xml, data.html, data.pdf, data.docx, data.xlsx, data.pptx, data.mp3, data.mp4, data.avi, data.mkv, data.jpg, data.png, data.gif

# Life cycle of a file:
# Open a file
# Perform operation(Read/write/append)
# Close the file

# Operations on file: -> mode
# (Read, Write, Append, Execute)

# Read                  Write(write, append, execute) 

# Example 1: Read a file
var = open("Testing.txt","r") #  Open a file
print(var.read()) # Perform operation(Read/write/append)
# var.write("new content") io.UnsupportedOperation: not writable
var.close() # Close the file
# var.read()  ValueError: I/O operation on closed file.

# Example 2: Write a file
file = open("Writing_file.txt","w") #  Open a file
file.write("This is my new file")
# file.read() io.UnsupportedOperation: not readable
file.close() # Close the file

# Example 3: Existed file - Read/Write 

# var = open("Testing_non_existent.txt","r") FileNotFoundError: [Errno 2] No such file or directory: 'Testing_non_existent.txt'
file = open("Writing_file.txt","w") #  Open a file
file.write("Updated the content")
file.close() # Close the file

# Standard input -> input() -> stdin -> keyboard(cmdline)
# Standard output -> print() -> stdout -> console(cmdline)

# Example 4: Append a file
file = open("Writing_file.txt","a") #  Open a file
file.write("\nThis is my updated file")
file.close() # Close the file
# what if file not exist? -> it will create a new file and append the content to it.
file = open("Writing_file2.txt","a") #  Open a file
file.write("\nThis is my updated file")
# file.read() io.UnsupportedOperation: not readable
file.close() # Close the file


# Example 5: Execute a file
# file = open("Writing_file_execute.txt","x") #  Open a file
# file.write("This is my new file using execute mode")

# file.close() # Close the file

# r+ -> Read and Write
# w+ -> Write and Read
# a+ -> Append and Read

# ‘r’	Read-only. Raises I/O error if file doesn't exist.
# ‘r+’	Read and write. Raises I/O error if the file does not exist.
# ‘w’	Write-only. Overwrites file if it exists, else creates a new one.
# ‘w+’	Read and write. Overwrites file or creates new one.
# ‘a’	Append-only. Adds data to end. Creates file if it doesn't exist.
# ‘a+’	Read and append. Pointer at end. Creates file if it doesn't exist.


file = open("Writing_file.txt","a+") 
file.seek(0)
print(file.read())
file.write("\nThis is the file which opens with write and read mode. Updated the content")
# print(file.tell())
# file.seek(0)
# print(file.tell())
# file.seek(2)
# print(file.tell())
