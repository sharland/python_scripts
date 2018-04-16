# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 10:08:13 2015

@author: sharland

how to add lists to a dictionary
"""

testDic = {'student3': [0,1,3],'student4' :1}

testDic['student1'] = [1,4,2,7]
testDic['student2'] = [4,8,1,9]

print(testDic)

keys = testDic.keys()

keys.sort()

for i in keys:
    getValue = testDic.get(keys[i], default=None)
    print(keys[i],getValue)

