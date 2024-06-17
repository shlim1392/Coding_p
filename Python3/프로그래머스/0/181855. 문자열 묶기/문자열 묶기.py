def solution(strArr):
    from collections import defaultdict
    length_groups = defaultdict(int)
    for string in strArr:
        length_groups[len(string)] += 1
    return max(length_groups.values())