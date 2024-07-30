def print_star_pattern(N):
    for i in range(1, N + 1):
        stars = '*' * i
        spaces = ' ' * (2 * (N - i))
        print(stars + spaces + stars)
        
    for i in range(N - 1, 0, -1):
        stars = '*' * i
        spaces = ' ' * (2 * (N - i))
        print(stars + spaces + stars)


N = int(input().strip())

print_star_pattern(N)
