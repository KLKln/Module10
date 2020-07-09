"""
Program: customer.py
Author: Kelly Klein
Last date modified: 7/4/2020
This program will create a class called customer allowing the user to
access information about a customer, also will raise AttributeError if
cid is not an int
"""


class Customer:
    def __init__(self, customer_id, lname, fname, address, phone):
        """
use reST style.
    :param customer_id: int assigned to identify customer
    :param last_name: customer's last name
    :param first_name: customer's first name
    :param address: customer's address
    :param phone_number: customer's phone number
    :return:
"""
        #this error is raised in the constructor
        """
        try:
            if isinstance(customer_id, int):
                self.cid = customer_id
        except AttributeError:
            AttributeError("'Customer' attribute has no attribute 'cid'")
"""

        self.cid = customer_id
        # customer_id: int: required
        self.last_name = lname
        # last_name: string: required
        self.first_name = fname
        # first_name: string: required
        self.address = address
        # address: string: required
        self.phone = phone
        # phone_number: string: required

    def display(self):
        """
    use reST style.
    :param customer_id: int assigned to identify customer
    :param last_name: customer's last name
    :param first_name: customer's first name
    :param address: customer's address
    :param phone_number: customer's phone number
        :return:
"""
        print(self.cid)
        print(self.first_name + ' ' + self.last_name)
        print(self.address)
        print(self.phone)

    def __str__(self):
        return self.cid, self.first_name + self.last_name, self.address, self.phone

    def __repr__(self):
        return self.cid, self.first_name + self.last_name, self.address, self.phone


if __name__ == '__main__':
    customer1 = Customer(1, 'Kelly', 'Klein', '456 main ave.\nnowhere, IA',
                         '319-456-7890')
    print(customer1.display())

    customer2 = Customer('this should fail', 'Samsam', 'Sam', '321 anywhere pl.\n Cedar Rapids, IA',
                         '999-999-9999')

    print(customer2.display())
