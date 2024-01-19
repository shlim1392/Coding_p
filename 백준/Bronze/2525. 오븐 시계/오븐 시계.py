h, m = map(int, input().split())
c = int(input())

if m + c >= 60:
    h += (m + c) // 60
    m = (m + c) % 60
else:
    m += c

if h >= 24:
    h %= 24

print(h, m)