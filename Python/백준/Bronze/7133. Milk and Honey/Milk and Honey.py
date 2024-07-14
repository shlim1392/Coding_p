def calculate_happiness(initial_happiness, decrement, count):
    total_happiness = 0
    current_happiness = initial_happiness
    for i in range(count):
        if current_happiness > 0:
            total_happiness += current_happiness
            current_happiness -= decrement
        else:
            break
    return total_happiness

def max_happiness(M, D_M, H, D_H, fields):
    N = len(fields)
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        C, B = fields[i - 1]
        milk_happiness = calculate_happiness(M, D_M, C)
        honey_happiness = calculate_happiness(H, D_H, B)
        dp[i] = max(dp[i - 1] + milk_happiness, dp[i - 1] + honey_happiness)

    return dp[N]


M, D_M = map(int, input().split())
H, D_H = map(int, input().split())
N = int(input())
fields = [tuple(map(int, input().split())) for _ in range(N)]

result = max_happiness(M, D_M, H, D_H, fields)
print(result)
