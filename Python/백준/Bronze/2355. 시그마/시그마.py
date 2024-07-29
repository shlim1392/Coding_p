def sum_between_two_numbers(A, B):
    start = min(A, B)
    end = max(A, B)
    count = end - start + 1
    total_sum = count * (start + end) // 2
    
    return total_sum

import sys
input = sys.stdin.read
data = input().split()
A = int(data[0])
B = int(data[1])

result = sum_between_two_numbers(A, B)
print(result)
