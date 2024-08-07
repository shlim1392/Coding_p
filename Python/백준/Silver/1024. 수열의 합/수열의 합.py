def find_sequence(N, L):
    for l in range(L, 101):
        temp = N - l * (l - 1) // 2
        if temp % l == 0:
            a = temp // l
            if a >= 0:
                return [a + i for i in range(l)]
    return -1


N, L = map(int, input().split())
result = find_sequence(N, L)


if result == -1:
    print(result)
else:
    print(' '.join(map(str, result)))
