class Mother:
    
    motherName = ""

    def mother(self):
        print(self.motherName)


class Father:
    fatherName = ""

    def father(self):
        print(self.fatherName)


class Son(Mother, Father):
    def parents(self):
        print("Father:", self.fatherName)
        print("Mother:", self.motherName)


s1 = Son()
s1.fatherName = "RAM"
s1.motherName = "SITA"
s1.parents()
