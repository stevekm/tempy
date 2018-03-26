#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
unit tests for the tempy module
"""
import unittest
from tempy import Celcius, Kelvin, Fahrenheit

class TestConverter(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True, 'Demo assertion')

    def test_fail(self):
        self.assertFalse(False)

    def test_error(self):
        self.assertRaises(ValueError)

    def test_C_to_K1(self):
        x = Celcius(-273.15)
        y = x.to_K()
        self.assertTrue(y == 0, 'Celcius to Kelvin conversion failed')

    def test_C_to_K2(self):
        x = Celcius(80)
        y = x.to_K()
        self.assertTrue(y == 353.15, 'Celcius to Kelvin conversion failed')

    def test_C_to_F1(self):
        x = Celcius(-50)
        y = x.to_F()
        self.assertTrue(y == -58.0, 'Celcius to Fahrenheit conversion failed')

    def test_C_to_F2(self):
        x = Celcius(90)
        y = x.to_F()
        self.assertTrue(y == 194.0, 'Celcius to Fahrenheit conversion failed')


    def test_K_to_C1(self):
        x = Kelvin(10)
        y = x.to_C()
        self.assertTrue(y == -263.15, 'Kelvin to Celcius conversion failed')

    def test_K_to_C2(self):
        x = Kelvin(500)
        y = round(x.to_C(), 2)
        self.assertTrue(y == 226.85, 'Kelvin to Celcius conversion failed')

    def test_K_to_F1(self):
        x = Kelvin(0)
        y = round(x.to_F(), 2)
        self.assertTrue(y == -459.67, 'Kelvin to Fahrenheit conversion failed')

    def test_K_to_F2(self):
        x = Kelvin(150)
        y = round(x.to_F(), 2)
        self.assertTrue(y == -189.67, 'Kelvin to Fahrenheit conversion failed')


    def test_F_to_C1(self):
        x = Fahrenheit(-459.67)
        y = round(x.to_C(), 2)
        self.assertTrue(y == -273.15, 'Fahrenheit to Celcius conversion failed')

    def test_F_to_C2(self):
        x = Fahrenheit(-50)
        y = round(x.to_C(), 2)
        self.assertTrue(y == -45.56, 'Fahrenheit to Celcius conversion failed')

    def test_F_to_C3(self):
        x = Fahrenheit(160)
        y = round(x.to_C(), 2)
        self.assertTrue(y == 71.11, 'Fahrenheit to Celcius conversion failed')

    def test_F_to_K1(self):
        x = Fahrenheit(-459.67)
        y = round(x.to_K(), 2)
        self.assertTrue(y == 0.0, 'Fahrenheit to Kelvin conversion failed')

    def test_F_to_K2(self):
        x = Fahrenheit(200)
        y = round(x.to_K(), 2)
        self.assertTrue(y == 366.48, 'Fahrenheit to Kelvin conversion failed')


if __name__ == '__main__':
    unittest.main()
