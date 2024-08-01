n = int(input())
numbers = list(map(int, input().split()))

result = []

for i in range(1, n+1):
    result.insert(len(result) - numbers[i-1], i)

print(" ".join(map(str, result)))
