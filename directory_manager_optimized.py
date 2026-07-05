import time
from directory_manager import Student, Event


class OptimizedDirectoryManager:
    def __init__(self):
        self.students_by_id = {}
        self.events = []

    def add_student(self, student_id, name, department, year):
        if student_id in self.students_by_id:
            raise ValueError(f"Student ID {student_id} already exists.")
        self.students_by_id[student_id] = Student(student_id, name, department, year)

    def find_student(self, student_id):
        return self.students_by_id.get(student_id)

    def list_students(self):
        return list(self.students_by_id.values())

    def add_event(self, event_id, title, date, department):
        self.events.append(Event(event_id, title, date, department))
        self.events.sort(key=lambda e: e.date)

    def find_events_on_date(self, target_date):
        lo, hi = 0, len(self.events) - 1
        results = []
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.events[mid].date == target_date:
                i = mid
                while i >= 0 and self.events[i].date == target_date:
                    results.append(self.events[i])
                    i -= 1
                i = mid + 1
                while i < len(self.events) and self.events[i].date == target_date:
                    results.append(self.events[i])
                    i += 1
                break
            elif self.events[mid].date < target_date:
                lo = mid + 1
            else:
                hi = mid - 1
        return results


def demo_speed_difference():
    from directory_manager import DirectoryManager

    linear = DirectoryManager()
    optimized = OptimizedDirectoryManager()

    for i in range(50000):
        sid = f"S{i}"
        linear.students.append(Student(sid, f"Name{i}", "CSE", 1))
        optimized.students_by_id[sid] = Student(sid, f"Name{i}", "CSE", 1)

    target = "S49999"

    start = time.perf_counter()
    linear.find_student(target)
    linear_time = time.perf_counter() - start

    start = time.perf_counter()
    optimized.find_student(target)
    optimized_time = time.perf_counter() - start

    print(f"Linear search (checking one by one):  {linear_time*1000:.4f} ms")
    print(f"Dictionary lookup (filing cabinet):   {optimized_time*1000:.4f} ms")
    print(f"Speedup: ~{linear_time/optimized_time:.0f}x faster")


if __name__ == "__main__":
    demo_speed_difference()

    odm = OptimizedDirectoryManager()
    odm.add_event("E01", "Hackathon", "2026-08-10", "CSE")
    odm.add_event("E02", "Robotics Fair", "2026-08-05", "ECE")
    odm.add_event("E03", "AI Workshop", "2026-08-10", "CSE")
    print(odm.find_events_on_date("2026-08-10"))