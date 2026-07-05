"""
Campus Connect - Core Domain Model
Module 3: Core Programming Foundations
"""

class Student:
    def __init__(self, student_id, name, department, year):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.year = year

    def __repr__(self):
        return f"Student({self.student_id}, {self.name}, {self.department}, Y{self.year})"


class Event:
    def __init__(self, event_id, title, date, department):
        self.event_id = event_id
        self.title = title
        self.date = date
        self.department = department

    def __repr__(self):
        return f"Event({self.event_id}, {self.title}, {self.date})"


class DirectoryManager:
    def __init__(self):
        self.students = []
        self.events = []

    def add_student(self, student_id, name, department, year):
        if self.find_student(student_id) is not None:
            raise ValueError(f"Student ID {student_id} already exists.")
        if not name.strip():
            raise ValueError("Student name cannot be empty.")
        student = Student(student_id, name, department, year)
        self.students.append(student)
        return student

    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def remove_student(self, student_id):
        student = self.find_student(student_id)
        if student is None:
            raise ValueError(f"No student with ID {student_id} found.")
        self.students.remove(student)
        return True

    def list_students(self):
        return list(self.students)

    def add_event(self, event_id, title, date, department):
        event = Event(event_id, title, date, department)
        self.events.append(event)
        return event

    def list_events(self):
        return list(self.events)


if __name__ == "__main__":
    dm = DirectoryManager()
    dm.add_student("S101", "Ravi Kumar", "CSE", 2)
    dm.add_student("S102", "Priya Singh", "ECE", 3)
    dm.add_event("E01", "Hackathon 2026", "2026-08-10", "CSE")

    print(dm.list_students())
    print(dm.list_events())

    try:
        dm.add_student("S101", "Duplicate", "CSE", 1)
    except ValueError as e:
        print("Caught expected error:", e)