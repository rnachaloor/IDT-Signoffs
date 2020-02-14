'''
Name: Rohit Nachaloor
Date: 03/19/2019
Assignment No. 27
Period: 1
Cowart
'''

def main():
    print('This is a exponential growth calculator')
    print('Please enter the initial value.')
    Ao = int(input())
    print('Please enter the rate of change(%)')
    pRate = int(input())
    rate = (pRate / 100) + 1
    print('Please enter the time')
    time = int(input())
    expGrow = lambda a, b, c : a * (b**c)
    ans = expGrow(Ao, rate, time)
    print('The answer to the problem is: '+str(ans))

if (__name__ == '__main__'):
    main()



