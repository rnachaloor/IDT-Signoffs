'''
Name:Rohit Nachaloor
Date: 03/05/2019
Assignment No. 15
Period: 1
Cowart
'''

def quad():
    print('Hello')
    print('This is a quadratic formula solver that inputs values in the y= ax^2 + bx + c')
    print('Please input your "a" value')
    a = int(input())
    print('Please input your "b" value')
    b = int(input())
    print('Please input your "c" value')
    c = int(input())
    import math
    out1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
    out2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
    print('These are your values')
    print(out1)
    print(out2)

def main():
    quad()
if (__name__=='__main__'):
    main()
