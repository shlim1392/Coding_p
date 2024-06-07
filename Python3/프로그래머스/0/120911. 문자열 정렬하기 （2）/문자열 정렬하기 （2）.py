def solution(my_string):
    lower_string = my_string.lower()
    sorted_list = sorted(lower_string)
    result = ''.join(sorted_list)
    return result