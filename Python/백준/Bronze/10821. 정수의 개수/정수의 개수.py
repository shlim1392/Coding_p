def count_integers(S):
    integers = S.split(',')
    return len(integers)


S = input().strip()

print(count_integers(S))
