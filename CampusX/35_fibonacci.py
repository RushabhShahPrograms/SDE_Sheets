'''
Print the first 20 numbers of a Fibonacci series
'''

def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        print(a)
        a,b = b,a+b

fibonacci(20)