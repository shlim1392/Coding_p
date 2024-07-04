N = int(input().strip())
total_amount = 0

bill_values = {
    136: 1000,
    142: 5000,
    148: 10000,
    154: 50000
}


for _ in range(N):
    width, height = map(int, input().strip().split())
    if height == 68:
        total_amount += bill_values[width]


print(total_amount)


