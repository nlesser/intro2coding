#demo of python math
#addition
#print("10+12 =",10+12) #adding 10 & 12
#subtraction
#print("1-20=",1-20)
#multiplication
#print("10*10 =",10*10)
#division
#print("100/3 =",100/3)
#why is the divison different?  What if we do this:
#print("100/3 =", int(100/3))

bank = 1000
earnings = 100
#print("This week I earned $%s", str(%mymoney))
message1='This week I earned $%s'
message2='I now have $%s in the bank'
message3='Next week I will earn $%s'
print(message1 %earnings)
#print("This week I earned $", earnings)
#print("I have $",bank+earnings)
bank=bank+earnings
print(message2 %bank)
earnings=int(input("How much will I earn next week?"))
print(message3 %earnings)
bank=bank+earnings
print(message2 %bank)

