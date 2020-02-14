def intercept():
    print('What is your "a" value')
    a = int(input())
    print('What is your "b" value')
    b = int(input())
    print('What is your "c" value')
    c = int(input())
    import math
    r = math.sqrt((b**2)-(4*a*c))
    p = ((-1 * b)-r)/(2 * a)
    q = ((-1 * b)+r)/(2 * a)
    print('This is your quadratic equation in intercept form')
    print(str(a)+'(x-'+str(p)+')(x-'+str(q)+')')
    
