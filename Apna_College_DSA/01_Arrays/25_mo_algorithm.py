'''
MO’s Algorithm (Query Square Root Decomposition) | Set 1 (Introduction)
Let us consider the following problem to understand MO’s Algorithm.
We are given an array and a set of query ranges, we are required to find the sum of every query range.

Example: 

Input:  arr[]   = {1, 1, 2, 1, 3, 4, 5, 2, 8};
        query[] = [0, 4], [1, 3] [2, 4]
Output: Sum of arr[] elements in range [0, 4] is 8
        Sum of arr[] elements in range [1, 3] is 4  
        Sum of arr[] elements in range [2, 4] is 6
'''

import math

# Function to perform MO's Algorithm
def query_sum(arr, queries):
    n = len(arr)
    block_size = int(math.sqrt(n))

    # Sort queries based on blocks and then by right endpoint
    queries.sort(key=lambda x: (x[0] // block_size, x[1]))

    # Initialize variables
    current_sum = 0
    current_l = 0
    current_r = 0
    result = []

    # Function to add an element to the current sum
    def add_element(x):
        nonlocal current_sum
        current_sum += arr[x]

    # Function to remove an element from the current sum
    def remove_element(x):
        nonlocal current_sum
        current_sum -= arr[x]

    # Process each query
    for query in queries:
        l, r = query

        # Extend current range to include the next query
        while current_l < l:
            remove_element(current_l)
            current_l += 1
        while current_l > l:
            current_l -= 1
            add_element(current_l)

        while current_r < r:
            current_r += 1
            add_element(current_r)
        while current_r > r:
            remove_element(current_r)
            current_r -= 1

        # Store the sum for this query range
        result.append(current_sum)

    return result

# Example usage
arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
queries = [[0, 4], [1, 3], [2, 4]]

# Calculate the sum of each query range
result = query_sum(arr, queries)

# Output the results
for i in range(len(result)):
    print("Sum of arr[] elements in range", queries[i], "is", result[i])
