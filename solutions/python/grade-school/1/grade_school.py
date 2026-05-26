class School:
    def __init__(self):
        self.record = []
        self.students = set()
        self.grades = {}

    def add_student(self, name, grade):
        if name not in self.students:
            self.students.add(name)
            self.grades.setdefault(grade, [])
            self.grades[grade].append(name)
            self.grades[grade].sort()
            self.record.append(True)
        else:
            self.record.append(False)

    def roster(self):
        students = []
        for grade in sorted(self.grades.keys()):
            students.extend(self.grades[grade])
        return students

    def grade(self, grade_number):
        return self.grades.get(grade_number, [])

    def added(self):
        return self.record
