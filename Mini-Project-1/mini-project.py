
batch = ["Python Foundation - Batch 1","Python Foundation - Batch 2", "Git Beginner Batch 1"]
course = ["Python", "Git", "Docker", "Linux"]

batch_dict = {
    course[0]:[
        {
        "Batch": batch[0],
        "start_batch": "March 2026",
        "Type": "weekday",
        "module": ("Variables","operators", "data types","OOPS", "functions")
        },
        {
        "Batch": batch[1],
        "start_batch": "July 2026",
        "Type": "weekend",
        "module": ("Variables","operators", "data types","OOPS", "functions")
        } ]     
              ,
    course[1]:[
        {
        "Batch": batch[2],
        "start_batch": "May 2026",
        "Type": "weekday",
        "module": ("merge","commit", "push","pull", "branch")
        }]
        
    }

student = {
    "name": "student_name",
    "email": "student_mail@email.com",
    "city": "pune",
    "batch": batch[1],
    "student_id": 101
}

# Student Name: student_name
# Email: student_mail@email.com
# City: Pune

# print(student.get("name"))

for keys, values in student.items():
    if keys == "name":
        print(f"Student {keys.capitalize()}: {student[keys]}")
    elif keys == "email":
        print(f"{keys.capitalize()}: {student[keys]}") 
    elif keys == "city":
        print(f"{keys.capitalize()}: {student[keys]}")    
    else:
        continue
    
    
