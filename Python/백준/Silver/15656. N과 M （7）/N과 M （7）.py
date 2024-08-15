from itertools import product

def solution():
    N, M = map(int, input().split())
    numbers = sorted(map(int, input().split()))

    for seq in product(numbers, repeat=M):
        print(' '.join(map(str, seq)))

solution()
