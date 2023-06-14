class GrandFather:
    def __init__(self, grandFatherName):
        self.grandFatherName = grandFatherName


class Father(GrandFather):
    def __init__(self, fatherName, grandFatherName):
        self.fatherName = fatherName

        GrandFather.__init__(self, grandFatherName)


class Son(Father):
    def __init__(self, sonName, fatherName, grandfatherName):
        self.sonName = sonName

        Father.__init__(self, fatherName, grandfatherName)

    def resultName(self):
        print('grand father name:', self.grandFatherName)
        print("father name :", self.fatherName)
        print("son name:", self.sonName)


s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandFatherName)
s1.resultName()
