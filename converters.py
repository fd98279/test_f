# All converter functions
def k2c(x):
    """Return Kelvin converted to Celsius."""
    return x - 273.15

def k2f(x):
    """Return Kelvin converted to Fahrenheit."""
    return x * 9/5 - 459.67

def k2r(x):
    """Return Kelvin converted to Rankine."""
    return x * 9/5

def c2k(x):
    """Return Celsius converted to Kelvin."""
    return x + 273.15

def c2f(x):
    """Return Celsius converted to Fahrenheit."""
    return  x * 9/5 + 32

def c2r(x):
    """Return Celsius converted to Rankine."""
    return (x + 273.15) * 9/5

def f2k(x):
    """Return Fahrenheit converted to Kelvin."""
    return (x + 459.67) * 5/9

def f2c(x):
    """Return Fahrenheit converted to Kelvin."""
    return (x - 32) * 5/9

def f2r(x):
    """Return Fahrenheit converted to Rankine."""
    return x + 459.67

def r2k(x):
    """Return Rankine converted to Kelvin."""
    return x * 5/9

def r2c(x):
    """Return Rankine converted to Celsius."""
    return (x - 491.67) * 5/9

def r2f(x):
    """Return Rankine converted to Fahrenheit."""
    return  x - 459.67

# Volumne converters

def li2ts(x):
    """Return Liters converted to Tablespoons."""
    return  x * 67.628045

def li2ci(x):
    """Return Liters converted to Cubic inches."""
    return  x * 61.024

def li2cu(x):
    """Return Liters converted to Cups."""
    return  x * 4.2267528377

def li2cf(x):
    """Return Liters converted to Cubic feet."""
    return  x * 0.035315

def li2ga(x):
    """Return Liters converted to Gallons."""
    return  x * 0.2641720524

def ts2li(x):
    return  x * 0.014787

def ts2ci(x):
    return  x * 0.902344

def ts2cu(x):
    return  x * 0.0625

def ts2cf(x):
    return  x * 0.00052219

def ts2ga(x):
    return  x * 0.00390625

def ci2li(x):
    return  x * 0.0163871

def ci2ts(x):
    return  x * 1.10823

def ci2cu(x):
    return  x * 0.0692641

def ci2cf(x):
    return  x * 0.000578704

def ci2ga(x):
    return  x * 0.004329

def cu2li(x):
    return  x * 0.236588

def cu2ts(x):
    return  x * 16

def cu2ci(x):
    return  x * 14.4375

def cf2cf(x):
    return  x * 0.00835503

def cf2ga(x):
    return  x * 0.0625

def ga2li(x):
    return  x * 3.78541

def ga2ts(x):
    return  x * 256

def ga2ci(x):
    return  x * 231

def ga2cu(x):
    return  x * 16

def ga2cf(x):
    return  x * 0.133681