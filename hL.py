def halfLife():
    print('Please enter the initial value.')
    Ao = int(input())
    print('Please enter the half-life')
    half = int(input())
    print('Please enter the time')
    time = int(input())
    ans = Ao * ((0.5)**(time / half))
    print('The answer to the problem is: '+str(ans))


