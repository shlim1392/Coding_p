n = int(input())
drinks = list(map(int, input().split()))

max_drink = max(drinks)

total = max_drink + sum(drink / 2 for drink in drinks if drink != max_drink)

print(total)
