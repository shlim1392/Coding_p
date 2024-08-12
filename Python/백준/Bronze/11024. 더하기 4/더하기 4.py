T = int(input())

for _ in range(T):
    numbers = list(map(int, input().split()))
    print(sum(numbers))
