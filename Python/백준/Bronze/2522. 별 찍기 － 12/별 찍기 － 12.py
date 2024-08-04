def print_star_pattern(N):
    for i in range(1, N+1):
        print(' ' * (N - i) + '*' * i)
    
    for i in range(1, N):
        print(' ' * i + '*' * (N - i))

N = int(input().strip())
print_star_pattern(N)
