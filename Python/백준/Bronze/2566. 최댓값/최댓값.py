m = []
for _ in range(9):
    a = list(map(int, input().split()))
    m.append(a)

max_value = m[0][0]
max_row = 0
max_col = 0

for i in range(9):
    for j in range(9):
        if m[i][j] > max_value:
            max_value = m[i][j]
            max_row = i
            max_col = j


print(max_value)
print(max_row + 1, max_col + 1)
