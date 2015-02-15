from itertools import combinations

def factorial(number):
	if number == 0:
		return 1
	else:
		return number * factorial(number-1)

def total_combinations(number):
	set_combinations = 0
	for i in xrange(0, number):
		i_factorial = factorial(i)
		num_sub_i_factorial = factorial(number-i)
		num_factorial = factorial(number)
		set_combinations = set_combinations + (num_factorial/(i_factorial*(num_sub_i_factorial)))
	return set_combinations

def total_combinations_array(number_array):
	number_array_len = len(number_array)
	total_array = []
	for i in xrange(1,total_combinations(number_array_len)):
		combination = combinations(number_array, i)
		total_array.extend(combination)
	return total_array
