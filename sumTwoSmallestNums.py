'Create a function that takes a list of numbers and returns the sum of the two lowest positive numbers.'

def sum_two_smallest_nums(lst):
	nonNeg = list(filter(lambda x: x > 0, lst))
	minim = min(nonNeg)
	nonNeg.remove(minim)
	return minim + min(nonNeg)
