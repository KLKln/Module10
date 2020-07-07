"""
Program: employee.py
Author: Kelly Klein
Last date modified: 7/4/2020
This program will create a class called employee allowing the user to
access information about an employee
"""

import datetime


class Employee:
    def __init__(self, lname, fname, address, phone, salaried, start_date, salary):

        """
        use reST style.
        :param last_name: employee's last name
        :param first_name: employee's first name
        :param address: employees address
        :param phone_number: employee's phone number
        :param salaried: boolean salaried or not
        :param start_date: date employee started
        :param salary: double to indicate salary
        :return:
        """
        self.last_name = lname
        #last_name: string
        self.first_name = fname
        #first_name: string
        self.address = address
        #address: string
        self.phone = phone
        #phone_number: string
        self.salaried = salaried
        #salaried: boolean
        self.start_date = start_date
        #start_date: datetime
        self.salary = salary
        #salary: double

    def display(self):
        """
        use reST style.
        :param last_name: employee's last name
        :param first_name: employee's first name
        :param address: employees address
        :param phone_number: employee's phone number
        :param salaried: whether employee is salaried or not
        :param start_date: date employee started working
        :param salary: employee's yearly salary or hourly wage
        :return:
        """
        print(self.first_name + ' ' + self.last_name)
        print(self.address)
        print(self.phone)
        if self.salaried is False:
            print('Hourly Employee:', self.salary)
        else:
            print('Salaried Employee:', self.salary)

    def __str__(self):
        print(str(self.first_name + self.last_name, self.address, self.phone, self.salaried, self.start_date, self.salary))

    def __repr__(self):
        print(repr(self.first_name + self.last_name, self.address, self.phone, self.salaried, self.start_date, self.salary))


if __name__ == '__main__':
    s_date = datetime.datetime(2019, 5, 17)
    employee1 = Employee('Klein', 'Kelly', '42 Fake st\nCoralville, IA',
                         '319-377-2760', True, s_date, '$65000.00')
    print(employee1.display())
    s_date = datetime.datetime(2020, 1, 20)
    employee2 = Employee('Lauper', 'Cyndi', '45 Elm St\nIowa City, IA',
                         '319-345-8998', False, s_date,'$35.00 an hour')
    print(employee2.display())
