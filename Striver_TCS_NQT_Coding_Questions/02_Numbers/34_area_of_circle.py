'''
Problem Statement: Given the radius of the circle, calculate the area of the circle.

Examples:

Example 1:
Input: N = 5
Output: 78.5
Explanation: Using formula  πr2 for finding area of circle we get area as 78.5

Example 2:
Input: N = 4
Output: 50.2
Explanation: Using formula  πr2 for finding area of circle we get area as 50.2
'''

class Area:
    def areaOfCircle(self, n):
        ans = 3.14 * n * n # Area of circle = πr2
        print("Area of circle is : ", ans)

n = 5
p1 = Area()
p1.areaOfCircle(n)
