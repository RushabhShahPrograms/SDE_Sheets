'''
Find the 15th term of the series?
0,0,7,6,14,12,21,18, 28
Explanation :
In this series the odd term is increment of 7 {0, 7, 14, 21, 28, 35 – – – – – – }
And even term is a increment of 6 {0, 6, 12, 18, 24, 30 – – – – – – } 
'''

num = int(input('enter the number: '))
a=0
b=0

for i in range(1,num+1):
    if(i%2!=0):
        a= a+7
    else:
        b = b+6

if(num%2!=0):
    print(' {} term of series is {}'.format(num,a-7))
else:
    print('{} term of series is {}'.format(num,b-6))