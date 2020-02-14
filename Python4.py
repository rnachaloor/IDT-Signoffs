"""
Name: Rohit Nachaloor
Date: 01/14/2019
Assignment: Python No. 4
Period: 1
Cowart
"""
#These are some games I play. 
x = 'Paladins'
y = 'Overwatch'
z = 'Fortnite'

print(x)
print(y)
print(z)

gameList = [x, y, z,]

print(gameList)

'''
The new variable doesn't have a game set to it, but instead it is an input function.
This allows me to add a different game every time I run the program.
'''

new = input()
gameList.append(new)
del gameList[2]

print(gameList)

#these are the controllers that I own.
myControllers= ('WiiMote', 'Xbox 360 Remote', 'Dualshock')

print(myControllers)
