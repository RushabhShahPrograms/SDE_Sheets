'''
Given an array of integers where every element appears even number of times except one element which appears odd number of times, write a program to find that odd occurring element in O(log n) time. The equal elements must appear in pairs in the array but there cannot be more than two consecutive occurrences of an element. 

For example : 

3 

2 3 2 

It doesn't have equal elements appear in pairs 

7 

1 1 2 2 2 3 3 

It contains three consecutive instances of an element. 

5 

2 2 3 1 1 

It is valid and the odd occurring element present in it is 3. 

Enter only valid inputs. 

Sample Input : 

5 

2 2 3 1 1 

Sample Output : 

3
'''

n = int(input())
a = list(map(int,input().split()))
left=0
right=n-1
if a[0] != a[1]:
    print(a[0])
elif a[n-1] != a[n-2]:
    print(a[n-1])

else:
    while left <= right:
        mid = ((right-left)//2)+left
        pre = mid-1
        nxt = mid+1

        if (a[pre] != a[mid])  and (a[nxt] != a[mid]):
            print(a[mid])
            break

        elif mid%2==0 :
            if a[pre] == a[mid] :
                right = mid - 1

            else :
                left = mid + 1

        else :
            if a[pre] == a[mid] :
                left = mid + 1

            else :
                right = mid - 1