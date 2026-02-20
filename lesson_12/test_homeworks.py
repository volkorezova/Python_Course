import sys
import os
import unittest
from unittest import TestCase

# Add directory to sys.path, to get known where homeworks.py should be found
sys.path.append(os.path.dirname(__file__))

# import functions from  з homeworks.py
from homeworks import string_filters, Student, sum_even_numbers

class TestStringFilter(TestCase):
    def test_string_filter(self):
        self.assertEqual(string_filters(['a', 3, 'n']), ['a', 'n'])
        self.assertEqual(string_filters([1, 2, 3]), [])
        self.assertEqual(string_filters(['x', 'y', 5, None]), ['x', 'y'])

    def test_string_filter_empty(self):
        self.assertEqual(string_filters([]), [])

    def test_string_filter_no_strings(self):
        self.assertEqual(string_filters([1, 2, 3, None, True]), [])

class TestStudent(TestCase):
    def test_student_creation(self):
        s = Student(name='Ivan', surname='Ivanov', age=20, average_grade=10)
        self.assertEqual(s.name, 'Ivan')
        self.assertEqual(s.surname, 'Ivanov')
        self.assertEqual(s.age, 20)
        self.assertEqual(s.average_grade, 10)

    def test_grade_change(self):
        s = Student(name='Anna', surname='Petrova', age=22, average_grade=12)
        s.change_grade(15)
        self.assertEqual(s.average_grade, 15)

    def test_grade_change_negative(self):
        s = Student(name='Anna', surname='Petrova', age=22, average_grade=12)
        s.change_grade(-5)
        self.assertEqual(s.average_grade, -5)

    def test_grade_change_none(self):
            s = Student(name='Anna', surname='Petrova', age=22, average_grade=12)
            s.change_grade()
            self.assertIsNone(s.average_grade)

class TestSumEvenNumbers(TestCase):
    def test_sum_even_numbers_basic(self):
        self.assertEqual(sum_even_numbers([1, 2, 3, 4, 5, 6]), 12)

    def test_sum_even_numbers_no_even(self):
        self.assertEqual(sum_even_numbers([1, 3, 5]), 0)

    def test_sum_even_numbers_empty(self):
        self.assertEqual(sum_even_numbers([]), 0)

    def test_sum_even_numbers_all_even(self):
        self.assertEqual(sum_even_numbers([2, 4, 6, 8]), 20)

if __name__ == "__main__":
    unittest.main()
