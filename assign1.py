# -*- coding: utf-8 -*-
'''
You`ve learned about dictionaries, strings and how you can manipulate strings by joining them using different methods.
However, there are other useful aspects of string manipulation such as extracting the relevant data out of a string.
Write a program (in Python 3) to print "I have attended ------ sessions!!" from the below variable dataset containing sessionIDs

Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}

[hint : it's a good idea to use the split function]

Eg. 
Sessions_Attended = {'sessions' : '1011,2344,'}
Answer:
I have attended 2 sessions!!
'''

Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}



values_list = Sessions_Attended['sessions'].split(',')


print ("I have attended %d sessions!!" % (len(values_list)))

