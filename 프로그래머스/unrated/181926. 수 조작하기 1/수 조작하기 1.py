def solution(n, control):
    data = {"w":1, "s":-1, "d":10, "a":-10}
    return n + sum(data[x] for x in control)