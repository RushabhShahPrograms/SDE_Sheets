'''
Circular rotation of an array by K position
Here in this program, we will learn about Python program for finding the circular rotations of array by k positions, which means rotating the elements in the array .The operation of the rotation moves the last element of the array to the first position and moves all the remaining elements to the right. Take into consideration the following [0,1,2] indexes to be checked.

Algorithm of Python program for finding the circular rotations of array by k positions
Algorithm
Step 1- Initialize a class

Step 2- Enter number of elements of array

Step 3- Enter number of rotations of array.

Step 4- Enter number of indexes to be displayed.

Step 5- Input array elements

Step 6- run a for loop, i=0; i< elements; , i++.

Step 7- then module your rotations with elements

Step 8- Enter the index of array to be displayed

Step 9- print number of indexes and rotations.
'''

def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr

arr = [1, 2, 3, 4, 5]
print("Array after left rotation is:", end=' ')
print(rotateArray(arr, len(arr), 2))