'''
Name: Rohit Nachaloor
Date: 03/18/2019
Assignment No. 19
Cowart
Period: 1
'''

def main():
    from quad import intercept
    from quad2 import vertex
    from quad3 import general
    print('Which calculator do you want to use:')
    print('a. General to Intercept Form')
    print('b. General to Vertex Form')
    print('c. Intercept to General')
    ans = input()
    if (ans == 'a'):
        intercept()
    if (ans == 'b'):
        vertex()
    if (ans == 'c'):
        general()

if (__name__ == '__main__'):
    main()


