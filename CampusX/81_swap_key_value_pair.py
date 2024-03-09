'''
Write a program to swap the key value pair for max and min values
Eg if the dict is like this {‘a’:1,’b’:2,’c’:3}
Output should be {a:3,b:2,c:1}
'''

dict1 = {'a':1,'b':2,'c':3}

key_max = max(dict1, key=dict1.get)
key_min = min(dict1, key=dict1.get)

dict1[key_max], dict1[key_min] = dict1[key_min], dict1[key_max]

print(dict1)
