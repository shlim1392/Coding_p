def solution(level_list):
    pos = []
    for x in level_list:
        if x < 250:
            pos.append(4)
        elif x >= 250 and x < 275:
            pos.append(3)
        elif x >= 275 and x < 300:
            pos.append(2)
        else:
            pos.append(1)
    return " ".join(map(str, pos))


n = int(input())
level_list = list(map(int, input().split()))


print(solution(level_list))
