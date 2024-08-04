import sys

def max_temperature_sum(N, K, temperatures):
    current_sum = sum(temperatures[:K])
    max_sum = current_sum
    
    for i in range(K, N):
        current_sum += temperatures[i] - temperatures[i - K]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def main():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    K = int(data[1])
    temperatures = list(map(int, data[2:]))
    
    result = max_temperature_sum(N, K, temperatures)
    print(result)

main()
