'''
Name: Rohit Nachaloor
Date: 03/19/2019
Assignment No. 20
Period: 1
Cowart
'''

from eG import expGrowth
from eD import expDecay
from hL import halfLife

def main():
    print('You can pick one of these three calculators to use')
    print('a. Exponential Growth')
    print('b. Exponential Decay')
    print('c. Half-Life')
    q = input()
    if (q == 'a'):
        expGrowth()
    if (q == 'b'):
        expDecay()
    if (q == 'c'):
        halfLife()

if (__name__ == '__main__'):
    main()


