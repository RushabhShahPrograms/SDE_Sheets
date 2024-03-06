'''
Print all the armstrong numbers in the range of 100 to 1000
'''

for num in range(100,1001):
    order = len(str(num))
    sum = 0
    temp = num
    while temp>0:
        digit = temp%10
        sum += digit ** order
        temp //= 10
    if num==sum:
        print(num)