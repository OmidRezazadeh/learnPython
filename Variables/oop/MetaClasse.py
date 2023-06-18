
class Person:
    type = "developer"

    def __init__(self, name, weight, age):
        self.name = name
        self.weigh = weight
        self.age = age

    def eat(self):
        print(f"you can eat your name is: {self.name}")

    def walk(self):
        print(f"you can walk your name is: {self.name}")

    def talk(self):
        print(f"you can eat your name is: {self.age}")

    @classmethod
    def info(cls):
        print(f"my job is {cls.type}")

    @classmethod
    def baby(cls):
        return cls('baby', 37, 0)


person = Person("omid", 170, 25)
person.eat()

baby = Person.baby()
baby.eat()
baby.talk()
