a, b = map(int, input().strip().split(' '))
res = ""
for n in range(b):
    for m in range(a):
        res += '*'
    res += '\n'

print(res)