import unittest

from student_system.models import Student
from student_system.storage import DataStorage


class TestDataStorage(unittest.TestCase):

    def setUp(self):
        self.storage = DataStorage()

        self.student1 = Student(
            user_id=1,
            login="maks",
            password="1234",
            full_name="Максим Шило",
            email="max@example.com",
            student_id=101,
            student_card_number="КН-001"
        )

        self.student2 = Student(
            user_id=2,
            login="olena",
            password="1234",
            full_name="Олена Петренко",
            email="olena@example.com",
            student_id=102,
            student_card_number="КН-002"
        )

    def test_save_student(self):
        self.storage.save_student(self.student1)

        self.assertIn(
            self.student1,
            self.storage.students
        )

    def test_search_student_by_name(self):
        self.storage.save_student(self.student1)
        self.storage.save_student(self.student2)

        result = self.storage.search_students("Максим")

        self.assertIn(
            self.student1,
            result
        )

        self.assertNotIn(
            self.student2,
            result
        )

    def test_search_student_by_login(self):
        self.storage.save_student(self.student1)

        result = self.storage.search_students("maks")

        self.assertIn(
            self.student1,
            result
        )

    def test_empty_search(self):
        result = self.storage.search_students(
            "Неіснуючий студент"
        )

        self.assertEqual(
            result,
            []
        )


if __name__ == "__main__":
    unittest.main()
