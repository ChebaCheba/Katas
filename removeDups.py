'Create a function that takes a list of items, removes all duplicate items and returns a new list in the same sequential order as the old list (minus duplicates).'

def removeDups(lst):
	dup = [x for n, x in enumerate(lst) if x not in lst[:n]]
	return dup
