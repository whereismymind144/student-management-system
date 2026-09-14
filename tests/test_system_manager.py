import unittest
from unittest.mock import Mock

from student_system.interfaces import Observer
from student_system.system_manager import SystemManager


class TestSystemManager(unittest.TestCase):

    def setUp(self):
        SystemManager._instance = None

        self.manager = SystemManager()

        self.mock_observer = Mock(
            spec=Observer
        )

    def tearDown(self):
        SystemManager._instance = None

    def test_singleton_instance(self):
        manager1 = SystemManager()
        manager2 = SystemManager()

        self.assertIs(
            manager1,
            manager2
        )

    def test_attach_observer(self):
        self.manager.attach(
            self.mock_observer
        )

        self.assertIn(
            self.mock_observer,
            self.manager._observers
        )

    def test_detach_observer(self):
        self.manager.attach(
            self.mock_observer
        )

        self.manager.detach(
            self.mock_observer
        )

        self.assertNotIn(
            self.mock_observer,
            self.manager._observers
        )

    def test_notify_observer(self):
        self.manager.attach(
            self.mock_observer
        )

        message = "Нова оцінка: 95"

        self.manager.notify(message)

        self.mock_observer.update.assert_called_once_with(
            message
        )

    def test_notify_multiple_observers(self):
        observer1 = Mock(
            spec=Observer
        )

        observer2 = Mock(
            spec=Observer
        )

        self.manager.attach(observer1)
        self.manager.attach(observer2)

        message = "Нова оцінка: 95"

        self.manager.notify(message)

        observer1.update.assert_called_once_with(
            message
        )

        observer2.update.assert_called_once_with(
            message
        )


if __name__ == "__main__":
    unittest.main()