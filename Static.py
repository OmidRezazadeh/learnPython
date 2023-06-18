class CssStudent:
    stream = "cse"

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


firstStudent = CssStudent('Geek', 1)
secondStudent = CssStudent("nerd", 2)
print(firstStudent.stream)  # prints "cse"
print(secondStudent.stream)  # prints "cse"

print(firstStudent.name)  # prints "Geek"
print(secondStudent.name)  # prints "Nerd"

print(firstStudent.roll)  # prints "1"
print(secondStudent.roll)  # prints "2"

# Class variables can be accessed using class
# name also
print(CssStudent.stream)  # prints "cse"

# Now if we change the stream for just a it won't be changed for b
firstStudent.stream = 'ece'
print(firstStudent.stream)  # prints 'ece'
print(secondStudent.stream)  # prints 'cse'

# To change the stream for all instances of the class we can change it
# directly from the class
CssStudent.stream = 'mech'

print(firstStudent.stream)  # prints 'ece'
print(secondStudent.stream)
