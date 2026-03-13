import json
import os

FILE_NAME = "students.json"


class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "grade": self.grade
        }


class StudentManager:
    def __init__(self):
        self.students = {}
        self.load_students()

    def load_students(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as f:
                data = json.load(f)
                for s in data:
                    student = Student(s["id"], s["name"], s["grade"])
                    self.students[s["id"]] = student

    def save_students(self):
        with open(FILE_NAME, "w") as f:
            json.dump([s.to_dict() for s in self.students.values()], f, indent=4)

    def add_student(self, student_id, name, grade):
        if student_id in self.students:
            print("❌ Student ID already exists!")
            return

        self.students[student_id] = Student(student_id, name, grade)
        self.save_students()
        print("✅ Student added successfully!")

    def update_student(self, student_id, name=None, grade=None):
        if student_id not in self.students:
            print("❌ Student not found!")
            return

        if name:
            self.students[student_id].name = name
        if grade:
            self.students[student_id].grade = grade

        self.save_students()
        print("✅ Student updated!")

    def delete_student(self, student_id):
        if student_id not in self.students:
            print("❌ Student not found!")
            return

        del self.students[student_id]
        self.save_students()
        print("🗑 Student deleted!")

    def list_students(self):
        if not self.students:
            print("No students found.")
            return

        print("\n--- Student List ---")
        print(f"{'ID':<10}{'Name':<20}{'Grade':<10}")
        print("-" * 40)

        for s in self.students.values():
            print(f"{s.student_id:<10}{s.name:<20}{s.grade:<10}")


def main():
    manager = StudentManager()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            sid = input("Enter ID: ")
            name = input("Enter Name: ")
            grade = input("Enter Grade: ")
            manager.add_student(sid, name, grade)

        elif choice == "2":
            sid = input("Enter ID to update: ")
            name = input("Enter new name (leave blank to skip): ")
            grade = input("Enter new grade (leave blank to skip): ")
            manager.update_student(sid, name or None, grade or None)

        elif choice == "3":
            sid = input("Enter ID to delete: ")
            manager.delete_student(sid)

        elif choice == "4":
            manager.list_students()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()