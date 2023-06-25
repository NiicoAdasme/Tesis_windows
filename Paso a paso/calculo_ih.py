# -*- coding: utf-8 -*-
"""
Created on Sat May 27 23:53:42 2023

@author: Nico
"""
from WaterRiskIndex1 import get_index_month_zone
from datetime import datetime

fecha_str = '1979-01-01'
fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
mes = fecha.strftime('%m')
print(mes)

tprom=0
pr=0
#mes=1
zona=12
resultado = get_index_month_zone(tprom, pr, mes, zona)

