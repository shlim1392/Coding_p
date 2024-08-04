def is_hansu(num):
    if num < 100:
        return True
    else:
        digits = list(map(int, str(num)))
        return (digits[1] - digits[0]) == (digits[2] - digits[1])

def count_hansu(N):
    count = 0
    for i in range(1, N + 1):
        if is_hansu(i):
            count += 1
    return count

N = int(input().strip())
print(count_hansu(N))
