class Family:
    def __init__(self,surname,family_members):
        self.surname = surname
        self.family_members = family_members


    def display(self):
        print("surname of this family is:",self.surname)
        print("members of this family are:",self.family_members)

child = Family("jha",6)
child.display
print(child.surname,child.family_members)