'Create a function that takes a list of non-negative numbers / strings and returns a new list without the strings.'

def filter_list(lst):
	num = []
	for i in lst:
		if not isinstance(i,str):
			num.append(i)
	return num
