# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 19:51:14 2021

@author: N
"""

import re
'''
num = input('輸入電話號碼:')
if re.fullmatch("^(09)\d{8}$",num) != None:
    print("符合")
else:
    print("ERROR")
'''    
#使用者輸入gmail 
num = input('輸入gmail:')
if re.fullmatch("[0-9A-Za-z]+@gmail.com",num) != None:
    print("符合")
else:
    print("ERROR")

