coins = [25, 10, 5, 1]
T = int(input())

for _ in range(T):
    C = int(input())
    result = []
    for coin in coins:
        result.append(C // coin)
        C %= coin
    

    print(*result)

    