# MBTI 각 글자에 대한 반대 값을 미리 정의
opposites = {
    'E': 'I',
    'I': 'E',
    'S': 'N',
    'N': 'S',
    'T': 'F',
    'F': 'T',
    'J': 'P',
    'P': 'J'
}

mbti = input()
opposite_mbti = ''.join(opposites[char] for char in mbti)

print(opposite_mbti)
