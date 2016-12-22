def is_matched(expression):
    history = []
    for c in expression:
        if c in "([{":
            history.append(c)
        else:
            complement = get_complement(c)
            prev_open = history.pop() if len(history) > 0 else None
            if complement != prev_open:
                return False
    return len(history) == 0


def get_complement(c):
    return {
        ')': '(',
        ']': '[',
        '}': '{',
    }[c]


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression):
        print("YES")
    else:
        print("NO")
