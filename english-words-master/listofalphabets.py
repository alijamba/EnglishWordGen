import itertools
from string import ascii_lowercase

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
		   'v', 'w', 'x', 'y', 'z']
# keywords = itertools.product(alphabets, repeat = 2)
repeat_range = int(input("Enter the range or length of the specific combination "))
file_writer = open('meaninglesswords.txt', 'w') # a text file which will be used to generate the words!
listofvowels = ['a', 'e', 'i', 'o', 'u']
for combination in itertools.product(ascii_lowercase, repeat=repeat_range):
	combination = str(combination).replace('(', '')
	combination = str(combination).replace(')', '')
	combination = str(combination).replace(',', '')
	combination = str(combination).replace("'", '')
	combination = str(combination).replace(' ', '')
	if str(combination).__contains__('a') or str(combination).__contains__('e') or str(combination).__contains__(
		   'i') or str(combination).__contains__('o') or str(combination).__contains__('u'):
		for i in range(len(combination)):
			if combination[0] in listofvowels and combination[-1] in listofvowels: # this checks the last and the first element be vowels
				print (combination)
				break
			elif combination[0] in listofvowels and combination[-1] not in listofvowels: # this checks if the first element is vowel
				print (combination) # prints the combination
				break
			elif combination[0] not in listofvowels and combination[-1] not in listofvowels: #this checks
				if combination[1] not in listofvowels and combination[2] not in listofvowels and combination[3] in listofvowels:
					print (combination)
				elif len(combination) < 5:
					print (combination)
				break

