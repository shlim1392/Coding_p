def min_key_presses(n, m, sequence):
    current_tab = 1
    total_presses = 0
    
    for target_tab in sequence:
        forward_distance = (target_tab - current_tab) % n
        backward_distance = (current_tab - target_tab) % n
        total_presses += min(forward_distance, backward_distance)
        current_tab = target_tab
    
    return total_presses

import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
sequence = list(map(int, data[2:2+m]))

result = min_key_presses(n, m, sequence)

print(result)
