def solution(array):
    res = []
    res.append(max(array)) 
    res.append(array.index(max(array))) 
    return res