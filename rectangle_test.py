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

    def test_set_width(self):
        rect = Rectangle(5, 10)
        rect.setWidth(7)
        self.assertEqual(rect.getWidth(), 7)
        self.assertEqual(rect.getHeight(), 10)

    def test_set_height(self):
        rect = Rectangle(5, 10)
        rect.setHeight(12)
        self.assertEqual(rect.getWidth(), 5)
        self.assertEqual(rect.getHeight(), 12)


if __name__ == '__main__':
    unittest.main()
