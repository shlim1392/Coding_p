import sys
from collections import Counter

def solution():
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    words = [word for word in data[1:] if len(word) >= m]

    count = Counter(words)
    result = sorted(count.keys(), key=lambda x: (-count[x], -len(x), x))

    sys.stdout.write('\n'.join(result) + '\n')

solution()
