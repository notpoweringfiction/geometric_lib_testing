import unittest
import circle, triangle, square, rectangle


class RectangleTestCase(unittest.TestCase):

   # Area tests
   def test_area_both_zero(self):
      res = rectangle.area(0, 0)
      self.assertEqual(res, 0)

   def test_area_first_zero(self):
      res = rectangle.area(0, 2)
      self.assertEqual(res, 0)

   def test_area_second_zero(self):
      res = rectangle.area(5, 0)
      self.assertEqual(res, 0)

   def test_area_small_nums_1(self):
      res = rectangle.area(4, 6)
      self.assertEqual(res, 4 * 6)

   def test_area_small_nums_2(self):
      res = rectangle.area(10, 2)
      self.assertEqual(res, 10 * 2)
   
   def test_area_big_nums_1(self):
      res = rectangle.area(500, 1024)
      self.assertEqual(res, 500 * 1024)
   
   def test_area_big_nums_2(self):
      res = rectangle.area(4_294_967_296, 2_124_413_981)
      self.assertEqual(res, 4_294_967_296 * 2_124_413_981)


   def test_area_first_negative_num(self):
      with self.assertRaises(ValueError):
            rectangle.area(-20, 1)
   
   def test_area_second_negative_num(self):
      with self.assertRaises(ValueError):
            rectangle.area(5, -12)
   
   def test_area_both_negative_num(self):
      with self.assertRaises(ValueError):
            rectangle.area(-20, -12)
      
   # Perimeter tests

   def test_perimeter_both_zero(self):
      res = rectangle.perimeter(0, 0)
      self.assertEqual(res, 0)

   def test_perimeter_first_zero(self):
      res = rectangle.perimeter(0, 2)
      self.assertEqual(res, 4)

   def test_perimeter_second_zero(self):
      res = rectangle.perimeter(5, 0)
      self.assertEqual(res, 10)

   def test_perimeter_small_nums_1(self):
      res = rectangle.perimeter(4, 6)
      self.assertEqual(res, 10 * 2)

   def test_perimeter_small_nums_2(self):
      res = rectangle.perimeter(10, 2)
      self.assertEqual(res, 12 * 2)
   
   def test_perimeter_big_nums_1(self):
      res = rectangle.perimeter(500, 1024)
      self.assertEqual(res, 2 * (500 + 1024))
   
   def test_perimeter_big_nums_2(self):
      res = rectangle.perimeter(4_294_967_296, 2_124_413_981)
      self.assertEqual(res, 2 * (4_294_967_296 + 2_124_413_981))

   def test_perimeter_first_negative_num(self):
      with self.assertRaises(ValueError):
            rectangle.perimeter(-20, 1)
   
   def test_perimeter_second_negative_num(self):
      with self.assertRaises(ValueError):
            rectangle.perimeter(5, -12)
   
   def test_perimeter_both_negative_num(self):
      with self.assertRaises(ValueError):
            rectangle.perimeter(-20, -12)
    

class TriangleTestCase(unittest.TestCase):

   # Area tests
   def test_area_both_zero(self):
      res = triangle.area(0, 0)
      self.assertEqual(res, 0)

   def test_area_first_zero(self):
      res = triangle.area(0, 1)
      self.assertEqual(res, 0)

   def test_area_second_zero(self):
      res = triangle.area(5, 0)
      self.assertEqual(res, 0)

   def test_area_small_nums_1(self):
      res = triangle.area(4, 6)
      self.assertEqual(res, 2 * 6)

   def test_area_small_nums_2(self):
      res = triangle.area(10, 2)
      self.assertEqual(res, 10)
   
   def test_area_big_nums_1(self):
      res = triangle.area(500, 1024)
      self.assertEqual(res, 500 * 1024 / 2)
   
   def test_area_big_nums_2(self):
      res = triangle.area(4_294_967_296, 2_924_613_111)
      self.assertEqual(res, 4_294_967_296 * 2_924_613_111 / 2)


   def test_area_first_negative_num(self):
      with self.assertRaises(ValueError):
            triangle.area(-20, 1)
   
   def test_area_second_negative_num(self):
      with self.assertRaises(ValueError):
            triangle.area(5, -12)
   
   def test_area_both_negative_num(self):
      with self.assertRaises(ValueError):
            triangle.area(-20, -12)
      
   # Perimeter tests

   def test_perimeter_both_zero(self):
      res = triangle.perimeter(0, 0, 0)
      self.assertEqual(res, 0)

   def test_perimeter_first_zero(self):
      res = triangle.perimeter(0, 2, 4)
      self.assertEqual(res, 6)

   def test_perimeter_second_zero(self):
      res = triangle.perimeter(5, 0, 4)
      self.assertEqual(res, 9)

   def test_perimeter_small_nums_1(self):
      res = triangle.perimeter(4, 6, 7)
      self.assertEqual(res, 17)

   def test_perimeter_small_nums_2(self):
      res = triangle.perimeter(10, 2, 15)
      self.assertEqual(res, 27)
   
   def test_perimeter_big_nums_1(self):
      res = triangle.perimeter(500, 1024, 999)
      self.assertEqual(res, 500 + 1024 + 999)
   
   def test_perimeter_big_nums_2(self):
      res = triangle.perimeter(4_294_967_296, 2_124_413_981, 3_164_531_771)
      self.assertEqual(res, 4_294_967_296 + 2_124_413_981 + 3_164_531_771)

   def test_perimeter_first_negative_num(self):
      with self.assertRaises(ValueError):
            triangle.perimeter(-20, 1, 4)
   
   def test_perimeter_second_negative_num(self):
      with self.assertRaises(ValueError):
            triangle.perimeter(5, -12, 10)
   
   def test_perimeter_third_negative_num(self):
      with self.assertRaises(ValueError):
            triangle.perimeter(5, 1, -100)

   def test_perimeter_all_negative_num(self):
      with self.assertRaises(ValueError):
            triangle.perimeter(-20, -12, -275)
    


