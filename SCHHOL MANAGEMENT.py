class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def display_details(self):
        print(f"Name: {self.name}, Subject: {self.subject}")


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def display_details(self):
        print(f"Name: {self.name}, Teacher: {self.teacher.name}")


class SchoolManagementSystem:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self):
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")
        self.students.append(Student(name, age, grade))
        print("Student added!")

    def add_teacher(self):
        name = input("Enter teacher name: ")
        subject = input("Enter teacher subject: ")
        self.teachers.append(Teacher(name, subject))
        print("Teacher added!")

    def add_course(self):
        name = input("Enter course name: ")
        teacher_name = input("Enter teacher name: ")
        teacher = next((t for t in self.teachers if t.name == teacher_name), None)
        if teacher:
            self.courses.append(Course(name, teacher))
            print("Course added!")
        else:
            print("Teacher not found!")

    def view_students(self):
        for student in self.students:
            student.display_details()

    def view_teachers(self):
        for teacher in self.teachers:
            teacher.display_details()

    def view_courses(self):
        for course in self.courses:
            course.display_details()


def main():
    sms = SchoolManagementSystem()

    while True:
        print("\nSchool Management System")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Add Course")
        print("4. View Students")
        print("5. View Teachers")
        print("6. View Courses")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            sms.add_student()
        elif choice == "2":
            sms.add_teacher()
        elif choice == "3":
            sms.add_course()
        elif choice == "4":
            sms.view_students()
        elif choice == "5":
            sms.view_teachers()
        elif choice == "6":
            sms.view_courses()
        elif choice == "7":
            print("Thank you!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()

