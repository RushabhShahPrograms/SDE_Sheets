'''
Write a program to find histogram of a given set of numbers. Take bin size from user. Print the result in the form of a dictionary.
'''

def calc_histogram(numbers, bin_size):
    min_num = min(numbers)
    max_num = max(numbers)

    num_bins = (max_num - min_num) // bin_size + 1

    histogram = {i: 0 for i in range(int(min_num), int(max_num + 1), bin_size)}

    for number in numbers:
        bin_number = number // bin_size * bin_size
        histogram[bin_number] += 1
    
    return histogram

numbers = [1,2,3,4,5,6,7,8,9,10]
bin_size = int(input("Enter the bin size: "))
print(calc_histogram(numbers,bin_size))