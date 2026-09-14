from typing import List

from .interfaces import StudentSearch
from .models import Student, StudyGroup, Subject, Grade


class DataStorage(StudentSearch):
    """Сховище даних системи."""

    def __init__(self):
        self.students: List[Student] = []
        self.groups: List[StudyGroup] = []
        self.subjects: List[Subject] = []
        self.grades: List[Grade] = []

    def save_student(self, student: Student) -> None:
        self.students.append(student)

    def save_group(self, group: StudyGroup) -> None:
        self.groups.append(group)

    def save_subject(self, subject: Subject) -> None:
        self.subjects.append(subject)

    def save_grade(self, grade: Grade) -> None:
        self.grades.append(grade)

        if grade not in grade.student.grades:
            grade.student.grades.append(grade)

    def search_students(self, query: str) -> List[Student]:
        query = query.lower()

        return [
            student
            for student in self.students
            if (
                query in student.full_name.lower()
                or query in student.login_name.lower()
                or query in str(student.student_id)
            )
        ]




