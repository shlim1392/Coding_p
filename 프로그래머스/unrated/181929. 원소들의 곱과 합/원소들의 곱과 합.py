from functools import reduce
def solution(num_list):
    a = reduce(lambda x, y: x * y, num_list, 1)
    b = sum(num_list)**2
    return  int(a < b) 