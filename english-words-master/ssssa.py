import json


def main():
	print ("this is the main program!")
	#file_open_json = open("businesses.json")  # loading the data from the json file
	result_dict = dict()
	categoryname = raw_input("Enter a Category")  # category name input
	categoryname = categoryname.strip()
	cuttoff_value = int(raw_input("Cutoff for displaying categories"))  # displaying category input (specific)
	data = []

	counter = 0
	categoryname_list = []
	with open('businesses.json') as f:  # A json file reader , an easy technique
		for line in f:
			if counter == 0:
				data.append(json.loads(line))
				line = json.loads(line)
				#data.append(json.loads(line))
				categoryname_list.append(line["categories"][0])
				categoryname_list.append(line["categories"][1])
				categoryname_list.append(line["categories"][2])
				categoryname_list.append(line["categories"][3])
				categoryname_list.append(line["categories"][4])
				# print (categoryname_list) this holds all the categories of the stuff
				counter += 1
				continue
			data.append(json.loads(line))
	result_list = list
	if categoryname in categoryname_list:
		for json_data in data:
			if str(json_data["categories"]).__contains__(categoryname):
				for item in json_data["categories"]:
					if item == categoryname:
						continue
					if result_dict.has_key(item):
						result_dict[str(item)] += 1
					else:
						result_dict[str(item)] = 1
		result_dict = (result_dict)
		final_dict = dict()
		for key, value in sorted(result_dict.items(),reverse=True):
			if value >= cuttoff_value:
				print (key,value)
	else:
		print ("InValid category")
		exit()








if __name__ == '__main__':
	main()  # calls the main program of the file.
