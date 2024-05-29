a = 100
area = [[0] * a for _ in range(a)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y +10):
            area[i][j] = 1

res = sum(sum(row) for row in area)
print(res)