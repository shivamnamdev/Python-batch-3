import json

# # Data write
# # json.dumps()	Serializes a Python object into a JSON format string.	In-memory string
# # json.dump()	Serializes a Python object and writes it to a file.	File stream

# # Data read
# # json.loads()	Deserializes a JSON format string into a Python object.	In-memory string
# # json.load()	Reads a JSON file and deserializes it into a Python object.	File stream

def get_student_data(file="student.json"):
    try:
        file = open(file,'r')
        student = json.load(file)
        print(student)
        return student
    except FileNotFoundError:
        print("Student JSON file is not found")    
    # finally:
    #     file.close()    

if __name__ == "__main__":
    get_student_data("../student.json")
