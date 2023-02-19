# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 19:10:57 2023

@author: Nico
"""

import datetime

input_date = '1979-12-15'
input_date = input_date.split('-')
print(input_date)
# YYY-MM-DD
fecha1 = datetime.date(int(input_date[0]), int(input_date[1]), int(input_date[2]))
fecha2 = datetime.date(2019, 1, 1)

print(fecha1)
print(fecha2)

print(fecha1 < fecha2)


print(fecha1 > fecha2)


print(fecha2 < fecha1)


print(fecha2 > fecha1)
