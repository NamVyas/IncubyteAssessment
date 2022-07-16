# -*- coding: utf-8 -*-
"""Incubyte.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1coDF-5YWv5NWcPvzKSmUyU8WRGINhE-1
"""

#string_calculator.py

import re
def add(numbers):
    if numbers == '':
        return 0
    else:
        numbers = map(int, re.findall(r"-?\d+", numbers))
        numbers = list(filter(lambda x: x < 1000, numbers))
        negative_numbers = list(filter(lambda x: x < 0, numbers))
        try:
          if negative_numbers: raise Exception('negatives not allowed ' + str(negative_numbers))
        except:
          print('negatives not allowed ' + str(negative_numbers))
        return sum(numbers)
    
#string_calculator_test.py

import code as calc
import pytest

def test_empty_string():
    assert calc.add('') == 0


def test_single_number_string():
    assert calc.add('34') == 34
    assert calc.add('0') == 0
    
def test_two_numbers_string():
    assert calc.add('61,32') == 93
    assert calc.add('21,21') == 42

def test_multiple_numbers_string():
    assert calc.add('1,2,3') == 6
    assert calc.add('100,200,300,50,10,40') == 700

def test_new_line_between_numbers_string():
    assert calc.add('1\n2,3') == 6
    assert calc.add('10\n20\n20\n10,20\n20') == 100

def test_different_delimiter():
    assert calc.add('//;\n1;2') == 3
    assert calc.add('//;\n1;2;7\n10') == 20

def test_ignore_larger_than_1000():
    assert calc.add('1000,100') == 100
    assert calc.add('1\n2,3000') == 3
    assert calc.add('//+\n1+2+7\n980') == 990

def test_any_length_delimiter():
    assert calc.add('//***\n10***20***70\n1000') == 100
    assert calc.add('//++\n1++2++7\n10') == 20

def test_multiple_delimiters():
    assert calc.add('//+*\n1+2*7') == 10
    assert calc.add('//+%\n1+2%7\n10') == 20

def test_handle_negative_numbers():
    with pytest.raises(Exception,match = r'negatives not allowed[-3, -4]'):
        assert calc.add('-3,-4,3')
    
def test_any_length_multiple_delimiters():
    assert calc.add('//++%%\n1++2%%3') == 6
    assert calc.add('//++%\n1++2%7\n10') == 20
