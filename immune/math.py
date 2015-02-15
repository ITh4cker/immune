from itertools import combinations

def factorial(number):
	# uses recurssion to find factorial
	if number == 0:
		return 1
	else:
		return number * factorial(number-1)

def total_combinations(number):
	# loops through the number to find total number of combinations
	set_combinations = 0
	for i in xrange(0, number):
		# finds factorials needed for combinations theorem
		i_factorial = factorial(i)
		num_sub_i_factorial = factorial(number-i)
		num_factorial = factorial(number)

		# updates set_combinations with number of combinations in this index
		set_combinations = set_combinations + (num_factorial/(i_factorial*(num_sub_i_factorial)))
	return set_combinations

def total_combinations_array(number_array):
	number_array_len = len(number_array)
	num_array_combinations = total_combinations(number_array_len)

	# loops through the the combinations and uses itertools to find combinations in list
	total_array = []
	for i in xrange(1,num_array_combinations):
		combination = combinations(number_array, i)
		total_array.extend(combination)

	# returns a list of total combinations
	return total_array
