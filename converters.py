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