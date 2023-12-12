def solution(arr):
    res = [] 
    
    for x in arr:
        if x >= 50 and x % 2 == 0: 
            res.append(x // 2) 
        elif x < 50 and x % 2 == 1: 
            res.append(x * 2)  
        else:
            res.append(x)  
    
    return res