from functools import reduce

n = int(input())
values = list(map(int, input().split()))
weights = list(map(int, input().split()))


def weighted_mean(values, weights):
    zipped = list(zip(values, weights))
    #numerator = reduce(lambda x, y: x[0] * x[1] + y[0] * y[1], zipped)
    numerator = 0
    for value, weight in zipped:
        numerator += value * weight
    return numerator / sum(weights)

print("{0:.1f}".format(round(weighted_mean(values, weights), 1)))
