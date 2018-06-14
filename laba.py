import random


class Person:
    def __init__(self, name):
        self.name = name;

    def display_info(self):
        print("Привет, меня зовут", self.name)


class Auto:
    color = "red"
    speed = random.randint(40, 220)
    def __init__(self, name):
        self.name = name

    def move(self):
        print(self.name," цвета ", self.color, " едет со скоростью ", self.speed, "км/ч")


def main():
    person1 = Person ("Din")
    person1.display_info()
    auto1 = Auto("BMW")
    auto1.move()


if __name__ == '__main__':
    main()
