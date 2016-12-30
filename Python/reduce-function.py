from fractions import Fraction
from functools import reduce


def product(fracs):
    t = reduce(lambda fr1, fr2: fr1 * fr2, fracs)
    return t.numerator, t.denominator

fracs = []
for _ in range(int(input())):
    fracs.append(Fraction(*map(int, input().split())))
result = product(fracs)
print(*result)
