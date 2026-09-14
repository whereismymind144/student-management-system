from student_system.models import (
    Student,
    Teacher,
    Administrator,
    StudyGroup,
    Subject,
    Grade
)

from student_system.notifications import EmailAlert
from student_system.storage import DataStorage
from student_system.system_manager import SystemManager


def main():

    print("=" * 60)
    print("СИСТЕМА УПРАВЛІННЯ СТУДЕНТАМИ")
    print("=" * 60)

    # 1. Створення сховища даних
    storage = DataStorage()

    # 2. Отримання єдиного екземпляра SystemManager
    manager1 = SystemManager()
    manager2 = SystemManager()

    print("\n[1] Перевірка Singleton:")
    print(
        f"manager1 is manager2: "
        f"{manager1 is manager2}"
    )

    # 3. Dependency Injection
    manager1.set_storage(storage)

    print("\n[2] DataStorage передано через Dependency Injection.")

    # 4. Створення студентів
    student1 = Student(
        user_id=1,
        login="max",
        password="1234",
        full_name="Максим Шило",
        email="max@example.com",
        student_id=101,
        student_card_number="IPZ-001"
    )

    student2 = Student(
        user_id=2,
        login="ivan",
        password="1234",
        full_name="Іван Петренко",
        email="ivan@example.com",
        student_id=102,
        student_card_number="IPZ-002"
    )

    storage.save_student(student1)
    storage.save_student(student2)

    # 5. Створення адміністратора
    administrator = Administrator(
        user_id=3,
        login="admin",
        password="admin",
        full_name="Адміністратор",
        email="admin@example.com",
        administrator_id=1
    )

    administrator.add_student(student1)

    # 6. Створення навчальної групи
    group = StudyGroup(
        group_id=1,
        name="ІПЗ-31",
        specialty="Інженерія програмного забезпечення",
        year=2026
    )

    administrator.create_group(group)

    administrator.add_to_group(student1, group)
    administrator.add_to_group(student2, group)

    group.view_students()

    # 7. Створення предмету
    subject = Subject(
        subject_id=1,
        name="Програмування",
        description="Основи програмування",
        hours=120
    )

    storage.save_subject(subject)

    # 8. Створення викладача
    teacher = Teacher(
        user_id=4,
        login="teacher",
        password="1234",
        full_name="Викладач",
        email="teacher@example.com",
        teacher_id=1,
        department="Кафедра програмної інженерії"
    )

    teacher.add_subject(subject)

    # 9. Підписка Observer
    email_alert = EmailAlert(
        "admin@example.com"
    )

    manager1.attach(student1)
    manager1.attach(student2)
    manager1.attach(email_alert)

    print("\n[3] Observer-и успішно підписані.")

    # 10. Додавання оцінки
    grade = Grade(
        grade_id=1,
        value=95,
        date="2026-09-11",
        comment="Відмінна робота",
        student=student1,
        subject=subject.name
    )

    teacher.enter_grade(grade)

    print("\n[4] Додавання нової оцінки:")

    manager1.add_grade(grade)

    # 11. Перегляд оцінок
    student1.view_grades()

    # 12. Пошук студентів через інтерфейс
    print("\n[5] Пошук студента:")

    results = manager1.search_students("Максим")

    for student in results:
        print(
            f"Знайдено: {student.full_name}, "
            f"ID: {student.student_id}"
        )

    print("\n" + "=" * 60)
    print("Демонстрацію завершено.")
    print("=" * 60)


if __name__ == "__main__":
    main()