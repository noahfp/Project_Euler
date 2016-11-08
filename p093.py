from itertools import combinations as subsets 
import numpy as np
from fractions import Fraction

combinations = [lambda a,b : a+b, 
				lambda a,b : abs(a-b),
				lambda a,b : a*b, 
				lambda a,b : a/b if b != 0 else np.nan, # When division fails, carry forward with NaN
				lambda a,b : b/a if a != 0 else np.nan
				]

class tree:
	def __init__(self, nums):
		self.nums = nums
		# Our initial operations just return the input values of our array
		self.operations = [lambda x, i=i: Fraction(x[i]) for i in xrange(nums)]
		# self.primes_list = [13093, 32086489, 141654797, 275634551]
		self.make_operations()


	# This takes a set of lambda functions and merges a given two of them
	# in all of the allowed ways
	def combine_operations(self, operations, pair):
		other_operations = [operations[i] for i in xrange(len(operations)) if not i in pair]
		l1, l2 = operations[pair[0]], operations[pair[1]]
		possible_merges = [lambda x, l1=l1, l2=l2, l=l: l(l1(x),l2(x)) for l in combinations]
		return [other_operations + [merge] for merge in possible_merges]
		
	# This makes all of the lambda functions allowed by the rules of the game
	def make_operations(self):
		operations_list = [self.operations]
		# We want to apply self.nums-1 combinations to the n operations
		for keep_going_while in xrange(self.nums-1):
			new_operations_list = []
			# For each set of operations, apply each possible combination 
			for operations in operations_list:
				for pair in subsets(xrange(len(operations)),2):
					new_operations_list += self.combine_operations(operations, pair)
			operations_list = new_operations_list
		operations_list = [thing[0] for thing in operations_list]
		self.operations = operations_list

	# Returns possible outputs of numlist through all operations, sorted
	def results(self, numlist):
		return list(set([operation(numlist) for operation in self.operations]))

	def clean_results(self, numlist):
		results = self.results(numlist)
		new_results = [result for result in results if type(result) == Fraction]
		new_results = [result.numerator for result in new_results if result.denominator == 1]
		return sorted(new_results)

	def max_consecutive(self, vals):
		vals.reverse()
		if vals[-1] == 0:
			vals.pop()
		check = 0
		try:
			while vals.pop() == check+1:
				check += 1
		except IndexError:
			pass
		return check

	# Find the inputs that yield all values 1,...,n for maximum n
	def test(self, limit):
		maxx_consec = -1
		for subset in subsets(xrange(1,limit+1),self.nums):
			max_consec = self.max_consecutive(self.clean_results(subset))
			print str(subset) + " : " + str(max_consec)
			if max_consec > maxx_consec:
				maxx_consec = max_consec
				maxx_subset = subset

		print str(maxx_subset) + " : " + str(maxx_consec)






