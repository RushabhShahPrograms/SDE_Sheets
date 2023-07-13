'''
Problem Statement: Given a number, convert it into the form of words.

Note:- Consider maximum no. of digits in the number as 4.

Examples:

Example 1:
Input: 7824
Output: seven thousand eight hundred twenty four
Explanation: 7824 in words can be written as seven thousand eight hundred twenty four.

Example 2:
Input: 370
Output: three hundred seventy
Explanation: 370 in words can be written as three hundred seventy.
'''

def convert_to_words(num):  
    if num == 0:  
        return "zero"  

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]  
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]  
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]  
    words = ""  

    if num>= 1000:  
        words += ones[num // 1000] + " thousand "  
        num %= 1000  
    if num>= 100:  
        words += ones[num // 100] + " hundred "  
        num %= 100  
    if num>= 10 and num<= 19:  
        words += teens[num - 10] + " "  
        num = 0  
    elif num>= 20:  
        words += tens[num // 10] + " "  
        num %= 10  
    if num>= 1 and num<= 9:  
        words += ones[num] + " "


    return words.strip()
  
num = int(input("Enter a number: "))
words = convert_to_words(num)  
print(words)   
