import unittest
from unittest import mock

from student_system.models import (
    User,
    Student,
    StudyGroup,
    Subject,
    Grade,
)


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User(
            user_id=1,
            login="maks",
            password="1234",
            full_name="Максим Шило",
            email="maks@example.com"
        )

    def test_user_creation(self):
        self.assertEqual(self.user.id, 1)
        self.assertEqual(self.user.login_name, "maks")
        self.assertEqual(self.user.full_name, "Максим Шило")
        self.assertEqual(self.user.email, "maks@example.com")

    def test_change_password(self):
        self.user.change_password("new_password")

        self.assertEqual(
            self.user.password,
            "new_password"
        )


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student(
            user_id=1,
            login="student1",
            password="1234",
            full_name="Максим Шило",
            email="student@example.com",
            student_id=101,
            student_card_number="КН-001"
        )

    def test_student_creation(self):
        self.assertEqual(
            self.student.full_name,
            "Максим Шило"
        )

        self.assertEqual(
            self.student.student_id,
            101
        )

        self.assertEqual(
            self.student.student_card_number,
            "КН-001"
        )

        self.assertEqual(
            self.student.grades,
            []
        )

    def test_student_update(self):
        with mock.patch("builtins.print") as mock_print:
            self.student.update("Нова оцінка")

            mock_print.assert_called_once_with(
                "[Student: Максим Шило] Нова оцінка"
            )

    def test_student_view_grades_without_grades(self):
        with unittest.mock.patch("builtins.print") as mock_print:
            self.student.view_grades()

            mock_print.assert_any_call(
                "Оцінок поки немає."
            )


class TestStudyGroup(unittest.TestCase):

    def setUp(self):
        self.group = StudyGroup(
            group_id=1,
            name="ІПЗ-31",
            specialty="Інженерія програмного забезпечення",
            year=3
        )

        self.student = Student(
            user_id=1,
            login="student1",
            password="1234",
            full_name="Максим Шило",
            email="student@example.com",
            student_id=101,
            student_card_number="КН-001"
        )

    def test_group_creation(self):
        self.assertEqual(
            self.group.name,
            "ІПЗ-31"
        )

        self.assertEqual(
            self.group.specialty,
            "Інженерія програмного забезпечення"
        )

        self.assertEqual(
            self.group.year,
            3
        )

        self.assertEqual(
            self.group.students,
            []
        )

    def test_add_student_to_group(self):
        self.group.add_student(self.student)

        self.assertIn(
            self.student,
            self.group.students
        )

    def test_remove_student_from_group(self):
        self.group.add_student(self.student)
        self.group.remove_student(self.student)

        self.assertNotIn(
            self.student,
            self.group.students
        )


class TestSubject(unittest.TestCase):

    def setUp(self):
        self.subject = Subject(
            subject_id=1,
            name="Програмування",
            description="Основи програмування",
            hours=120
        )

    def test_subject_creation(self):
        self.assertEqual(
            self.subject.subject_id,
            1
        )

        self.assertEqual(
            self.subject.name,
            "Програмування"
        )

        self.assertEqual(
            self.subject.hours,
            120
        )

    def test_update_information(self):
        self.subject.update_information(
            description="Поглиблене програмування",
            hours=150
        )

        self.assertEqual(
            self.subject.description,
            "Поглиблене програмування"
        )

        self.assertEqual(
            self.subject.hours,
            150
        )


class TestGrade(unittest.TestCase):

    def setUp(self):
        self.student = Student(
            user_id=1,
            login="student1",
            password="1234",
            full_name="Максим Шило",
            email="student@example.com",
            student_id=101,
            student_card_number="КН-001"
        )

        self.grade = Grade(
            grade_id=1,
            value=95,
            date="2026-09-14",
            comment="Добре виконано",
            student=self.student,
            subject="Програмування"
        )

    def test_grade_creation(self):
        self.assertEqual(
            self.grade.grade_id,
            1
        )

        self.assertEqual(
            self.grade.value,
            95
        )

        self.assertEqual(
            self.grade.student,
            self.student
        )

        self.assertEqual(
            self.grade.subject,
            "Програмування"
        )

    def test_change_grade_value(self):
        self.grade.change_value(100)

        self.assertEqual(
            self.grade.value,
            100
        )


if __name__ == "__main__":
    unittest.main()
