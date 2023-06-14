# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def sayHi(self):
#         print("say", self.name)
#
#
# p = Person('hi')
# p.sayHi()


class Car:
    def __init__(self, firstName, lastName, old):
        self.firstName = firstName
        self.lastName = lastName
        self.old = old

    def interview(self):
        print(f"my name is {self.firstName} and last name is{self.lastName}")


# result = Car("rwerw", "sadfsdf", 22)
# result.interview()


class Bmw(Car):
    def print(self):
        print("Emp class called")


Bmw_de = Bmw("rwerw", "sadfsdf", 22)
Bmw_de.interview()
Bmw_de.print()

# class Car:
#     def __init__(self, firstName, lastName, old):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.old = old
#
#     def interview(self):
#         print(f"my name is {self.firstName} and last name is {self.lastName}")
#
#
# result = Car("rwerw", "sadfsdf",22)
# result.interview()
