#build a hangman game
import random
import sys
import os
#hangman
hangman= ['\
\n        ----\
\n       |    |\
\n       |     \
\n       |      \
\n       |      \
\n       |      \
\n       |      \
\n     --+--','\
\n        ----\
\n       |    |\
\n       |    O \
\n       |      \
\n       |      \
\n       |      \
\n       |      \
\n     --+--','\
\n        ----\
\n       |    |\
\n       |    O \
\n       |    |  \
\n       |      \
\n       |      \
\n       |      \
\n     --+--','\
\n        ----\
\n       |    |\
\n       |    O \
\n       |   /|  \
\n       |      \
\n       |      \
\n       |      \
\n     --+--','\
\n        ----\
\n       |    |\
\n       |    O \
\n       |   /|\\\
\n       |    \
\n       |      \
\n       |\
\n     --+--','\
\n        ----\
\n       |    |\
\n       |    O \
\n       |   /|\\\
\n       |    |\
\n       |      \
\n       |\
\n     --+--','\
\n        ----\
\n       |    |\
\n       |    O \
\n       |   /|\\\
\n       |    |\
\n       |   /   \
\n       |\
\n     --+--','\
\n        ----\
\n       |    |\
\n       |    O \
\n       |   /|\\\
\n       |    |\
\n       |   / \\\
\n       |\
\n     --+--']

#set some global variables
failcount=0
badList=[] #incorrect letters guessed
guess='' #word so far

#set clear command
opsys=sys.platform
if opsys == 'darwin':
	clearCMD = 'clear'
elif opsys == 'linux':
	clearCMD = 'clear'
else:
	clearCMD = 'cls'
	

print(clearCMD)
#clear screen
os.system(clearCMD)

#statup sequence
start = input ('\ndo you want to play hangman? (y/n)')
if start != 'y':
	exit()
#get words from a dictionary
# if 'darwin' default to : /usr/share/dict/words
if opsys == 'darwin':
	dictpath='/usr/share/dict/words'
else:
	dictpath=input('please enter the full location of your dictionary file: ')
with open(dictpath,'r') as dictF:
	dictionary_construct=dictF.read()
	dictionary=dictionary_construct.splitlines()

#choose a random word
word=random.choice(dictionary)
length=len(word)
result=('-')*length
resultList=list(result)

os.system(clearCMD)

while (failcount < 8) and (result != word):
	#clear screen
	#os.system(clearCMD)
	#print hangman 
	print(hangman[failcount])
	#print result
	print('The word is',end=" ")
	print(result)
	#print letters guessed (badList)
	if guess != '':
		print('incorrect letters guessed:', str.join('',badList))

	guess = input('enter a letter:')
	if guess[0] in badList:
		os.system(clearCMD)
		print("you guessed ",guess[0], " already!")
	elif guess[0] in result: 
		os.system(clearCMD)
		print("you guessed ",guess[0], " already!")
	elif guess[0] in word:
		os.system(clearCMD) 
		print("\nway to go!\n")
		#update result
		for i in range(len(word)):
			if guess[0] == word[i]:
				resultList[i]=guess[0]
				result=str.join('',resultList)
	else:
		os.system(clearCMD)
		print("oops. ",guess," isn't in there.\ntry again.")
		badList.append(guess)
		badList.append(',')
		failcount+=1
if (result == word):
	print('the answer was:', word)
	print('you win!')
else:
	os.system(clearCMD)
	print('sorry!', 'the answer was: ',word)
	print ('you loose.')
exit()




