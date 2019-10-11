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
        self.assertEqual(round(converters.r2f(300), 2),  -159.67 )

    def test_ts2li(self):
        self.assertEqual(round(converters.ts2li(1), 2), round(0.014787, 2))

    def test_ts2ci(self):
        self.assertEqual(round(converters.ts2ci(100), 2),  round(90.2344, 2))

    def test_ts2cu(self):
        self.assertEqual(round(converters.ts2cu(100), 2),  round(6.25, 2))

    def test_ts2cf(self):
        self.assertEqual(round(converters.ts2cf(100), 2),  round(0.052218981478542737806, 2))

    def test_ts2ga(self):
        self.assertEqual(round(converters.ts2ga(100), 2),  round(0.390625, 2))

    def test_ci2li(self):
        self.assertEqual(round(converters.ci2li(100), 2),  round(1.6387047611999969732, 2))

    def test_ci2ts(self):
        self.assertEqual(round(converters.ci2ts(100), 2),  round(110.822399993669819, 2))

    def test_ci2cu(self):
        self.assertEqual(round(converters.ci2cu(100), 2),  round(6.92641, 2))

    def test_ci2cf(self):
        self.assertEqual(round(converters.ci2cf(100), 2),  round(0.0578703125, 2))

    def test_ci2ga(self):
        self.assertEqual(round(converters.ci2ga(100), 2),  round(0.4329, 2))

    def test_cu2li(self):
        self.assertEqual(round(converters.cu2li(300), 2),  round(70.976459144247812105, 2))

    def test_cu2ts(self):
        self.assertEqual(round(converters.cu2ts(300), 2),  round(4799.9992016000551303, 2))

    def test_cu2ci(self):
        self.assertEqual(round(converters.cu2ci(300), 2),  round(4331.2492795688, 2))

    def test_cu2cf(self):
        self.assertEqual(round(converters.cu2cf(300), 2),  round(2.50651, 2))

    def test_cu2ga(self):
        self.assertEqual(round(converters.cu2ga(300), 2),  round(18.75, 2))

    def test_cf2cu(self):
        self.assertEqual(round(converters.cf2cu(300), 2),  round(35906.49, 2))

    def test_cf2ga(self):
        self.assertEqual(round(converters.cf2ga(300), 2),  round(18.75, 2))

    def test_ga2li(self):
        self.assertEqual(round(converters.ga2li(300), 2),  round(1135.62, 2))

    def test_ga2ts(self):
        self.assertEqual(round(converters.ga2ts(300), 2),  round(76800, 2))

    def test_ga2ci(self):
        self.assertEqual(round(converters.ga2ci(300), 2),  round(69300, 2))

    def test_ga2cu(self):
        self.assertEqual(round(converters.ga2cu(300), 2),  round(4731.75, 2))

    def test_ga2cf(self):
        self.assertEqual(round(converters.ga2cf(300), 2),  round(40.104126575868, 2))