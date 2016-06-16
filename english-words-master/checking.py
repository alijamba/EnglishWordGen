import itertools

items = 'abcdefghijklmnopqrst'
for i in range(len(items)+1):
    for combination in itertools.combinations('abcd', i):
        combination = str(combination).replace('(', '')
        combination = str(combination).replace(')', '')
        combination = str(combination).replace(',', '')
        combination = str(combination).replace("'", '')
        combination = str(combination).replace(' ', '')
        if str(combination).__contains__('a') or str(combination).__contains__('e') or str(combination).__contains__('i') or str(combination).__contains__('o') or str(combination).__contains__('u'):
            print (combination)