def solution(my_string):
    letter = ['a', "e", "i", "o","u"]
    for x in letter:
        my_string = my_string.replace(x, "")
    return my_string