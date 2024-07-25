L, P = map(int, input().strip().split())
article_counts = list(map(int, input().strip().split()))

correct_count = L * P

differences = [count - correct_count for count in article_counts]

print(" ".join(map(str, differences)))
