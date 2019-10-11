import unittest
import converters


class TestConverters(unittest.TestCase):

    def test_k2c(self):
        """Return Kelvin converted to Celsius."""
        self.assertEqual(round(converters.k2c(300), 2), 26.85)

    def test_k2f(self):
        """Return Kelvin converted to Fahrenheit."""
        self.assertEqual(round(converters.k2f(300), 2), 80.33)

    def test_k2r(self):
        """Return Kelvin converted to Rankine."""
        self.assertEqual(round(converters.k2r(300), 2), 540)

    def test_c2k(self):
        """Return Celsius converted to Kelvin."""
        self.assertEqual(round(converters.c2k(10), 2), 283.15)

    def test_c2f(self):
        """Return Celsius converted to Fahrenheit."""
        self.assertEqual(round(converters.c2f(20), 2),  68)

    def test_c2r(self):
        """Return Celsius converted to Rankine."""
        self.assertEqual(round(converters.c2r(20), 2),  527.67)

    def test_f2k(self):
        """Return Fahrenheit converted to Kelvin."""
        self.assertEqual(round(converters.f2k(60), 2),  288.71)

    def test_f2c(self):
        """Return Fahrenheit converted to Kelvin."""
        self.assertEqual(round(converters.f2c(68), 2),  20)

    def test_f2r(self):
        """Return Fahrenheit converted to Rankine."""
        self.assertEqual(round(converters.f2r(68), 2),  527.67)

    def test_r2k(self):
        """Return Rankine converted to Kelvin."""
        self.assertEqual(round(converters.r2k(300), 2),  166.67)

    def test_r2c(self):
        """Return Rankine converted to Celsius."""
        self.assertEqual(round(converters.r2c(300), 2),  -106.48)

    def test_r2f(self):
        """Return Rankine converted to Fahrenheit."""
        self.assertEqual(round(converters.r2f(300), 2),  -159.67)

