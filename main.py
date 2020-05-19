from ProgrerssBarClass.subject import Subject
from ProgrerssBarClass.observer import FirstObserver, SecondObserver, ThirdObserver
import random


def main():
    subject = Subject()
    ran_num = random.sample(range(1, 1000), 100)

    for v in ran_num:
        if v % 3 == 0:
            subject.add_observer(FirstObserver)
        elif v % 2 == 0:
            subject.add_observer(SecondObserver)
        elif v % 1 == 0:
            subject.add_observer(ThirdObserver)

    subject.notify(None)


if '__main__' == __name__:
    main()
