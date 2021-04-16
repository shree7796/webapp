import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # only for testing CI/CD. Will add real test once CI will implemented.
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
