'''
Name: Rohit Nachaloor
Date: 02/21/2019
Assignment No. 11
Period: 1
Cowart
'''

#This is my set
classes = {'IDT', 'Math', 'Science'}
print(classes)

#I am adding things to my set
classes.add('Spanish')
print(classes)
classes.update(['Government', 'LA'])
print(classes)

#I am letting the user add things to the class
print('Do you have a class to add? If so, what is it?')
ans = input()
if ans == 'No':
  print('Good. Thank You.')
else:
  print('Thanks.')
  classes.add(ans)
  print(classes)

pokemon = {
  "name": "Trubbish",
  "region": "Unova",
  "type": "Poison",
  "abilities": "Sticky Hold"
}

x = pokemon.get('name')
y = pokemon.get('abilities')
z = pokemon.get('type')
w = pokemon.get('region')
print(x)
print(y)
print(z)
print(w)

print('Wanna change the ablities? If so, please state it?')
ans = input()
if ans == 'No':
  print('Ok. Good.')
else:
  pokemon['abilities'] = ans
  print(pokemon)
