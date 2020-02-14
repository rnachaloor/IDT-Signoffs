'''
Name: Rohit Nachaloor
Date: 02/21/2019
Period: 1
Cowart
'''

#This is my list of cricket teams.
ipl_cricket = ['Chennai Super Kings', 'Mumbai Indians', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad', 'Rajastan Royals']
print(ipl_cricket)
print('There are '+str(len(ipl_cricket))+' teams in my list.')

#I added a team to the list
ipl_cricket.append('Kolkata Knight Riders')
print('Now, there are '+str(len(ipl_cricket))+' teams in my list.')
print(ipl_cricket)

#This is another list of cricket teams. 
icc_cricket = ['India', 'Pakistan', 'West Indies', 'England', 'South Africa']
icc_cricket.remove('South Africa')
print(icc_cricket)

#This combines both the list.
ipl_cricket.extend(icc_cricket)
print(ipl_cricket)

#This is my tuple of my favorite ice cream flavors
ice_creams = ('Strawberry', 'Chocolate', 'Cookies and Cream', 'Mint Choc. Chip')
print('Do you think Vanilla is in this tuple? Y/N')
ans = input()
if ans == 'Y':
    print('NOOOOOOOOOO!!!! I HATE Vanilla.')
else:
    print('Good. You know that vanilla sucks')

