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
        student = s.Student('Constantine', 'John', 'DEMONHUNTING', '4.0')
        assert student.last_name == 'Constantine'
        assert student.first_name == 'John'
        assert student.major == 'DEMONHUNTING'
        assert student.gpa == '4.0'

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Klein, Kelly has major CIS with gpa: 3.7')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = s.Student('123', 'Kelly', 'CIS')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            p = s.Student('Klein', '123', 'CIS')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            p = s.Student('Klein', 'Kelly', '123')

    #def test_object_not_created_error_gpa(self):
        #pass

if __name__ == '__main__':
    unittest.main()
