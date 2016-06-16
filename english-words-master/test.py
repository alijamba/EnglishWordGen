import itertools
from string import ascii_lowercase

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
		   'v', 'w', 'x', 'y', 'z']
# keywords = itertools.product(alphabets, repeat = 2)
repeat_range = int(input("Enter the range or length of the specific combination "))
file_writer = open('non_letter.txt', 'w')  # a text file which will be used to generate the words!
listofvowels = ['a', 'e', 'i', 'o', 'u']
resultlist = list()
for combination in itertools.product(ascii_lowercase, repeat=repeat_range):
	combination = str(combination).replace('(', '')
	combination = str(combination).replace(')', '')
	combination = str(combination).replace(',', '')
	combination = str(combination).replace("'", '')
	combination = str(combination).replace(' ', '')
	valid = False
	stateValid = None
	if str(combination).__contains__('a') or str(combination).__contains__('e') or str(combination).__contains__(
		   'i') or str(combination).__contains__('o') or str(combination).__contains__(
		'u'):  # check that the combination of the word has atleast one vowel
		check = 0
		for i in range(len(combination)):  # looping through each character
			# print (i)
			#print (type(combination[i]))
			if combination[i] in listofvowels:
				if (check > 0) and (check <= 2):
					check = 0
					valid = True
					stateValid = True
				elif check > 2:
					valid = False
					stateValid = False
					break
			elif combination[i] not in listofvowels:
				if check > 2:
					valid = False
					stateValid = False
					break
				check += 1

		if stateValid and check < 2:
			resultlist.append(combination)
			print(combination)
		else:
			continue


	else:
		continue

print (resultlist)
