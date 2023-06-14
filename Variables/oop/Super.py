# parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


# child class
class Student(Person):
    def __init__(self, name, age, dob):
        self.sName = name
        self.sAge = age
        self.dob = dob
        # inheriting the properties of parent class
        super().__init__("Rahul", age)

    def displayInfo(self):
        print(f"my name is {self.sName},  my age is {self.sAge}, my dob is {self.dob}")


obj = Student("Mayank", 23, "16-03-2000")
obj.display()
obj.displayInfo()
