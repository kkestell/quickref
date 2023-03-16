```python
import unittest

# Basic test case
class MyTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

# Running test cases
if __name__ == '__main__':
    unittest.main()

# Test fixtures
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.my_list = [1, 2, 3]

    def test_length(self):
        self.assertEqual(len(self.my_list), 3)

    def test_contains(self):
        self.assertIn(2, self.my_list)

    def tearDown(self):
        del self.my_list

# Skipping tests
class MyTestCase(unittest.TestCase):
    @unittest.skip('Skipping test')
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

# Expected failures
class MyTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_addition(self):
        self.assertEqual(1 + 1, 3)

# Parameterized tests
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_cases = [
            (1, 2, 3),
            (2, 2, 4),
            (3, 2, 5),
        ]

    def test_addition(self):
        for a, b, expected in self.test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(a + b, expected)

# Mocking objects
from unittest.mock import MagicMock

class MyTestCase(unittest.TestCase):
    def test_mock(self):
        mock_obj = MagicMock()
        mock_obj.my_method.return_value = 42
        result = mock_obj.my_method()
        self.assertEqual(result, 42)

# Skipping entire test cases
@unittest.skip('Skipping entire test case')
class MyTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

# Asserting exceptions
class MyTestCase(unittest.TestCase):
    def test_division(self):
        with self.assertRaises(ZeroDivisionError):
            result = 1 / 0

# Skipping tests conditionally
class MyTestCase(unittest.TestCase):
    @unittest.skipIf(sys.version_info.major < 3, 'Python 2 is not supported')
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

# Running only a subset of tests
class MyTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(2 - 1, 1)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2, testRunner=unittest.TextTestRunner(verbosity=2)).run(MyTestCase('test_addition'))


```
