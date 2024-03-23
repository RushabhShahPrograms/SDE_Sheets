'''
Array reverse or reverse a array means changing the position of each number of the given array to its opposite position from end, i.e. if a number is at position 1 then its new position will be Array.length, similarly if a number is at position 2 then its new position will be Array.length – 1, and so on.

Input: original_array[] = {1, 2, 3}
Output: array_reversed[] = {3, 2, 1}

Input: original_array[] = {4, 5, 1, 2}
Output: array_reversed[] = {2, 1, 5, 4}
'''

original_array = [1, 2, 3, 4, 5]

reversed_array = list(reversed(original_array))
print(reversed_array)