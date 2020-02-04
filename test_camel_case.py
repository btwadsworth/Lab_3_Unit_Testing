from unittest import TestCase
import camel_case

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):
        expected = 'helloWorld'
        actual = camel_case.camel_case('Hello World')
        self.assertEqual(expected, actual)

    def test_extra_spaces(self):
        expected = 'helloWorld'
        actual = camel_case.camel_case('Hello     World')
        self.assertEqual(expected, actual)

    def test_numbers(self):
        expected = True
        actual = camel_case.check_for_numbers('ABC DEF G 5H IJ K')
        self.assertEqual(expected, actual)

    def test_remove_special_chars(self):
        expected = 'hello world'
        actual = camel_case.remove_special_chars('he$ll^o *()world')
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    import unittest
    unittest.main()
