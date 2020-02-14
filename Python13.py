'''
Name: Rohit Nachaloor
Date: 02/21/2019
Assignment No.13
Period: 1
Cowart
'''

print('List 10 things you want for Christmas.')

#I used chimpanzee because it has 10 letters which allows me the loop to and at 10 entries
y = 'chimpanzee'

#The Gift List
gift = []

#The Gift For Loop
for x in y:
    z = input()
    gift.append(z)
    if z == 'Done':
        gift.remove('Done')
        break

#Presentation of Data Collected in the Loop
print('This is what you wished for')
print(gift)

#Amount of Entries in the Shopping List
print('How many thing do you want to enter in the shopping list?')
a = int(input())

#Shopping List
shop = []

#Shopping While Loop
while a > 0:
    b = input()
    shop.append(b)
    a = a - 1
    if b == 'Done':
        shop.remove('Done')
        break

#Presentation of Data Collected in the Loop
print('This is what you need to buy')
print(shop)


