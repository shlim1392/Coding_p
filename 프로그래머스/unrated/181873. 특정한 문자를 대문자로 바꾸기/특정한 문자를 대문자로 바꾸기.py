def solution(my_string, alp):
    result_string = ""
    for char in my_string:
        if char == alp:
            result_string += char.upper()
        else:
            result_string += char
    return result_string


# def solution(my_string, alp):
#    return my_string.replace(alp, alp.upper())
