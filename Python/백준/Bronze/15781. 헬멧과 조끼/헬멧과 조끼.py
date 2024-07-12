N, M = map(int, input().split())
helmets = list(map(int, input().split()))
jackets = list(map(int, input().split()))

max_helmet = max(helmets)
max_jacket = max(jackets)

max_defense = max_helmet + max_jacket

print(max_defense)
