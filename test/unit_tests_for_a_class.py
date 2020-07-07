import unittest
from class_definitions import student as s



class MyTestCase(unittest.TestCase):
    def setup(self):
        self.student = s.Student('Klein', 'Kelly', 'CIS', '3.7')

    def tearDown(self):
        del self.student

    


if __name__ == '__main__':
    unittest.main()
