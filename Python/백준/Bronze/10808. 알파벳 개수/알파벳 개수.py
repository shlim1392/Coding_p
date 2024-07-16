def count_alphabets(S):
    counts = [0] * 26
    
    for char in S:
        index = ord(char) - ord('a')  
        counts[index] += 1
    
    print(' '.join(map(str, counts)))

S = input().strip()
count_alphabets(S)
