scores = []
for i in range(5):
    scores.append(sum(map(int, input().strip().split())))

max_score = max(scores)
winner = scores.index(max_score) + 1

print(winner, max_score)
