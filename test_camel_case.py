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


if __name__ == '__main__':
    import unittest
    unittest.main()
