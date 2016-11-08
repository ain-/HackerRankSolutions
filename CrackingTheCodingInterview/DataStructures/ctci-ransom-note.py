from collections import Counter


def ransom_note(magazine, ransom):
    magazine_counts = Counter(magazine)
    ransom_counts = Counter(ransom)
    for key in ransom_counts:
        magazine_words = magazine_counts[key]
        if magazine_words is None or magazine_words < ransom_counts[key]:
            return False
    return True


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print("Yes")
else:
    print("No")
