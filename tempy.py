#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Convert temperatures. Converts between Fahrenheit, Celcius, and Kelvin. 

tempy.py <temp_value> <unit_from> <unit_to>

Examples
--------
Example usage::

    $ ./tempy.py 1 K F
    Converting 1.0K to F
    -457.87F

"""
import sys

class Temperature(object):
    """
    base class for Temperature obects

    Examples
    --------
    Example usage::

        x = Temperature(t = 1)

    """
    def __init__(self, t):
        self.t = float(t)
    def __repr__(self):
        return('Temperature({0})'.format(self.t))
    def __str__(self):
        return('{0}'.format(self.t))

class Celcius(Temperature):
    def __init__(self, t):
        Temperature.__init__(self, t = t)
    def __repr__(self):
        return('Celcius({0})'.format(self.t))

    def to_F(self, t = None):
        """
        Converts Celcius to Fahrenheit
        """
        if not t:
            t = self.t
        f = float(((t * 9.0) / 5.0) + 32)
        return(f)

    def to_K(self, t = None):
        """
        Converts Celcius to Kelvin
        """
        if not t:
            t = self.t
        k = t + 273.15
        return(k)

class Kelvin(Temperature):
    def __init__(self, t):
        Temperature.__init__(self, t = t)
    def __repr__(self):
        return('Kelvin({0})'.format(self.t))

    def to_F(self, t = None):
        """
        Converts Kelvin to Fahrenheit
        """
        if not t:
            t = self.t
        f = float(((t * 9.0) / 5.0) - 459.67)
        return(f)

    def to_C(self, t = None):
        """
        Converts Kelvin to Celcius
        """
        if not t:
            t = self.t
        c = t - 273.15
        return(c)

class Fahrenheit(Temperature):
    def __init__(self, t):
        Temperature.__init__(self, t = t)
    def __repr__(self):
        return('Fahrenheit({0})'.format(self.t))

    def to_C(self, t = None):
        """
        Converts Fahrenheit to Celcius
        """
        if not t:
            t = self.t
        c = (t - 32.0) * (5.0/9.0)
        return(c)

    def to_K(self, t = None):
        """
        Converts Fahrenheit to Kelvin
        """
        if not t:
            t = self.t
        k = (t + 459.67) * (5.0/9.0)
        return(k)

def main():
    """
    Main control function for the script
    """
    t_val = float(sys.argv[1])
    from_unit = sys.argv[2]
    to_unit = sys.argv[3]

    unit_method_key = {
    'K': 'to_K',
    'C': 'to_C',
    'F': 'to_F'
    }

    unit_class_key = {
    'K': 'Kelvin',
    'C': 'Celcius',
    'F': 'Fahrenheit'
    }

    print("Converting {0}{1} to {2}: ".format(t_val, from_unit, to_unit))

    # create object of given class for temp value
    class_type = unit_class_key[from_unit]
    temp_obj = globals()[class_type](t_val)

    # get method to call on object
    method_to_call = unit_method_key[to_unit]
    converted_temp = getattr(temp_obj, method_to_call)()

    print('{0}{1}'.format(converted_temp, to_unit))


if __name__ == '__main__':
    main()
