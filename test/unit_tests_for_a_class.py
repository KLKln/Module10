import unittest
from class_definitions import student as s


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Klein', 'Kelly', 'CIS', '3.7')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Klein')
        self.assertEqual(self.student.first_name, 'Kelly')
        self.assertEqual(self.student.major, 'CIS')


if __name__ == '__main__':
    unittest.main()
