from collections import defaultdict

class Teacher:
    def __init__(self, name, availability):
        self.name = name
        self.availability = availability
        self.students = []
        self.preferences = {}

    def set_preferences(self, students):
        for student in students:
            self.preferences[student.name] = student.availability

    def get_available_student(self):
        for student in self.students:
            if student.available:
                student.available = False
                return student
        return None

class Student:
    def __init__(self, name, availability):
        self.name = name
        self.availability = availability
        self.available = True
        self.preferences = {}

    def set_preferences(self, teachers):
        for teacher in teachers:
            self.preferences[teacher.name] = teacher.availability

def gale_shapley(teachers, students):
    while True:
        free_teacher = None
        for teacher in teachers:
            if not teacher.students:
                free_teacher = teacher
                break
        if not free_teacher:
            break

        for student_name in free_teacher.preferences:
            student = [s for s in students if s.name == student_name][0]
            if student.available:
                # Check for overlap in availability
                overlap = list(set(free_teacher.availability) & set(student.preferences[free_teacher.name]))
                if overlap:
                    free_teacher.students.append(student)
                    student.available = False
            else:
                current_teacher = [t for t in teachers if student in t.students][0]
                print(student.preferences[current_teacher.name]) #
                print(student.availability) #
                print(student.preferences[free_teacher.name]) #
                print(student.preferences[free_teacher.name].index(student.availability))
                if student.preferences[current_teacher.name].index(student.availability) > student.preferences[free_teacher.name].index(student.availability):
                    current_teacher.students.remove(student)
                    free_teacher.students.append(student)
                    student.available = False

    schedule = defaultdict(list)
    for teacher in teachers:
        for student in teacher.students:
            schedule[teacher.name].append(student.name)

    return dict(schedule)

# Example usage:
if __name__ == "__main__":
    teacher1 = Teacher("Teacher1", ["Monday: 8-10", "Wednesday: 14-16"])
    teacher2 = Teacher("Teacher2", ["Tuesday: 12-14", "Thursday: 9-11"])

    student1 = Student("Student1", ["Monday: 8-10", "Tuesday: 9-11", "Thursday: 9-11"])
    student2 = Student("Student2", ["Wednesday: 14-16", "Thursday: 9-11"])
    student3 = Student("Student3", ["Tuesday: 12-14", "Wednesday: 14-16"])

    teachers = [teacher1, teacher2]
    students = [student1, student2, student3]

    for teacher in teachers:
        teacher.set_preferences(students)

    for student in students:
        student.set_preferences(teachers)

    schedule = gale_shapley(teachers, students)

    print("Schedule:")
    for teacher, students in schedule.items():
        print(f"{teacher} -> {', '.join(students)}")