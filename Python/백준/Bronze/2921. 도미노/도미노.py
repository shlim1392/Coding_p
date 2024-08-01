def domino_set_score(N):
    total_score = 0
    for i in range(N + 1):
        for j in range(i, N + 1):
            total_score += i + j
    return total_score

N = int(input().strip())

print(domino_set_score(N))
