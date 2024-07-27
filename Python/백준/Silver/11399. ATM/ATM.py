def min_total_waiting_time(N, times):
    times.sort()

    total_time = 0
    accumulated_time = 0
    
    for time in times:
        accumulated_time += time
        total_time += accumulated_time
    
    return total_time

N = int(input().strip())
times = list(map(int, input().strip().split()))

print(min_total_waiting_time(N, times))
