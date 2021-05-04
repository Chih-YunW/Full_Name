import unittest
import name

class testCaseName(unittest.TestCase):
        def test_normal_name(self):
                self.assertEqual(name.full_name("Emily", "Lee"), "Emily Lee")
        def test_blank_firstName(self):
                self.assertEqual(name.full_name("", "Smith"), " Smith")
        def test_type_integer(self):
                self.assertRaises(TypeError, name.full_name, 4, 5)

if __name__ == '__main__':
        unittest.main()

