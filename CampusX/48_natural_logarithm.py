'''
The natural logarithm can be approximated by the following series.
If x is input through the keyboard, write a program to calculate the
sum of the first seven terms of this series.
'''
import math

x = float(input("Enter the value of x: "))

# Checking if x is positive and not equal to 1, as log(1) is 0 and log for negative numbers is undefined
if x > 0 and x != 1:
    # Calculating the first seven terms of the series
    ln_x_approx = (x - 1)/x - ((x - 1)/x)**2/2 + ((x - 1)/x)**3/3 - ((x - 1)/x)**4/4 + ((x - 1)/x)**5/5 - ((x - 1)/x)**6/6 + ((x - 1)/x)**7/7
    
    print(f"The approximation of ln({int(x)}) using first seven terms of series is {ln_x_approx}")
else:
    print("The value of x should be positive and not equal to one.")
