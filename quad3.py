def general():
    print('What is your "p" value')
    p = int(input())
    print('What is your "q" value')
    q = int(input())
    b = (-1 * p) + (-1 * q)
    c = (-1 * p) * (-1 * q)
    print('This is your equation.')
    print('x^2+'+str(b)+'x+'+str(c))

