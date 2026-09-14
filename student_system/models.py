from dataclasses import dataclass, field
from typing import List

from .interfaces import Observer


class User:
    """Базовий клас користувача системи."""

    def __init__(
        self,
        user_id: int,
        login: str,
        password: str,
        full_name: str,
        email: str
    ):
        self.id = user_id
        self.login_name = login
        self.password = password
        self.full_name = full_name
        self.email = email

    def login(self) -> None:
        print(f"{self.full_name} увійшов у систему.")

    def logout(self) -> None:
        print(f"{self.full_name} вийшов із системи.")

    def change_password(self, new_password: str) -> None:
        self.password = new_password


class Student(User, Observer):
    """Студент системи та Observer для отримання повідомлень."""

    def __init__(
        self,
        user_id: int,
        login: str,
        password: str,
        full_name: str,
        email: str,
        student_id: int,
        student_card_number: str
    ):
        User.__init__(
            self,
            user_id,
            login,
            password,
            full_name,
            email
        )

        self.student_id = student_id
        self.student_card_number = student_card_number
        self.grades: List["Grade"] = []

    def view_grades(self) -> None:
        print(f"\nОцінки студента {self.full_name}:")

        if not self.grades:
            print("Оцінок поки немає.")
            return

        for grade in self.grades:
            print(
                f"- {grade.subject}: "
                f"{grade.value} ({grade.comment})"
            )

    def view_subjects(self) -> None:
        print(f"{self.full_name} переглядає список предметів.")

    def update(self, message: str) -> None:
        """Реалізація Observer."""
        print(f"[Student: {self.full_name}] {message}")


class Teacher(User):
    """Викладач."""

    def __init__(
        self,
        user_id: int,
        login: str,
        password: str,
        full_name: str,
        email: str,
        teacher_id: int,
        department: str
    ):
        super().__init__(
            user_id,
            login,
            password,
            full_name,
            email
        )

        self.teacher_id = teacher_id
        self.department = department

    def add_subject(self, subject: "Subject") -> None:
        print(
            f"Викладач {self.full_name} додав предмет "
            f"{subject.name}."
        )

    def enter_grade(self, grade: "Grade") -> None:
        print(
            f"Викладач {self.full_name} виставив оцінку "
            f"{grade.value}."
        )

    def edit_grade(self, grade: "Grade", new_value: int) -> None:
        grade.change_value(new_value)


class Administrator(User):
    """Адміністратор системи."""

    def __init__(
        self,
        user_id: int,
        login: str,
        password: str,
        full_name: str,
        email: str,
        administrator_id: int
    ):
        super().__init__(
            user_id,
            login,
            password,
            full_name,
            email
        )

        self.administrator_id = administrator_id

    def add_student(self, student: Student) -> None:
        print(
            f"Адміністратор {self.full_name} додав "
            f"студента {student.full_name}."
        )

    def edit_student(self, student: Student) -> None:
        print(
            f"Дані студента {student.full_name} "
            f"відредаговано."
        )

    def delete_student(self, student: Student) -> None:
        print(
            f"Студента {student.full_name} видалено."
        )

    def create_group(self, group: "StudyGroup") -> None:
        print(
            f"Створено навчальну групу {group.name}."
        )

    def add_to_group(
        self,
        student: Student,
        group: "StudyGroup"
    ) -> None:
        group.add_student(student)
        print(
            f"Студента {student.full_name} додано "
            f"до групи {group.name}."
        )

    def search_student(
        self,
        students: List[Student],
        surname: str
    ) -> List[Student]:
        return [
            student
            for student in students
            if surname.lower() in student.full_name.lower()
        ]


@dataclass
class StudyGroup:
    """Навчальна група."""

    group_id: int
    name: str
    specialty: str
    year: int
    students: List[Student] = field(default_factory=list)

    def add_student(self, student: Student) -> None:
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student: Student) -> None:
        if student in self.students:
            self.students.remove(student)

    def view_students(self) -> None:
        print(f"\nСтуденти групи {self.name}:")

        for student in self.students:
            print(f"- {student.full_name}")


@dataclass
class Subject:
    """Навчальний предмет."""

    subject_id: int
    name: str
    description: str
    hours: int

    def update_information(
        self,
        description: str,
        hours: int
    ) -> None:
        self.description = description
        self.hours = hours


@dataclass
class Grade:
    """Оцінка студента."""

    grade_id: int
    value: int
    date: str
    comment: str
    student: Student
    subject: str

    def change_value(self, new_value: int) -> None:
        self.value = new_value