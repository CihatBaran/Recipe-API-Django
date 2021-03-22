from django.test import TestCase

from app.calc import sum_two_number, sub_two_number


class CalcTests(TestCase):
    def test_sum_two_number(self):
        """Test two numbers are added together"""
        self.assertEqual(sum_two_number(3, 8), 11)

    def test_sub_two_numbers(self):
        """Test two numbers are subtructed"""
        self.assertEquals(sub_two_number(10, 5), 5)
