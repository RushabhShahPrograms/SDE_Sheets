'''
Write a program to merge two given dictionary
'''

dict1 = {"a":1,"b":2,"c":3}
dict2 = {"d":4,"e":5,"f":6}

merge_dict = {**dict1,**dict2}
print(merge_dict)