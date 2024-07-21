from itertools import combinations


heights = []
for _ in range(9):
    heights.append(int(input().strip()))


combi = combinations(heights, 7)


for c in combi:
    if sum(c) == 100:
        result = sorted(c)
        break


for height in result:
    print(height)
