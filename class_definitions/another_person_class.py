class Person(object):
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, title, name, surname, allowed_titles=TITLES):
        if title not in allowed_titles:
            raise ValueError("%s is not a valid title." % title)

        self.title = title  # Ok to access directly objectName.title
        self._name = name  # should be considered private
        self.__surname = surname  # considered private, name mangled

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.isdigit():
            raise ValueError
        self._name = value

    def __str__(self):
        return 'Person with last name ' + str(self.__surname) + ', first name ' + str(self._name)


# Driver
# Valid person


person1 = Person('Dr', 'Duck', 'Donald')  # ssn not required
print(str(person1))
