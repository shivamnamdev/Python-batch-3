from modules.student_data import get_student_data
from modules.profile_generation import generate_profile

def main():
    # Reading the json file
    student = get_student_data() #getter functions
    # Writing the profile of the student
    generate_profile(student) # setter functions

if __name__ == "__main__":
    main()