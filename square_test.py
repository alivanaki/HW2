import unittest
from main import Shape, Square


class MyTestCase(unittest.TestCase):

    def test_compute_area_square(self):
        square = Square(5)
        self.assertEqual(square.computeArea(), 25)

    def test_get_side(self):
        square = Square(5)
        self.assertEqual(square.getSide(), 5)

    def test_set_side(self):
        square = Square(5)
        square.setSide(7)
        self.assertEqual(square.getSide(), 7)

if __name__ == '__main__':
    unittest.main()
