def solution(n):
    max_score = 0  

    for _ in range(n):
        a, d, g = map(int, input().split())
        if a == (d + g):
            score = (a * (d + g)) * 2
        else:
            score = a * (d + g)
        max_score = max(max_score, score)  

    return max_score

n = int(input())
print(solution(n))
