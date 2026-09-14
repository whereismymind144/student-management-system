from typing import List

from .interfaces import Observer, StudentSearch
from .models import Grade


class SystemManager:
    """
    Центральний менеджер системи.
    Реалізує Singleton та Subject з патерна Observer.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(
        self,
        storage: StudentSearch | None = None
    ):
        if getattr(self, "_initialized", False):
            return

        self._observers: List[Observer] = []
        self.storage = storage
        self._initialized = True

    def set_storage(
        self,
        storage: StudentSearch
    ) -> None:
        """
        Dependency Injection для сховища.
        """
        self.storage = storage

    def attach(self, observer: Observer) -> None:
        """Додає Observer до списку підписників."""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Видаляє Observer зі списку підписників."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """Повідомляє всіх підписників."""
        for observer in self._observers:
            observer.update(message)

    def add_grade(self, grade: Grade) -> None:
        """
        Додає оцінку та генерує подію Observer.
        """

        if self.storage is None:
            raise RuntimeError(
                "DataStorage не було передано через Dependency Injection."
            )

        self.storage.save_grade(grade)

        message = (
            f"Нова оцінка: {grade.value} з предмета "
            f"{grade.subject} для студента "
            f"{grade.student.full_name}"
        )

        self.notify(message)

    def search_students(self, query: str):
        """
        Делегує пошук об'єкту, який реалізує StudentSearch.
        """
        if self.storage is None:
            raise RuntimeError("Сховище не налаштовано.")

        return self.storage.search_students(query)
