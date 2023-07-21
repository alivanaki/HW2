import unittest

class TestRectangle(unittest.TestCase):

    def test_compute_area(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.computeArea(), 50)


if __name__ == '__main__':
    unittest.main()
