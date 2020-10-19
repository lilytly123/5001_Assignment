# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 18:55:33 2020

@author: 49166
"""
import re
import xml.dom.minidom as xm
dom = xm.parse('blocklist.xml')
page = dom.documentElement
a = page.getElementsByTagName('emItem')
b = page.getElementsByTagName('gfxBlacklistEntry')
lst = a+b
#print(lst)
blockID=[]
for i in lst:
    blockID.append(i.getAttribute('blockID'))

for j in blockID:
    c=re.match('^i.*\d$|^g.*\d$',j)
    if c:
        n=blockID.index(j)
        print(lst[n].toxml().split('\n')[0])



