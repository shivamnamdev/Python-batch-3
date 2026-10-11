from modules.student_data import get_student_data
from modules.profile_generation import generate_profile

def main():
    # Reading the json file
    student = get_student_data()
    # Writing the profile of the student
    generate_profile(student)

if __name__ == "__main__":
    main()