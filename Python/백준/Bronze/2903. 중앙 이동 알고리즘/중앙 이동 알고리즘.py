def calculate_points(N):
    return (2**N + 1) ** 2


N = int(input().strip())


print(calculate_points(N))
