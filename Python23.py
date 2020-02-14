'''
Name: Rohit Nachaloor
Date: 03/18/2019
Assignment No. 23
Cowart
Period 1
'''

def main():
    try:
        txt = open('D:\\Python23.txt', 'r')
        print(txt.read(5))
        print(txt.readline(3))
        print(txt.read())
    except:
        print('You made a mistake')

if (__name__ == '__main__'):
    main()



