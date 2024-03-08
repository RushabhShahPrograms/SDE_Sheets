'''
the max item of each row of a matrix
'''

def max_in_rows(matrix):
    max_items = [max(row) for row in matrix]

    return max_items

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
max_items = max_in_rows(matrix)

print("Max items in each row: ", max_items)