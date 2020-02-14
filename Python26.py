'''
Name: Rohit Nachaloor
Date: 03/18/2019
Assignment No. 26
Period: 1
Cowart
'''

def main():

    print('This will calculate the sum, average, smallest and largest numbers in a set.')
    print('How many numbers do you want to use for the calculations. Type Done when finished.')
    num = int(input())
    number = num
    numList = []

    while num > 0:
        z = int(input())
        numList.append(z)
        num = num - 1
        if (z == 'Done'):
            numList.remove('Done')

    Sum = sum(numList)
    Average = Sum / number
    Min = min(numList)
    Max = max(numList)

    print('This is the sum of all the numbers: '+str(Sum))
    print('This is the average of all the numbers: '+str(Average))
    print('This is the smallest of all the numbers: '+str(Min))
    print('This is the largest of all the numbers: '+str(Max
                                                         ))

if (__name__ == '__main__'):
    main()
