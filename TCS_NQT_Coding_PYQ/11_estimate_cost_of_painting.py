'''
Problem Statement

We want to estimate the cost of painting a property. Interior wall painting cost is Rs.18 per sq.ft. and exterior wall painting cost is Rs.12 per sq.ft.

Take input as
1. Number of Interior walls
2. Number of Exterior walls
3. Surface Area of each Interior 4. Wall in units of square feet
Surface Area of each Exterior Wall in units of square feet

If a user enters zero  as the number of walls then skip Surface area values as User may don’t  want to paint that wall.

Calculate and display the total cost of painting the property
Example 1:
6
3
12.3
15.2
12.3
15.2
12.3
15.2
10.10
10.10
10.00
Total estimated Cost : 1847.4 INR
Note: Follow in input and output format as given in above example
'''

ni, ne = map(int, input().split())
int_p = 18
ext_p = 12
cost = 0

if ni < 0 or ne < 0:
    print("INVALID INPUT")
elif ni == 0 and ne == 0:
    print("Total estimated Cost : 0.0")
else:
    for i in range(ni):
        temp = float(input())
        cost += int_p * temp
    for i in range(ne):
        temp = float(input())
        cost += ext_p * temp
    print(f"Total estimated Cost : {cost:.1f}")
