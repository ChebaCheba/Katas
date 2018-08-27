'Create a function that takes a list of numbers and returns a list where each number is the sum of itself + all previous numbers in the list.'

from itertools import accumulate
import operator

def cumulative_sum(lst):
	return list(accumulate(lst, operator.add))
