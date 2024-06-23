n = int(input())
member = list(map(str, input().split()))
class_ = input()

def solution(member, class_):
    res = 0
    for x in member:
        if x == class_:
            res += 1
    return res


print(solution(member, class_))