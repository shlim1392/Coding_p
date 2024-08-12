n, game_type = input().split()
n = int(n)

players = set(input().strip() for _ in range(n))

if game_type == 'Y':
    required_players = 2
elif game_type == 'F':
    required_players = 3
elif game_type == 'O':
    required_players = 4

max_games = len(players) // (required_players - 1)

print(max_games)
