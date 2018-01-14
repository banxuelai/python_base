#! /usr/bin/env python

import sys
str = "Hello World"
print str
print str[0]
print str[2:7]
print str[2:]
print sys.argv

list = ['first',1,'second',2]
tinylist = [3,'ff']

print list+tinylist

dict = {}
dict['one'] = "this is one"
dict[2] = "this is two"
tinylist = {'name':'jhon','phone':'15690018743','dept':'3.3'}

print dict['one']
print dict[2]
print tinylist
print tinylist.keys()
print tinylist.values()
exit(0)




