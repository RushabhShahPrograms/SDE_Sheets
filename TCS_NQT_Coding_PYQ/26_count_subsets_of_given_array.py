'''
Given an array of integers and a sum, the task is to count all subsets of given array with sum equal to given sum. 
Input :  

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the array. The next line contains n space separated integers forming the array. The last line contains the sum. 

Output : 

Count all the subsets of given array with sum equal to given sum. 

NOTE: Since result can be very large, print the value modulo 109+7. 

Constraints : 

1<=T<=100 

1<=n<=103 

1<=a[i]<=103 

1<=sum<=103 

Example : 

Input : 

2 

6 

2 3 5 6 8 10 

10 

5 

1 2 3 4 5 

10 

Output : 

3 

3 

Explanation : 

Testcase 1: possible subsets : (2,3,5) , (2,8) and (10) 

Testcase 2: possible subsets : (1,2,3,4) , (2,3,5) and (1,4,5)
'''

def printBool(n, length):
    while n:
        if n & 1:
            print(1, end="")
        else:
            print(0, end="")
        n >>= 1
        length -= 1

    while length:
        print(0, end="")
        length -= 1

    print()

def printSubsetsCount(arr, n, val):
    count = 0
    for i in range(1 << n):
        s = 0
        for j in range(n):
            if i & (1 << j):
                s += arr[j]
        if s == val:
            count += 1

    if count == 0:
        print("No subset is found")
    else:
        print(count)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    val = int(input())
    printSubsetsCount(arr, n, val)
