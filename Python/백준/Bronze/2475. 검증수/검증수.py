n = list(map(int, input().split()))
num = [x ** 2 for x in n ]
res = sum(num) % 10
print(res)