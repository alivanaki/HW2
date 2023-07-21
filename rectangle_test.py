import unittest
from main import Shape, Rectangle

class TestRectangle(unittest.TestCase):

    def test_compute_area(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.computeArea(), 50)

    def test_get_width(self):
        rect = Rectangle(width=5, height=10)
        self.assertEqual(rect.getWidth(), 5)

    def test_get_height(self):
        rect = Rectangle(width=5, height=10)
        self.assertEqual(rect.getHeight(), 10)


if __name__ == '__main__':
    unittest.main()
