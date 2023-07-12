'''
Problem Statement: Given an array that contains both negative and positive integers, find the maximum product subarray.

Examples:

Example 1:
Input:
 Nums = [1,2,3,4,5,0]
Output:
 120
Explanation:
 In the given array, we can see 1×2×3×4×5 gives maximum product value.


Example 2:
Input:
 Nums = [1,2,-3,0,-4,-5]
Output:
 20
Explanation:
 In the given array, we can see (-4)×(-5) gives maximum product value.
'''

def maxProductSubArray(nums):
    result = float('-inf')
    for i in range(len(nums)-1):
        product = 1

        for j in range(i,len(nums)):
            product *= nums[j]
            result = max(result,product)
    return result

nums = [1,2,-3,0,-4,-5]
print("The maximum product subarray:",maxProductSubArray(nums))