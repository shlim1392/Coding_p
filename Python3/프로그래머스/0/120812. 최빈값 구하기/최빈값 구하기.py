from collections import Counter

def solution(array):
    frequency = Counter(array)
    most_common = frequency.most_common()
    
    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        return -1 
    else:
        return most_common[0][0] 