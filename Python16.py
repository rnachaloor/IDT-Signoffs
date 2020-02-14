'''
Name: Rohit Nachaloor
Date: 03/09/2019
Assignment No. 16
Period: 1
Cowart
'''

def main():
    def helper():
        print('What is your "a" value')
        a = int(input())
        print('What is your "b" value')
        b = int(input())
        print('What is your "c" value')
        c = int(input())
        h = (1*b)/(2*a)
        f = (b / 2)*(b / 2)
        k = c - (a*f)
        print('This is your quadratic equation in vertex form')
        print(str(a)+'(x+'+str(h)+')+'+str(k))
        print('This assignment will convert a quadratic from general form to vertex form.')
    def regular():
        helper()
        print('Now, I can perform any exponent function you want.')
        print('Type in your base')
        base = int(input())
        print('Type in the exponent')
        exp = int(input())
        ans = base**exp
        print('This is your answer.')
        print(ans)
    regular()

if (__name__)=='__main__':
    main()
    
