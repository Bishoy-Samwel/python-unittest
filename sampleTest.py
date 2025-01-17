import unittest

from sample import car_speed, student_score


class TestStringMethods(unittest.TestCase):

    def test_car_speed(self):
        self.assertEqual(car_speed(-10), 'Level shall be Invalid')
        self.assertEqual(car_speed(30), 'Level shall be Low')
        self.assertEqual(car_speed(60), 'Level shall be Normal')
        self.assertEqual(car_speed(150), 'Level shall be High')
        self.assertEqual(car_speed(210), 'Level shall be V.High')
        self.assertEqual(car_speed(250), 'Level shall be Invalid')

    def test_student_score(self):
        self.assertEqual(student_score(-10), 'Level shall be Invalid')
        self.assertEqual(student_score(40), 'Level shall be Low')
        self.assertEqual(student_score(60), 'Level shall be Normal')
        self.assertEqual(student_score(70), 'Level shall be High')
        self.assertEqual(student_score(80), 'Level shall be V.High')
        self.assertEqual(student_score(90), 'Level shall be Excellent')
        self.assertEqual(student_score(101), 'Level shall be Invalid')



if __name__ == '__main__':
    unittest.main()