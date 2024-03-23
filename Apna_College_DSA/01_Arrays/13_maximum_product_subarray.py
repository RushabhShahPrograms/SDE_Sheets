'''
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.


Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

def maxProduct(nums):
    if not nums:
        return 0
    
    max_so_far = min_so_far = result = nums[0]

    for i in range(1,len(nums)):
        if nums[i]<0:
            max_so_far,min_so_far = min_so_far,max_so_far
        max_so_far = max(nums[i],max_so_far * nums[i])
        min_so_far = min(nums[i],min_so_far * nums[i])

        result = max(result,max_so_far)

    return result

print(maxProduct([2,3,-2,4]))
print(maxProduct([-2,0,-1]))