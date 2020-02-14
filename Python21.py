'''
Name: Rohit Nachaloor
Date: 02/21/2019
Assignment No. 21
Period: 1
Cowart
'''

def main():
    import datetime

    today = datetime.datetime.now()

    print('This will show you how many days there are to a certain date')

    print('Please type in the year of your next event')
    yr = int(input())

    print('Please type in the month number (Ex. March = 3)')
    mn = int(input())

    print('Please type in the day')
    day = int(input())

    future = datetime.datetime(int(yr), int(mn), int(day))

    rYr = yr - int(today.strftime("%Y"))

    rMn = mn - int(today.strftime("%m"))

    rDay = day - int(today.strftime("%d"))

    if (rMn < 0):
        rMn = 12 + rMn

    if (rDay < 0):
        rDay = 365 + rDay
    print('This is when your event takes place.')
    print(future.strftime('%x'))
    print('There are '+str(rYr)+' years, '+str(rMn)+' months, and '+str(rDay)+' days until this event')

if (__name__ == '__main__'):
    main()

