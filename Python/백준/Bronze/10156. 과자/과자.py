def solution():
    K, N, M = map(int, input().split())  
    total_cost = K * N  
    money_needed = total_cost - M  
    
    if money_needed > 0:
        print(money_needed)  
    else:
        print(0)  

solution()
