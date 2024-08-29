import re

def solution(my_string):
    numbers = re.findall(r'\d+', my_string)
    answer = sum(int(num) for num in numbers)
    
    return answer
