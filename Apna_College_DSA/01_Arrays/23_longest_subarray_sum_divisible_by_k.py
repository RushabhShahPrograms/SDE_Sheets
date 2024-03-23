'''
Longest subarray with sum divisible by K
Given an array arr containing N integers and a positive integer K, find the length of the longest sub array with sum of the elements divisible by the given value K.

Example 1:

Input:
N = 6, K = 3
arr[] = {2, 7, 6, 1, 4, 5}
Output: 
4
Explanation:
The subarray is {7, 6, 1, 4} with sum 18, which is divisible by 3.
Example 2:

Input:
N = 7, K = 3
arr[] = {-2, 2, -5, 12, -11, -1, 7}
Output: 
5
Explanation:
The subarray is {2,-5,12,-11,-1} with sum -3, which is divisible by 3.
'''

def longest_subarray(arr, N, K):
    remainder_map = {}
    max_length = 0 
    prefix_sum = 0 

    for i in range(N):
        prefix_sum += arr[i]
        current_remainder = prefix_sum % K

        if current_remainder == 0:
            max_length = i + 1
        elif current_remainder in remainder_map:
            max_length = max(max_length, i - remainder_map[current_remainder])
        else:
            remainder_map[current_remainder] = i

    return max_length

# Example usage:
arr1 = [2, 7, 6, 1, 4, 5]
N1 = len(arr1)
K1 = 3
print(longest_subarray(arr1, N1, K1))

arr2 = [-2, 2, -5, 12, -11, -1, 7]
N2 = len(arr2)
K2 = 3
print(longest_subarray(arr2, N2, K2))
