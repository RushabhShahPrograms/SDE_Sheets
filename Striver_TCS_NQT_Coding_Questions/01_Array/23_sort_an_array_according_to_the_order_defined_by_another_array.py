'''
Sort Array according to the order defined by Another Array
In this article, we will learn In this article, we will learn about Python Program to Sort Array according to the order defined by Another Array.

We have given two arrays A1[] and A2[], sort A1 in such a way that the relative order among the elements will be same as those are in A2. For the elements not present in A2, append them at last in sorted order.

In this method we will use the concept of hashing to sort the array arr1 on the basis of the order of arr2 elements.
'''

from collections import Counter

def solve(arr1, arr2):
    res = []
    
    f = Counter(arr1)
     
    for e in arr2:
       
        res.extend([e]*f[e])
         
        f[e] = 0
         
    rem = list(sorted(filter(lambda x: f[x] != 0, f.keys())))
     
    for e in rem:
        res.extend([e]*f[e])
         
    return res
 
 
# Driver Code
arr1 = [ 20, 1, 20, 5, 7, 1, 9, 39, 6, 18, 18 ];
arr2 = [ 20, 1, 18, 39 ];
print(*solve(arr1, arr2))