"""
Name: Rohit Nachaloor
Date: 01/14/2019
Assignment: Python No. 6
Period: 1
Cowart
"""
print('Enter F to Convert Fahreinheit to Celcius')
print('Enter C to Convert Celcius to Fahreinheit')
print('Enter I to Convert Inches to Centimeters')
print('Enter CM to Convert Centimeters to Inches')
func = input()

#Fahreinheit to Celcius
if func == 'F':
  print('Enter a Value in Fahreinheit')
  new = input()
  print((5/9)*(int(new)-32))

#Celcius to Fahreinheit
if func == 'C':
  print('Enter a Value in Celcius')
  new = input()
  print((5/9)*int(new)+32)

#Inches to Centimeter
if func == 'I':
  print('Enter a Value in Inches')
  new = input()
  print((2.54) * int(new))

#Inches to Centimeter
if func == 'CM':
  print('Enter a Value in Centimeters')
  new = input()
  print(int(new)/(2.54))


