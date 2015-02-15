from math import total_combinations_array

def probability(set, test_set):
	# stores length of set and test_set
	len_set = len(set)
	len_test_set = len(test_set)

	# stores array of all combinations of set and test_set
	set_combinations_array = total_combinations_array(set)
	test_set_combinations_array = total_combinations_array(test_set)

	# calculates the total combinations for set and test_set
	set_combinations = len(set_combinations_array)
	test_set_combinations = len(test_set_combinations_array)

	# loops through set and test_set to see if anything matches
	total_matches = 0
	for i in xrange(0,set_combinations):
		for x in xrange(0,test_set_combinations):
			if set_combinations_array[i] == test_set_combinations_array[x]:
				total_matches += 1

	# returns the probability of set being inside test_set
	return total_matches/float(test_set_combinations)