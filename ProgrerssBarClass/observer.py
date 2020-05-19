from abc import ABC, abstractmethod
from time import sleep


class Observer:
    def __init__(self):
        super().__init__()

    @abstractmethod
    def update(self, *args, **kwargs):
        pass


class FirstObserver(Observer):
    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        sleep(0.20)


class SecondObserver(Observer):
    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        sleep(0.05)


class ThirdObserver(Observer):
    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        sleep(0.10)