class SquareTestCase(unittest.TestCase):

   # Area tests
   def test_area_both_zero(self):
      res = square.area(0)
      self.assertEqual(res, 0)

   def test_area_small_nums_1(self):
      res = square.area(4)
      self.assertEqual(res, 4 * 4)

   def test_area_small_nums_2(self):
      res = square.area(10)
      self.assertEqual(res, 10 * 10)
   
   def test_area_big_nums_1(self):
      res = square.area(1024)
      self.assertEqual(res, 1024 * 1024)
   
   def test_area_big_nums_2(self):
      res = square.area(4_294_967_296)
      self.assertEqual(res, 4_294_967_296 * 4_294_967_296)


   def test_area_negative_num(self):
      with self.assertRaises(ValueError):
            square.area(-12)
      
   # Perimeter tests

   def test_perimeter_zero(self):
      res = square.perimeter(0)
      self.assertEqual(res, 0)

   def test_perimeter_small_nums_1(self):
      res = square.perimeter(6)
      self.assertEqual(res, 6 * 4)

   def test_perimeter_small_nums_2(self):
      res = square.perimeter(10)
      self.assertEqual(res, 10 * 4)
   
   def test_perimeter_big_nums_1(self):
      res = square.perimeter(1024)
      self.assertEqual(res, 1024 * 4)
   
   def test_perimeter_big_nums_2(self):
      res = square.perimeter(4_294_967_296)
      self.assertEqual(res, 4 * 4_294_967_296)

   def test_perimeter_negative_num(self):
      with self.assertRaises(ValueError):
            square.perimeter(-20)
    

class CircleTestCase(unittest.TestCase):

    # Area tests
    def test_area_zero(self):
       res = circle.area(0)
       self.assertEqual(res, 0)

    def test_area_small_num_1(self):
       res = circle.area(4)
       est_pi = 3.14159265358979323846
       self.assertAlmostEqual(res, 4 * 4 * est_pi, delta=0.05)

    def test_area_small_num_2(self):
       res = circle.area(10)
       est_pi = 3.14159265358979323846
       self.assertAlmostEqual(res, 10 * 10 * est_pi, delta=0.05)

    def test_area_big_num_1(self):
       res = circle.area(1024)
       est_pi = 3.14159265358979323846
       self.assertAlmostEqual(res, 1024 * 1024 * est_pi, delta=0.05)

    
    def test_area_bin_num_2(self):
       res = circle.area(4_294_967_296)
       est_pi = 3.14159265358979323846
       self.assertAlmostEqual(res, 4_294_967_296 * 4_294_967_296 * est_pi, delta=0.05)

    def test_area_negative_num(self):
       with self.assertRaises(ValueError):
            circle.area(-20)
       
    # Perimeter tests

    def test_perimeter_zero_num(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_small_num_1(self):
       res = circle.perimeter(4)
       est_pi = 3.14159265358979323846
       self.assertAlmostEqual(res, 2 * 4 * est_pi, delta=0.05)

    def test_perimeter_small_num_2(self):
       res = circle.perimeter(10)
       est_pi = 3.14159265358979323846
       self.assertAlmostEqual(res, 2 * 10 * est_pi, delta=0.05)

    def test_perimeter_big_num_1(self):
       res = circle.perimeter(1024)
       est_pi = 3.14159265358979323846
       self.assertAlmostEqual(res, 2 * 1024 * est_pi, delta=0.05)

    
    def test_perimeter_bin_num_2(self):
       res = circle.perimeter(4_294_967_296)
       est_pi = 3.14159265358979323846
       self.assertAlmostEqual(res, 2 * 4_294_967_296 * est_pi, delta=0.05)

    def test_perimeter_negative_num(self):
       with self.assertRaises(ValueError):
            circle.perimeter(-15)