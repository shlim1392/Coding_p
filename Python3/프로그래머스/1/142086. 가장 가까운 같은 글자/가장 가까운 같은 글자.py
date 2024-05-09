def solution(s):
    answer =[]
    save = {}
    for idx, x in enumerate(s):
        if x in save:
            diff = idx - save[x] +1
            answer.append(diff)
            save[x] = idx + 1
        else:
            answer.append(-1)
            save[x] = idx +1
    return answer