'''
Name: Rohit Nachaloor
Date: 02/18/2019
Period: 1
Cowart
'''
#5 Day high temperatures
fiveHigh=(43,44,61,61,62)
print(fiveHigh)

#Same as previous but in list form
editHigh=[fiveHigh[0],fiveHigh[1],fiveHigh[2],fiveHigh[3],fiveHigh[4]]
print(editHigh)

#This converts Celcius to Fahreinheit
tuesdayHigh=(fiveHigh[0] - 32) * (5 / 9)
wedHigh=(fiveHigh[1] - 32) * (5 / 9)
thursHigh=(fiveHigh[2] - 32) * (5 / 9)
friHigh=(fiveHigh[3] - 32) * (5 / 9)
satHigh=(fiveHigh[4] - 32) * (5 / 9)

#Putting my data in a string.
print('Today, the temperature will reach a high of '+str(fiveHigh[0])+' degrees fahrenheit or '+str(round(tuesdayHigh))+' degrees celcius.')
print('Tommorow, the temperature will reach a high of '+str(fiveHigh[1])+' degrees fahrenheit or '+str(round(wedHigh))+' degrees celcius.')
print('On Thursday, the temperature will reach a high of '+str(fiveHigh[2])+' degrees fahrenheit or '+str(round(thursHigh))+' degrees celcius.')
print('On Friday, the temperature will reach a high of '+str(fiveHigh[3])+' degrees fahrenheit or '+str(round(friHigh))+' degrees celcius.')
print('On Saturday, the temperature will reach a high of '+str(fiveHigh[4])+' degrees fahrenheit or '+str(round(satHigh))+' degrees celcius.')


