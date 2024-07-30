def remove_typo(position, word):
    corrected_word = word[:position - 1] + word[position:]
    return corrected_word

T = int(input().strip())
test_cases = []

for _ in range(T):
    data = input().strip().split()
    position = int(data[0])
    word = data[1]
    test_cases.append((position, word))

for position, word in test_cases:
    result = remove_typo(position, word)
    print(result)
