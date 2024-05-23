alphabet_to_number_mapping = [
    ('ABC', 2), ('DEF', 3), ('GHI', 4),
    ('JKL', 5), ('MNO', 6), ('PQRS', 7),
    ('TUV', 8), ('WXYZ', 9)
]

def alphabet_to_number(ch):
    for letters, number in alphabet_to_number_mapping:
        if ch in letters:
            return number
    return 0  
def min_time_to_dial(word):
    total_time = 0
    for ch in word:
        number = alphabet_to_number(ch)
        total_time += number + 1  
    return total_time

word = input()
print(min_time_to_dial(word))
