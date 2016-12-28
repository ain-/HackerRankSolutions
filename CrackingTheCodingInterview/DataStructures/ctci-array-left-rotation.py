def array_left_rotation(a, n, d):
    first_half = a[d:n]
    second_half = a[0:d]
    return first_half + second_half

n, d = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, d)
print(*answer, sep=' ')