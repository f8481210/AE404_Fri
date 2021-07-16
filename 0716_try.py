# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 17:45:47 2021

@author: N
"""

'''
try:
    f = open("test.txt","r")
    print(f.read())
    
except:
    print("File is not find")

finally:
    print("File is close")
    
'''
try:
    with open("python.txt","r") as f:
        f.read()
except IOError:
    print("File is not find")
    
 