# K Most Frequent

"""
Patrick Danford 
Lab 3, K Most Frequent

Given a non-empty array of integers, return the k most frequent elements.
For example, Given [1,1,1,2,2,3] and k = 2, return [1,2]


"""

import operator


def count_numbers(numbers, k = 2):
    counts = {}
    result = []
    for w in numbers:
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1

    for item in sorted(counts.items(), key=operator.itemgetter(1), reverse=True):
        result.append(item[0])

    print(result[:k])



count_numbers([1,2,3,4,5,6,5,4,3])