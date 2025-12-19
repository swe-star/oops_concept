from abc import ABC, abstractmethod

class task(ABC):
    def __init__(self, title, status):   # fixed syntax
        self.title = title
        self._status = status

    @abstractmethod                     # fixed decorator
    def complete(self):
        pass

    def get_status(self):
        return self._status


class developertask(task):
    def complete(self):
        print(f"{self.title} has the status {self._status}")  # fixed attribute


class testertask(task):
    def complete(self):
        print(f"{self.title} has the status {self._status}")  # fixed spacing & attribute


class managertask(task):
    def complete(self):
        print(f"{self.title} has the status {self._status}")  # fixed spacing & attribute


if __name__ == "__main__":
    task1 = developertask("Develop Feature", "In Progress")
    task2 = testertask("Test Feature", "Pending")
    task3 = managertask("Approve Feature", "Waiting")

    task1.complete()
    task2.complete()
    task3.complete()