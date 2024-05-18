def solution(num_list):
    res = 0  
    for num in num_list:  
        while num != 1:  
            if num % 2 == 0:  
                num = num // 2
            else:  
                num = (num-1) // 2
            res += 1  
    return res  