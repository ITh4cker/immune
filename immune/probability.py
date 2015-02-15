from math import factorial, total_combinations, total_combinations_array

def probability(set, test_set):
	len_set = len(set)
	len_test_set = len(test_set)

	set_combinations = total_combinations(len_set)
	test_set_combinations = total_combinations(len_test_set)
	total_matches = 0

	set_combinations_array = total_combinations_array(set)
	test_set_combinations_array = total_combinations_array(test_set)

	for i in xrange(0,set_combinations):
		for x in xrange(0,test_set_combinations):
			if set_combinations_array[i] == test_set_combinations_array[x]:
				total_matches += 1

	return total_matches/float(test_set_combinations)