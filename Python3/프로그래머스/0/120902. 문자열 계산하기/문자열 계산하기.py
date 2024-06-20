def solution(my_string):
    try:
        result = eval(my_string)
        return result
    except Exception as e:
        return str(e)