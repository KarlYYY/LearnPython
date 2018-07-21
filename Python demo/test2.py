#!/usr/bin/env python3
# -*- coding: utf-8 -*-
list1=['Alice','Bob','Chris','Dean'] # list
print('The first list element is %s'%list1[0])
print('The last list element is %s'%list1[-1])
list1.pop()
print('The last list element is %s'%list1[-1])
list1.append('Eric')
print('The last list element is %s'%list1[-1])

tuple1=('A','B','C','D') #tuple
tuple2=(1,)
print('The first tuple element is %s'%tuple1[0])

tuple3=(1,'s',[10,20])
tuple3[2][0]=30
print('The tuple is %d'%tuple3[2][0])

name = input()
