#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 04:02:10 2020

@author: Tim
"""

#1)
#a)
a=list(range(1,21))

#b)
b=list(range(20,0,-1))

#c)
c= a + list(range(19,0,-1))

#d)
d = [4,6,3]*10

#e)
e = d +[4]


import math
import numpy as np

#2)
for i in np.arange(3,6,0.1):
    print(math.exp(i)*math.cos(i))
  
#3) 
for i in range(1,26,1):
    print((2**i)/i)
    

#4)
    #a)
for i in range(0,len(a)):
    print(a[i]-a[len(a)-i-1])
    
#b)
for i in range(0,len(a)):
    print(a[i]%2==0)
    
#5)
lorem = open("lorem.txt")
text = lorem.read()

import re

patlen = re.compile(r'\b\w{1,4}\b|\b\w{4,7}\b|\b\w{8,}\b')

#a)
matchlen = patlen.findall(text)
print('5a): Letters within ranges: %s\n' % len(matchlen))

patup = re.compile('([A-Z][a-z]+)')
    
matchup=patup.findall(text)

print('5b): Uppercase Letters: %s\n' % len(matchup))
