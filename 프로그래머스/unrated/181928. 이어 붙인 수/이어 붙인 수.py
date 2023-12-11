def solution(num_list):
    even = ""
    odd = ""
    for x in num_list:
        if x % 2==0:
            even += str(x)
        else:
            odd += str(x)
    return int(even) + int(odd)

def solution(num_list):
    even=int(''.join([str(i) for i in num_list if i%2==0]))
    odd=int(''.join([str(i) for i in num_list if not i%2==0]))
    return even+odd

# join 함수는 리스트의 각 요소를 하나의 문자열로 합치는 역할
