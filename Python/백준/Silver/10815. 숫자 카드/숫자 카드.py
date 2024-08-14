import sys
input = sys.stdin.read

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


data = input().split()

n = int(data[0])
cards = list(map(int, data[1:n+1]))
m = int(data[n+1])
targets = list(map(int, data[n+2:n+2+m]))

cards.sort()

result = []
for target in targets:
    if binary_search(cards, target, 0, n-1):
        result.append('1')
    else:
        result.append('0')

print(' '.join(result))
