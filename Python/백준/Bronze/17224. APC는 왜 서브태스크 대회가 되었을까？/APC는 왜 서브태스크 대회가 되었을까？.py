def solution():
    N, L, K = map(int, input().split())
    problems = []
    
    for _ in range(N):
        sub1, sub2 = map(int, input().split())
        problems.append((sub1, sub2))

    hard_solves = []
    easy_solves = []
    
    for sub1, sub2 in problems:
        if sub2 <= L:  
            hard_solves.append(140)
        elif sub1 <= L: 
            easy_solves.append(100)
    total_score = 0
    total_score += sum(hard_solves[:K])
    K -= len(hard_solves)

    if K > 0:
        total_score += sum(easy_solves[:K])
    
    print(total_score)

solution()