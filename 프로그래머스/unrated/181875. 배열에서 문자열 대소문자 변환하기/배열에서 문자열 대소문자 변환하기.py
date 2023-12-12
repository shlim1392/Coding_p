def solution(strArr):
    return [char.upper() if i % 2 == 1 else char.lower() for i, char in enumerate(strArr)]