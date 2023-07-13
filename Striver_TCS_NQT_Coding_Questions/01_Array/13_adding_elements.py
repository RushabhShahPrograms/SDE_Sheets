'''
Problem Statement: Given an array of N integers, write a program to add an array element at the beginning, end, and at a specific position.

Example:
Input: N = 5, array[] = {1,2,3,4,5}
insertbeginning(6)
insertending(7)
insertatpos(8,4)
Output: 6,1,2,8,3,4,5,7
Explanation: 6 is added at the beginning and 7 is added at the end and 8 is added at position 4 
'''

def insert_at_position(arr, value, pos):
    n = len(arr)
    arr.append(None)
    for i in range(n, pos - 1, -1):
        arr[i] = arr[i - 1]
    arr[pos - 1] = value

# Main function
if __name__ == '__main__':
    arr = [10, 9, 14, 8, 20, 48, 16, 9]
    value = 40
    pos = 5

    print("Before inserting the value at position:")
    print(*arr)

    insert_at_position(arr, value, pos)

    print("After inserting the value at position:")
    print(*arr)