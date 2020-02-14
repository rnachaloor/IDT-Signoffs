'''
Name: Rohit Nachaloor
Date: 03/18/2019
Assignment No. 22
Period: 1
Cowart
'''

def main():

    import math
    x = math.sqrt(9)
    try:
        print(x**2)
    except:
        print('OOOOOF! You screwed up man.')
    else:
        print('Statment ran smoothly.')
    finally:
        print('This test is finished.')

    try:
        print(y)
    except NameError:
        print('OOOOF! Check your names.')
    except:
        print('OOOOF! Check for some mistakes.')
    else:
        print('Statment ran smoothly.')
    finally:
        print('This test is finished.')

if (__name__ == '__main__'):
    main()

