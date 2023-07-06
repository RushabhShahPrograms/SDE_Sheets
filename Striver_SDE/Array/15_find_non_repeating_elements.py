'''
Problem Statement: Find all the non-repeating elements for a given array. Outputs can be in any order.

Examples:

Example 1:
Input:
 Nums = [1,2,-1,1,3,1]
Output:
 2,-1,3
Explanation:
 1 is the only element in the given array which occurs thrice in the array. -1,2,3 occurs only once and hence, these are non-repeating elements of the given array.

Example 2:
Input:
 Nums = [1,2,3]
Output:
 1,2,3
Explanation:
 All elements present in the array occur once. Hence, every element is non-repeating.
'''

def find_non_repeating_element(nums):
    non_repeating_nums = []
    for i in range(len(nums)):
        chk = False
        for j in range(len(nums)):
            if i!=j and nums[i] == nums[j]:
                chk = True
                break
        
        if not chk:
            non_repeating_nums.append(nums[i])
    
    print("Non-repeating numbers are:")
    print(*non_repeating_nums)


if __name__ == '__main__':
    nums = [1,2,-1,1,3,1]
    find_non_repeating_element(nums)