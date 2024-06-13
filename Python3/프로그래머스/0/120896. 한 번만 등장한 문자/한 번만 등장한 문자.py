def solution(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    

    unique_chars = [char for char in char_count if char_count[char] == 1]
    unique_chars.sort()
    return ''.join(unique_chars)
