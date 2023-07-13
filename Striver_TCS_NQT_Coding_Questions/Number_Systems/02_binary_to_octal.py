'''
Problem Statement: Convert a binary number to an octal number

Examples:

Example 1:.
Input: N = 1100110
Output: 146
Explanation: 1100110 when converted to octal number is “146”.

Example 2:
Input: 11111
Output: 37
Explanation: 11111 when converted to octal number is “37”.
'''

# function to convert binary to octal
def convert(num):
    octalDigit = 0
    count = 1
    i = 0
    pos = 0
    octalArray = [0] * 32

    while num != 0:
        digit = num % 10
        octalDigit += digit * pow(2, i)
        i += 1
        num //= 10

        # placing current octal-sum for 3 pair in array index position
        octalArray[pos] = octalDigit

        # whenever we have read next 3 digits
        # setting values to default
        # increasing pos so next values can be placed at next array index
        if count % 3 == 0:
            octalDigit = 0
            i = 0
            pos += 1

        count += 1

    # printing octal array in reverse order
    for j in range(pos, -1, -1):
        print(octalArray[j], end='')


binary = int(input("Enter the binary number: ")) #try to enter 10101111 (257) and 1100110 (146)
convert(binary)