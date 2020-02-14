'''
Name: Rohit Nachaloor
Date: 03/20/2019
Assignment No. 28
Period: 1
Cowart
'''

import math
def main():
    print('This program can calculate the area of a circle')
    print('Please type in the radius')
    r = int(input())
    area = lambda a : math.pi * (a**2)
    ans = area(r)
    print('This is the answer to the problem: '+str(ans))

if (__name__ == '__main__'):
    main()
