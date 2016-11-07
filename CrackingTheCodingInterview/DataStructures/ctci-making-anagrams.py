def number_needed(a, b):
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    a_index, b_index = 0, 0
    removals = 0
    while True:
        if a_sorted[a_index] == b_sorted[b_index]:
            a_index += 1
            b_index += 1
        elif a_sorted[a_index] > b_sorted[b_index]:
            b_index += 1
            removals += 1
        else:
            a_index += 1
            removals += 1

        if len(a_sorted) == a_index and len(b_sorted) == b_index:
            return removals
        elif len(a_sorted) == a_index:
            return removals + (len(b) - b_index)
        elif len(b_sorted) == b_index:
            return removals + (len(a) - a_index)



a = input().strip()
b = input().strip()

print(number_needed(a, b))
