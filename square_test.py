import unittest
from main import Shape, Square


class MyTestCase(unittest.TestCase):

    def test_compute_area_square(self):
        square = Square(5)
        self.assertEqual(square.computeArea(), 25)

    def test_get_side(self):
        square = Square(5)
        self.assertEqual(square.getSide(), 5)

if __name__ == '__main__':
    unittest.main()
