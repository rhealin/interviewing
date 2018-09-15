## Problem
# Given an array of unique integers, determine the minimum absolute difference
# between any two elements. Print all element pairs with that minimal absolute
# difference in ascending order.

# For example, numbers = [6, 2, 4, 10]. The minimal absolute difference is 2.
# Pairs with that difference are (2, 4) and (4, 6). If a pair's elements are (i, j),
# they are listed in ascending order, ordered first by i and then by j.

from operator import itemgetter

# Complete the closestNumbers function below.
def closestNumbers(numbers):
    sorted_numbers = sorted(numbers)
    min_diff = float('inf')
    pairs = []
    
    for i in range(len(sorted_numbers)-1):
        diff = abs(sorted_numbers[i]-sorted_numbers[i+1])
        if diff < min_diff:
            min_diff = diff
            pairs = []
        if diff == min_diff:
            pairs.append(sorted([sorted_numbers[i], sorted_numbers[i+1]]))
    for pair in sorted(pairs, key=itemgetter(0, 1)):
        print("{} {}".format(pair[0], pair[1]))
            