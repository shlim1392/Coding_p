def solution(s, n):
    res = ""
    for char in s:
        if char.isalpha():
            if char.isupper():
                res += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            else:
                res += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        else:
            res += char
    return res