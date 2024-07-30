def find_largest_uphill(N, heights):
    max_uphill = 0
    current_start = heights[0]
    current_max = 0

    for i in range(1, N):
        if heights[i] > heights[i - 1]:
            current_max = heights[i] - current_start
        else:
            max_uphill = max(max_uphill, current_max)
            current_start = heights[i]
            current_max = 0

    max_uphill = max(max_uphill, current_max)
    return max_uphill

N = int(input().strip())
heights = list(map(int, input().strip().split()))

result = find_largest_uphill(N, heights)
print(result)
