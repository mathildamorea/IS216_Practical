# CAPSTONE APPLICATION
# Student Management System

from functools import reduce


class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def display_student(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}"


class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name

    def display_course(self):
        return f"{self.course_code} - {self.course_name}"


class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course

    def display_enrollment(self):
        return f"{self.student.name} enrolled in {self.course.course_name}"


class Grade:
    def __init__(self, student, mark):
        self.student = student
        self.mark = mark

    def get_grade(self):
        if self.mark >= 80:
            return "A"
        elif self.mark >= 70:
            return "B"
        elif self.mark >= 60:
            return "C"
        elif self.mark >= 50:
            return "D"
        else:
            return "F"


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.enrollments = []
        self.grades = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def enroll_student(self, enrollment):
        self.enrollments.append(enrollment)

    def add_grade(self, grade):
        self.grades.append(grade)

    def list_students(self):
        for student in self.students:
            print(student.display_student())

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def sort_students_by_name(self):
        return sorted(self.students, key=lambda student: student.name)

    def show_grades(self):
        for grade in self.grades:
            print(f"{grade.student.name}: {grade.mark} - Grade {grade.get_grade()}")

    def calculate_average_mark(self):
        marks = list(map(lambda grade: grade.mark, self.grades))
        total = reduce(lambda a, b: a + b, marks)
        return total / len(marks)


# Main Program

try:
    system = StudentManagementSystem()

    # Create students
    student1 = Student(1, "John", 20)
    student2 = Student(2, "Alice", 21)
    student3 = Student(3, "Peter", 19)

    # Create courses
    course1 = Course("IS216", "Introduction to Programming")
    course2 = Course("IS214", "Data Communications")

    # Add students
    system.add_student(student1)
    system.add_student(student2)
    system.add_student(student3)

    # Add courses
    system.add_course(course1)
    system.add_course(course2)

    # Enroll students
    system.enroll_student(Enrollment(student1, course1))
    system.enroll_student(Enrollment(student2, course1))
    system.enroll_student(Enrollment(student3, course2))

    # Add grades
    system.add_grade(Grade(student1, 85))
    system.add_grade(Grade(student2, 72))
    system.add_grade(Grade(student3, 59))

    print("All Students")
    system.list_students()

    print("\nSearch Student")
    found_student = system.search_student(2)

    if found_student:
        print(found_student.display_student())
    else:
        print("Student not found")

    print("\nSorted Students")
    sorted_students = system.sort_students_by_name()

    for student in sorted_students:
        print(student.display_student())

    print("\nEnrollments")
    for enrollment in system.enrollments:
        print(enrollment.display_enrollment())

    print("\nGrades")
    system.show_grades()

    print("\nAverage Mark")
    print(system.calculate_average_mark())

except ZeroDivisionError:
    print("Error: No grades available to calculate average.")

except Exception as error:
    print("An error occurred:", error)