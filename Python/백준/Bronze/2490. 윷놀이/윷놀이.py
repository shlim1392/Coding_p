def solution(y):
    zero_count = y.count(0)  
    result_dict = {
        1: 'A',  
        2: 'B',  
        3: 'C',  
        4: 'D',  
        0: 'E'   
    }
    
    return result_dict[zero_count]


for _ in range(3):
    y = list(map(int, input().split()))
    result = solution(y)
    print(result)

