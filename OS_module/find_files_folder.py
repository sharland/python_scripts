# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:19:48 2015

@author: sharland

simple example of finding a txt file

"""

import os

#for file in os.listdir("/Users/sharland"):
#    if file.endswith(".txt"):
#        print(file)
        
for file in os.listdir("/Users/sharland"):
    if file.startswith("work"):
        print(file)