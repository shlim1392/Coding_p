def solution(s):
    n=0
    m=0
    for c in s.lower():
        if c == "p":
            n +=1
        elif c == "y":
            m +=1
    return True if n == m else False           