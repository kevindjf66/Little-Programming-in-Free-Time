'''
make a fibonacci sequence
'''

#way 1: recursion
def fib1(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return (fib1(n-1) + fib1(n-2))

#way 2: loop!
def fib2(n):
    a = 0
    b = 1
    for i in range(n-1):
        a, b = b, a + b
    print a
    
#way 3:
