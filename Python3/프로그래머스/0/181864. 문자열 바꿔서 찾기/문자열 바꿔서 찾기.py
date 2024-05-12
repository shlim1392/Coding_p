def solution(myString, pat):
    trans = myString.maketrans("AB","BA")
    trans_string = myString.translate(trans)
    if pat in trans_string:
        return 1
    else :
        return 0