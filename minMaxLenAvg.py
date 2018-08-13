'Create a function that takes a list of numbers and returns the following statistics Minimum Value Maximum Value Sequence Length Average Value'

from functools import reduce
def minMaxLengthAverage(lst):
	avg= reduce(lambda x, y: x + y, lst) / len(lst)
	temp = [min(lst), max(lst),len(lst), avg]
	return temp
