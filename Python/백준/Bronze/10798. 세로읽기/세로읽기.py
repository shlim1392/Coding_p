words = [input().strip() for _ in range(5)]
max_length = max(len(word) for word in words)
result = ""

for i in range(max_length):
    for word in words:
        if i < len(word):
            result += word[i]

print(result)

    