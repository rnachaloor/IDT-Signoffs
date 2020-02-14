def expGrowth():
    print('Please enter the initial value.')
    Ao = int(input())
    print('Please enter the rate of change(%)')
    rate = int(input())
    print('Please enter the time')
    time = int(input())
    ans = Ao * (((rate / 100) + 1)**time)
    print('The answer to the problem is: '+str(ans))



