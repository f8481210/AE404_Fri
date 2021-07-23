# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 18:15:59 2021

@author: N
"""

import re
pattern1 = "cat"
pattern2 = "dog"

string = "in the house cat"

#print(pattern1 in string)
#print(re.search(pattern1, string))
#print(re.match(pattern1, string)) #字首開始判斷
#print(re.fullmatch(pattern1, string)) #一模一樣
#print(re.sub(pattern1,pattern2,string)) #代替 sub(被替換的單字, 取代的單字 , 句子)

string = "cat in the house cat"
print(re.findall(pattern1, string)) #找到的結果存成list





string1 = ""
string2 = 123

#print(re.fullmatch('\d*', string1))
#print(re.fullmatch('\d?', string2))



