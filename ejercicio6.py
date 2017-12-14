#!/usr/bin/python
# -*- coding: utf-8 -*-
#Valle Juarez Pedro Angel
	
dic={i:(bin(i),hex(i))for i in range(51) if  bin(i).count('1')%2!=0}

print dic
print '\ndone'
