# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Aaron Manning 2020
# %% Code Cell 1

import pandas as pd
import matplotlib as plt
import numpy as np

a = 1
b = 4
c = a+b

list_sample = ['first','second','third']
values_sample = [1,2,3]

dict_sample = dict(zip(list_sample,values_sample))

# %% Code Cell 2

print (c)
print('this is my sample project')
for i in dict_sample:
    print(i + '->' + str(dict_sample[i]))
    
    

