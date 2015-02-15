from probability import probability

# Defines sample set to test
sample_set = [1,2,3,4,5,6,7,8,3,2,5,2,6]
# Defines test set to base sample set off of
test_set = [4,2,3]

# Runs probability equation and prints result
probability_set = probability(sample_set, test_set)
print(probability_set)