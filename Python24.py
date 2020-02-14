'''
Name: Rohit Nachaloor
Date: 03/20/2019
Assignment No. 24
Period: 1
Cowart
'''

def main():
    try:
        wTxt = open('D:\\Python24.txt', 'w')
        wTxt.write('Hello World.')
        wTxt.write('\n' + '(Sorry for being boring.)')
        wTxt.close
    finally:
        print('Text file edited')

if (__name__ == '__main__'):
    main()
    
