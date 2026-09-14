from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    """Інтерфейс Observer."""

    @abstractmethod
    def update(self, message: str) -> None:
        """Отримати повідомлення від Subject."""
        pass


class StudentSearch(ABC):
    """Інтерфейс пошуку студентів."""

    @abstractmethod
    def search_students(self, query: str) -> List[object]:
        """Пошук студентів за заданим запитом."""
        pass






