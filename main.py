class Student:
    def __init__(self, sid, name):
        self.sid   = sid
        self.name  = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def average(self):
        return sum(self.grades.values()) / len(self.grades) if self.grades else 0

    def __str__(self):
        return f"[{self.sid}] {self.name} | O'rtacha: {self.average():.1f}"


class StudentManager:
    def __init__(self):
        self._students = {}

    def add(self, sid, name):
        if sid in self._students:
            raise ValueError(f"ID {sid} allaqachon bor.")
        self._students[sid] = Student(sid, name)

    def get(self, sid):
        return self._students.get(sid)

    def remove(self, sid):
        self._students.pop(sid, None)

    def top(self, n=3):
        return sorted(self._students.values(),
                      key=lambda s: s.average(), reverse=True)[:n]

    def search(self, name):
        return [s for s in self._students.values()
                if name.lower() in s.name.lower()]

    def report(self):
        print(f"\n{'='*40}")
        print(f"  Jami talabalar: {len(self._students)}")
        print(f"{'='*40}")
        for s in self._students.values():
            print(" ", s)

if __name__ == "__main__":
    mgr = StudentManager()
    mgr.add(1, "Ali Valiyev")
    mgr.add(2, "Vali Karimov")
    mgr.add(3, "Soli Rahimov")

    mgr.get(1).add_grade("Matematika", 90)
    mgr.get(1).add_grade("Python", 88)
    mgr.get(2).add_grade("Matematika", 72)
    mgr.get(2).add_grade("Python", 65)
    mgr.get(3).add_grade("Matematika", 95)
    mgr.get(3).add_grade("Python", 97)

    mgr.report()

    print("\nTop 2:")
    for s in mgr.top(2):
        print(" ", s)

    print("\nQidiruv 'ali':", [str(s) for s in mgr.search("ali")])
