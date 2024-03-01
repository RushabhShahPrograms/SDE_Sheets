'''
 Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.
'''

PI = 3.14
radius = float(input('Please enter the radius of the cylinder: '))
height = float(input('Please enter the height of the cylinder: '))

volume = PI * radius**2 * height
print(f'The volume of the cylinder is approximately {volume:.2f} cubic units.')

cost_per_liter = 40
total_cost = volume * cost_per_liter
print(f'The cost for the given volume of milk is ₹{total_cost:.2f}')
