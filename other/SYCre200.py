# -*- coding : utf-8 -*-

a='750c517b1f7d4a7b026e417d0d0d557b600c7b65500a'
x = a.decode('hex')
b = ''
for i in range(len(x)):
    tmp=ord(str(x[i]))^32
    b +=chr(tmp+4)
print b

