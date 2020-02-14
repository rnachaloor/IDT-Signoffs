"""
Name: Rohit Nachaloor
Date: 01/14/2019
Assignment: Python No. 7
Period: 1
Cowart
"""

#First round of Rock Paper Scissors
print('Rock, Paper, Scissors show:')
enter = input()
print('Paper')

#What happens when you win or lose
if enter == 'Scissors':
  print('Congrats, you have won one out of three games.')
  p = 1
else: 
  print('Unfortunately, you have lost this round')
  p = 0

#Second Round of Rock Paper Scissors
print('Rock, Paper, Scissors show:')
enter = input()
print('Rock')

#What happens when you win or lose
if enter == 'Paper':
  print('Congrats, you have won the second round.')
  p = p + 1
else:
  print('Unfortunately, you have lost this round')

#Final Round of Rock Paper Scissors
print('Rock, Paper, Scissors show:')
enter = input()
print('Scissors')

#What happens when you win or lose
if enter == 'Rock':
  print('Congrats, you have won the final round.')
  p = p + 1
else:
  print('Unfortunately, you have lost this round')

#Results of the game
if p == 0:
  print('Unfortunately, you lost all the rounds, therefore you lost the game.')
  
if p == 1:
  print('Unfortunately, you only won one round, therefore you lost the game.')

if p == 2: 
  print('Fortunately, you won two rounds, therefore you won the game.')

if p == 3: 
  print('Fortunately, you won all the rounds, therefore you won the game.')
