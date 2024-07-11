def calculate_interest_scores(n, scores, registered):
    total = sum(scores)
    non_registered_total = sum(scores[i] for i in range(n) if registered[i] == 0)
    return total, non_registered_total

n = int(input())
scores = list(map(int, input().split()))
registered = list(map(int, input().split()))


total, non_registered_total = calculate_interest_scores(n, scores, registered)

print(total)
print(non_registered_total)