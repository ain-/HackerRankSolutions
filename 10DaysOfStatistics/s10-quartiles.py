n = int(input())
values = list(map(int, input().split()))
values.sort()


def median(values):
    if len(values) % 2 == 1:
        median = values[len(values) // 2]
    else:
        median = (values[len(values) // 2] + values[len(values) // 2 - 1]) / 2
    return median


print("{:.0f}".format(median(values[:len(values) // 2])))
print("{:.0f}".format(median(values)))
print("{:.0f}".format(median(values[-(len(values) // 2):])))



