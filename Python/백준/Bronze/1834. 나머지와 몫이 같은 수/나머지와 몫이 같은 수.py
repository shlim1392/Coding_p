def sum_of_numbers(N):
    total_sum = 0
    for k in range(1, N):
        total_sum += k * (N + 1)
    return total_sum

N = int(input().strip())

print(sum_of_numbers(N))
