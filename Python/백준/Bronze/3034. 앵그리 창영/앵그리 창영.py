import math

def can_matchbox_hold_matches(N, W, H, match_lengths):
    diagonal_length = math.sqrt(W * W + H * H)
    
    results = []
    for length in match_lengths:
        if length <= diagonal_length:
            results.append("DA")
        else:
            results.append("NE")
    
    return results


import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
W = int(data[1])
H = int(data[2])

match_lengths = [int(data[i]) for i in range(3, 3 + N)]

results = can_matchbox_hold_matches(N, W, H, match_lengths)
for result in results:
    print(result)
