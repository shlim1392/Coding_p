n, m = map(int, input().split())
num =list(range(1,n+1))
for _ in range(m):
    i, j = map(int, input().split())
    num[i-1:j] = reversed(num[i-1:j])
print(' '.join(map(str, num)))