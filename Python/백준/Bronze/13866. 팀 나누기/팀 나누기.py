def min_skill_difference(A, B, C, D):
    diff1 = abs((A + B) - (C + D))
    diff2 = abs((A + C) - (B + D))
    diff3 = abs((A + D) - (B + C))
    

    return min(diff1, diff2, diff3)

A, B, C, D = map(int, input().split())

print(min_skill_difference(A, B, C, D))
