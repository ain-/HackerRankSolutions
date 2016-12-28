
n = int(input())
values = list(map(int, input().split()))

values.sort()

mean = sum(values) / len(values)

if len(values) % 2 == 1:
    median = values[len(values) // 2]
else:
    median = (values[len(values) // 2] + values[len(values) // 2 - 1]) / 2

highest_count = 1
current_count = 1
mode = values[0]
for i in range(1, len(values)):
    if values[i] != values[i - 1]:
        current_count = 1
    else:
        current_count += 1
    if current_count > highest_count:
        highest_count = current_count
        mode = values[i]


print("{0:.1f}".format(round(mean, 1)))
print("{0:.1f}".format(round(median, 1)))
print(mode)
