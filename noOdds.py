'Create a function that takes a list of numbers and returns only the even values.'

def noOdds(lst):
	even = [num for num in lst if num%2==0]
	return even
