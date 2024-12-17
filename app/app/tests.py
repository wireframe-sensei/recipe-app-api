"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CaclTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        res = calc.add(3, 8)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test that two numbers are subtracted"""
        res = calc.subtract(8, 4)
        self.assertEqual(res, 4)
