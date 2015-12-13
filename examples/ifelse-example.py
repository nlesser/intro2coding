age=input('>How old are you? ') #what is wrong with this line of code? Hint: see pages 62-64
age=int(age)
if age < 10:
	print('   You are too young to code!')
elif age > 20:
	print ('   You old fart, this class is for kids!')
else:
	print ('   Nice!')

#Or & And
gender=str(input('>Are you a boy or a girl?'))
print('your a %s' % gender)
if gender == 'boy' or gender=='cow':
	print('   Oh, boy!')
elif gender == 'girl' and age < 20:
	print('   Rocking!  Your our target demo.')
elif gender == 'girl' and age >= 20:
	print('   Don\'t you mean \"woman!\"')
else:
	print('   Really?! What the heck are you?')
