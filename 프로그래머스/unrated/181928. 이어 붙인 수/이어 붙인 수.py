def solution(num_list):
    even = ""
    odd = ""
    for x in num_list:
        if x % 2==0:
            even += str(x)
        else:
            odd += str(x)
    return int(even) + int(odd)