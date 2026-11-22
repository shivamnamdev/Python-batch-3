class Student:
    """Base class: data and behaviour common to every student."""

    # ---- Class variables (shared by ALL Student objects) ----
    institute_name = "Think in Python Academy"
    total_students = 0

    def __init__(self, student_id, name, age, course, marks=0):   # Constructor
        # ---- Instance variables (each object has its own copy) ----
        self.student_id = student_id     # + public
        self.name = name                 # + public
        self.age = age                   # + public
        self.course = course             # + public
        self.__marks = 0                 # - private (name-mangled to _Student__marks)
        self.update_details(age=age, marks=marks)   # validate initial values

        Student.total_students += 1

    # ---- Controlled access to the private attribute ----
    def get_marks(self):
        return self.__marks

    # ---- Methods from the design ----
    def calculate_grade(self):
        marks = self.__marks             # Local variable (exists only inside this call)
        if marks >= 90:
            return "A"
        if marks >= 80:
            return "B"
        if marks >= 70:
            return "C"
        if marks >= 60:
            return "D"
        return "Needs Improvement"

    def update_details(self, name=None, age=None, course=None, marks=None):
        """Update any field passed in; leave fields given as None unchanged.

        Every value is checked before anything changes, so a bad value
        leaves the object untouched.
        """
        if name is not None and not name.strip():
            raise ValueError("Name cannot be empty.")
        if age is not None and age <= 0:
            raise ValueError("Age must be positive.")
        if course is not None and not course.strip():
            raise ValueError("Course cannot be empty.")
        if marks is not None and not 0 <= marks <= 100:
            raise ValueError("Marks must be from 0 to 100.")

        if name is not None:
            self.name = name.strip()
        if age is not None:
            self.age = age
        if course is not None:
            self.course = course.strip()
        if marks is not None:
            self.__marks = marks         # only the class itself writes the private field

    def display_details(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Age: {self.age}")
        print(f"Course: {self.course} | Marks: {self.__marks}/100 | Grade: {self.calculate_grade()}")
        print(f"Institute: {Student.institute_name}")

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.__marks,
            "student_type": type(self).__name__,
        }


class RegularStudent(Student):
    """Inherits everything from Student; overrides fee and display."""

    def calculate_fee(self):
        return 5000

    def display_details(self):                    # Method overriding (polymorphism)
        super().display_details()                 # reuse the parent's output
        print(f"Plan: Regular | Fee: ₹{self.calculate_fee():,.2f}")


class PremiumStudent(Student):
    """Same interface as RegularStudent, different behaviour."""

    MENTOR_SESSIONS = 4                           # Class variable specific to this subclass

    def calculate_fee(self):
        return 12000

    def display_details(self):                    # Method overriding (polymorphism)
        super().display_details()
        print(f"Plan: Premium | Fee: ₹{self.calculate_fee():,.2f} "
              f"| Mentor sessions: {PremiumStudent.MENTOR_SESSIONS}/month")
