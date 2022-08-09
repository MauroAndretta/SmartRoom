# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



from prolog import * 
from sensor import *

from pyswip import Prolog
prolog = Prolog()
prolog.consult("C:/Users/Mauro-Pc/Desktop/progetto/smarthome.pl")


print(simulateSensorValues())