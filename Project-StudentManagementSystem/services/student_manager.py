import json
from pathlib import Path
from models.student import Student, RegularStudent, PremiumStudent
from utils.helpers import get_int_input, get_text_input

DATA_FILE = Path(__file__).resolve().parent.parent / "students.json"


class StudentManager:
    """Manages a collection of Student objects (StudentManager --> Student)."""

    STUDENT_TYPES = {"RegularStudent": RegularStudent, "PremiumStudent": PremiumStudent}

    def __init__(self, data_file=DATA_FILE):
        self.data_file = Path(data_file)
        self.students = {}               # {student_id: Student}
        self.next_id = 1
        self.load_students()

    # ---------- persistence ----------
    def load_students(self):
        try:
            with self.data_file.open("r", encoding="utf-8") as file:
                records = json.load(file)
            if not isinstance(records, list):
                raise ValueError(f"Expected a list in {self.data_file.name}")
            for record in records:
                student = self._from_record(record)
                self.students[student.student_id] = student
            if self.students:
                self.next_id = max(self.students) + 1
        except FileNotFoundError:
            print("No saved file found; starting empty.")
        except (json.JSONDecodeError, ValueError, KeyError, TypeError) as error:
            print(f"Could not load records: {error}")

    def _from_record(self, record):
        cls = self.STUDENT_TYPES.get(record.get("student_type"), RegularStudent)
        return cls(int(record["student_id"]), str(record["name"]), int(record["age"]),
                   str(record["course"]), int(record.get("marks", 0)))

    def save_students(self):
        try:
            with self.data_file.open("w", encoding="utf-8") as file:
                json.dump([s.to_dict() for s in self.students.values()], file, indent=4)
        except OSError as error:
            print(f"Save failed: {error}")

    # ---------- methods from the design ----------
    def add_student(self):
        print("\n-- Add Student --")
        name = get_text_input("Name: ")
        age = get_int_input("Age: ")
        course = get_text_input("Course: ")
        marks = get_int_input("Marks (0-100): ")
        kind = get_int_input("Type: 1 Regular, 2 Premium: ")
        cls = PremiumStudent if kind == 2 else RegularStudent
        try:
            student = cls(self.next_id, name, age, course, marks)   # validated in Student
        except ValueError as error:
            print(f"Not added: {error}")
            return
        self.students[student.student_id] = student
        self.next_id += 1
        self.save_students()
        print(f"Added {type(student).__name__}. ID = {student.student_id}")

    def view_students(self):
        if not self.students:
            print("No students yet.")
            return
        for student in self.students.values():
            print("-" * 40)
            student.display_details()    # Polymorphism: Regular/Premium version runs

    def search_student(self):
        sid = get_int_input("Student ID: ")
        student = self.students.get(sid)
        if student:
            student.display_details()
        else:
            print("Student not found.")

    def update_student(self):
        sid = get_int_input("Student ID to update: ")
        student = self.students.get(sid)
        if not student:
            print("Student not found.")
            return
        print("Press Enter to keep existing value.")
        name = input(f"Name [{student.name}]: ").strip() or None
        age_text = input(f"Age [{student.age}]: ").strip()
        course = input(f"Course [{student.course}]: ").strip() or None
        marks_text = input(f"Marks [{student.get_marks()}]: ").strip()
        try:
            age = int(age_text) if age_text else None
            marks = int(marks_text) if marks_text else None
            student.update_details(name=name, age=age, course=course, marks=marks)
        except ValueError as error:
            print(f"Not updated: {error}")
            return
        self.save_students()
        print("Updated.")

    def delete_student(self):
        sid = get_int_input("Student ID to delete: ")
        student = self.students.pop(sid, None)
        if not student:
            print("Student not found.")
            return
        Student.total_students = max(0, Student.total_students - 1)
        self.save_students()
        print(f"Removed {student.name}.")

    # ---------- extra (not in the diagram) ----------
    def student_report(self):
        if not self.students:
            print("No records for report.")
            return
        students = list(self.students.values())
        total = len(students)
        premium = sum(isinstance(s, PremiumStudent) for s in students)
        average = sum(s.get_marks() for s in students) / total
        revenue = sum(s.calculate_fee() for s in students)          # Polymorphism
        print(f"Total: {total} | Regular: {total - premium} | Premium: {premium}")
        print(f"Average marks: {average:.2f} | Fee total: ₹{revenue:,.2f}")
        print(f"Class counter (Student.total_students): {Student.total_students}")
