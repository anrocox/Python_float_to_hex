#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2014

@author: anroco

How to convert a float to hex in Python?

¿Cómo convertir un float a hexadecimal en Python?
'''

#crate a float number
f = 21.94
print(f)

#the hex() method generate the representation of a floating-point number as a
#hexadecimal string.
#review https://docs.python.org/3/library/stdtypes.html#float.fromhex
s_hex = f.hex()
print(s_hex)

#crate a negative float number
f = -2834.9982
print(f)

#get hex string from 'f'
s_hex = f.hex()
print(s_hex)
