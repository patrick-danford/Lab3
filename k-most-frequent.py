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