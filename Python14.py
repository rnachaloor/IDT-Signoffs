'''
Name: Rohit Nachaloor
Date: 02/21/2019
Assignment No. 14
Period: 1
Cowart
'''

#List of complaints and variable that counts complaints)
comp = []
numComp = 0

print('Give the following Airlines a rating between 1-5.')

#Delta Review
print('Delta')
th = int(input())
if th > 3:
    print('Ok thanks')
else:
    print('State your complaint')
    comp1 = input()
    comp.append(comp1)
    print('Ok thanks')
    numComp = numComp + 1

#United Review
print('United')
th = int(input())
if th > 3:
    print('Ok thanks')
else:
    print('State your complaint')
    comp1 = input()
    print('Ok thanks')
    numComp = numComp + 1
    comp.append(comp1)

#American Review
print('American')
th = int(input())
if th > 3:
    print('Ok thanks')
else:
    print('State your complaint')
    comp1 = input()
    print('Ok thanks')
    numComp = numComp + 1
    comp.append(comp1)

#Southwest Review
print('Southwest')
th = int(input())
if th > 3:
    print('Ok thanks')
else:
    print('State your complaint')
    comp1 = input()
    print('Ok thanks')
    numComp = numComp + 1
    comp.append(comp1)

#What happens when there is no complaints
if numComp == 0:
    comp.append('None')

#Presenting list of complaints
print('Here is a list of your complaints')
print(comp)
    


