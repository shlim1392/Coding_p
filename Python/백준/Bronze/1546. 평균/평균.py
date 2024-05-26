n = int(input())
score = list(map(int, input().split()))
res = []
M = max(score)
for x in score:
    new = x / M * 100
    res.append(new)
print(sum(res)/n)