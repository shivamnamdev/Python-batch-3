# import utilities

def generate_profile(student):
    # print(student)
    try:
        profile = (
        f"\n========== STUDENT PROFILE ==========\n"
        f"Name       : {student['name']}\n"
        f"Email      : {student['email']}\n"
        f"Batch      : {student['batch']}\n"
        f"Location   : {student['location']}\n"
        # f"\nEnrolled Courses:\n" + "".join([f"- {c}\n" for c in enrolled_courses]) +
        # f"\nCompleted Skills:\n" + "".join([f"- {skill}\n" for skill in completed_skills]) +
        # f"\nTotal Skills       : {total_skills}\n"
        # f"Completed Skills   : {completed_count}\n"
        # f"Progress           : {progress:.2f}%\n"
        f"\nAttendance: Regular\n"
        f"Status             : In Progress\n"
        f"======================================"
        )
        file = open("student_profile.txt",'w')
        file.write(profile)
    except KeyError as e:
        print("Missing field in the data: ",e) 
        
if __name__ == "__main__":
    generate_profile()           
