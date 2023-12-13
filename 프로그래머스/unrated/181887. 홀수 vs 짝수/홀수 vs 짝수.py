def solution(num_list):
    even = 0
    odd = 0
    
    for i, x in enumerate(num_list, start=1):
        if i % 2 == 0: 
            even += x
        else:  
            odd += x
            
    return odd if odd >= even else even

def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))
