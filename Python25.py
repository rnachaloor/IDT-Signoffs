'''
Name: Rohit Nachaloor
Date: 03/18/2019
Assignment No. 25
Period: 1
Cowart
'''

def main():
    print('This is a Pythagorean Theorem calculator')
    print('Are you solving for the hypotenuse or a leg?')
    q = input()
    import math
    try:
        if (q == 'hypotenuse'):
            print('Give me the length of one leg.')
            a = int(input())
            print('Give me the length of the other leg.')
            b = int(input())
            f = lambda d, e : math.sqrt((d**2) + (e**2))
            c = f(a, b)
            print('This is the length of the hypotenuse')
            print(c)
        if (q == 'leg'):
            print('Give me the length of one leg.')
            a = int(input())
            print('Give me the length of the hypotenuse.')
            c = int(input())
            f = lambda d, e : math.sqrt((d**2) - (e**2))
            b = f(c, a)
            print('This is the length of the other leg')
            print(b)
    except:
        print('Sorry. Please try agian.')

if (__name__ == '__main__'):
    main()

