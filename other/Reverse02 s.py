# -*- coding : utf-8 -*-

a='Th1s_Is_So_Easy'
b = ''
for i in range(len(a)):
    tmp=ord(str(a[i]))^7
    b +=chr(tmp)
print b
