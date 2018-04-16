# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:13:23 2015

@author: sharland
"""

class Adding:
    def DoAdd(self, Value1=0, Value2=0):
        Sum = Value1 + Value2
        print("The sum of {0} plus {1} is {2}.".format(Value1, Value2, Sum))
        

MyInstance = Adding()
MyInstance.DoAdd(5,8)

