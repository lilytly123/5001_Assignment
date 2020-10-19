# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 20:05:50 2020

@author: 49166
"""

import re
import xml.dom.minidom as xm
dom = xm.parse('blocklist.xml')
page = dom.documentElement
lst = page.getElementsByTagName('emItem')
ID = []
for i in lst:
    ID.append(i.getAttribute('id'))

for j in ID:
    c=re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z_\-]{1,19}\.[com,cn,net,org]{1,3}$',j)
    if c:
        k=ID.index(j)
        print(lst[k].toxml().split('\n')[0])
