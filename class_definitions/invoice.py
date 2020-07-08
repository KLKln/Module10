"""
Program: invoice.py
Author: Kelly Klein
Last date modified: 7/5/2020
This program will
"""


class Invoice:
    def __init__(self, invoice_id, customer_id, address, lname, fname,  phone, items_with_price={}):
        """
use reST style.
    :param invoice_id: unique int assigned to identify an invoice
    :param customer_id: unique int assigned to identify customer
    :param last_name: customer's last name
    :param first_name: customer's first name
    :param address: customer's address
    :param phone_number: customer's phone number
    :return:
"""

        self.invoice_id = invoice_id
        # invoice_id: int: required
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
        self.items_with_price = items_with_price
        # items_with_price: dictionary, optional
        # since optional, how do we default to a 'blank' dictionary

    def create_invoice(self):
        """
    use reST style.

        :return:

"""
        print('invoice number: ', self.invoice_id)
        print('customer id: ', self.cid)
        print(self.last_name, self.first_name)
        print('address: ', self.address)
        print('phone number: ', self.phone)

        subtotal = 0
        # items_with_price = {}
        # loop over each k, v pair in items_with_price
        # print str(key) + '.....' + str(value)
        # subtotal assigned to itself + value
        for k, v in self.items_with_price.items():
            print(k, ':', v)
            subtotal += v
        # at end of loop we have the sum of all values
        # tax = 6%
        tax = .06
        # tax_owed = subtotal * tax
        tax_owed = subtotal * tax
        # total is tax_owed + subtotal
        total = subtotal + tax_owed
        # print our tax ........108.00
        print('Tax Owed.........' + '$', tax_owed)
        # print our total ........ 1907.98
        print('Total..........' + '$', total)

    def add_item(self, item_price_dict):
        """
    use reST style.
        :param item_price_dict:
"""
        for key, value in item_price_dict.items():
            self.items_with_price[key] = value

    #invoice_id, customer_id, lname, fname,  phone, address
    def __str__(self):
        return self.invoice_id, self.cid, self.last_name, self.first_name, self.phone, self.address

    def __repr__(self):
        return self.invoice_id, self.cid, self.last_name, self.first_name, self.phone, self.address


if __name__ == '__main__':
    # Driver code
    invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802', 'Mouse', 'Minnie', '555-867-5309')
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()
