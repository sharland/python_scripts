# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pylab import *
import random

plotvalues = []
plotvalues2 = []

for i in range(1,20):
    x= random.randint(1,10)
    plotvalues.append(x)


plot(plotvalues)



xlabel('hello world')