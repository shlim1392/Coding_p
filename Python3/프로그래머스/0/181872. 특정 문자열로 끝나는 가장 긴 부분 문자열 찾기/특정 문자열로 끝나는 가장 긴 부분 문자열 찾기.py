def solution(myString, pat):
    start_pos = myString.rfind(pat)
    if start_pos == -1:
        return ""
    return myString[:start_pos + len(pat)]