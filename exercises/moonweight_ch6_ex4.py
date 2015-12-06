# ch3, exercise 4
weightLbs=int(input('what is your weight in pounds?'))
weightKgs=weightLbs/2.2
moonweight=weightKgs*0.165
print('Your weight in kilograms is:', weightKgs)
print('Your weight on the moon is:', moonweight,'kg')

for x in range(0,15):
	moonweight=moonweight+0.165
	print('after',x+1,'years your weight on the moon will be:',moonweight,'kg')
exit()