def solution(n):
    vote = 0
    for _ in range(n):
        op = int(input())
        if op > 0 :
            vote += 1
        else:
            vote -= 1
            
    if vote > 0:
        print("Junhee is cute!")
    else:
        print("Junhee is not cute!")
        
n = int(input())
solution(n)