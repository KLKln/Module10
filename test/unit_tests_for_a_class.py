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

    def test_object_created_all_attributes(self):
        student = s.Student('Constantine', 'John', 'DEMON HUNTING', '4,0')
        assert student.last_name == 'Constantine'
        assert student.first_name == 'John'
        assert student.major == 'DEMON HUNTING'
        assert student.gpa == '4,0'


if __name__ == '__main__':
    unittest.main()
