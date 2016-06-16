import random


def read_from_file():
	read_file = open('words.txt', 'r')
	data = read_file.readlines()
	read_file.close()
	return data


def list_generator(data):
	wordlist = list()
	for i in data:
		i = str(i).strip()
		wordlist.append(i)
	print ('Wordlist generated!')
	return wordlist


def RandomSelector(size, wordlist):
	counter = 0
	randomdatalist = list()
	random_indexes = list()
	while counter < int(size):
		randomlist_index = random.randint(0, len(wordlist))
		random_indexes.append(randomlist_index)
		counter += 1
	return random_indexes


def wordcheck(wordinput):
	if str(wordinput) in wordlist:
		print ('A valid word ! :) ')
	else:
		print ('The word is invalid ! :) ')


def randomwordreturn(randomnumbers):
	resultset = list()
	counter = 0
	for i in randomnumbers:
		resultset.append(wordlist[int(i)])
	return  resultset

def main():
	data = read_from_file()
	global wordlist
	wordlist = list_generator(data)
	inputcheck = input('Do you want random words ? Y/y or N/n')
	if inputcheck in ['Y', 'y']:
		sizewords = int(input('How many words ?'))
		randomnumbers  = RandomSelector(sizewords, wordlist)
		randomword_generated = randomwordreturn(randomnumbers)
		print ('Random words are : :)')
		for i in randomword_generated:
			print (i)
	elif inputcheck in ['N', 'n']:
		print ('Exiting the program!')
		exit()

	else:
		print ('Invalid input !!! :/')


if __name__ == '__main__':
	main()
