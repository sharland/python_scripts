# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 12:38:00 2016

@author: sharland
"""

class Person:
  def __init__(self, name):
    self.name = name
  
  def greet(self,name,other_name):
    return "Hi {0}, my name is {1}".format(other_name, name)
    
Person.greet("bob","bill","ben")