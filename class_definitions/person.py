class Person:
    """Person class"""
    def __init__(self, title, lname, fname, addy=''):         # Constructor
        self.last_name = lname
        self.first_name = fname
        self.address = addy


    def __str__(self):
        return 'Person with last name ' + str(self.last_name) + ', first name ' + str(self.first_name)

#Driver
#Valid person
person1 = Person('Duck', 'Donald')#ssn not required
print(str(person1))
