def is_matched(expression):
    open_brac_surplus = {'(': 0, '[': 0, '{': 0}
    history = []
    for c in expression:
        if c == '(' or c == '[' or c == '{':
            open_brac_surplus[c] += 1
            history.append(c)
        else:
            complement = get_complement(c)
            if open_brac_surplus[complement] <= 0:
                return False
            else:
                prev_open = history.pop() if len(history) > 0 else None
                if complement != prev_open:
                    return False
                open_brac_surplus[complement] -= 1
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
