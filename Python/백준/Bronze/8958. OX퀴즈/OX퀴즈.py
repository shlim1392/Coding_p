def solution(n):
    for _ in range(n):
        test = input()
        score = 0
        re = 0
        
        for x in test:
            if x == "O":
                re += 1
                score += re
            else:
                re =0
        print(score)
        
n = int(input())        
solution(n)
        