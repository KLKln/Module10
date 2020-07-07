"""
Program: invoice.py
Author: Kelly Klein
Last date modified: 7/5/2020
This program will
"""


class Invoice:
    def __init__(self, invoice_id, customer_id, lname, fname, address, phone, items_with_price=dict()):
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

    def create_invoice(self, invoice_id, customer_id, last_name, first_name, address,
                      phone_number,  items_with_price):
        """
    use reST style.
    :param invoice_id: unique int assigned to identify an invoice
    :param customer_id: unique int assigned to identify customer
    :param last_name: customer's last name
    :param first_name: customer's first name
    :param address: customer's address
    :param phone_number: customer's phone number
    :param items_with_price: dictionary containing item and price
        :return:
"""
        subtotal = 0
        #items_with_price = {}
        #loop over each k, v pair in items_with_price
            #print str(key) + '.....' + str(value)
            #subtotal assigned to itself + value
        for k, v in items_with_price:
            print(k, ':', v)
            subtotal += v
        #at end of loop we have the sum of all values
        #tax = 6%
        tax = .06
        #tax_owed = subtotal * tax
        tax_owed = subtotal * tax
        #total is tax_owed + subtotal
        total = subtotal + tax_owed
        # print our tax ........108.00
        print('Tax Owed.........'+'$', tax_owed)
        # print our total ........ 1907.98
        print('Total..........'+'$', total)

    def add_item(item, price):
        """
    use reST style.
        :param item:
        :param price:
        :return: item, price

"""
        items_with_price = dict()
        for i in items_with_price:
            if i == item:
                print('error')
                return
        items_with_price[item] = price

        return items_with_price

    def __str__(self):
        return self.cid, self.first_name + self.last_name, self.address, self.phone

    def __repr__(self):
        return self.cid, self.first_name + self.last_name, self.address, self.phone


if __name__ == '__main__':
    # Driver code
    invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309' )
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
