import sys
input = sys.stdin.read

def solution():
    data = input().split()
    
    index = 0
    results = []
    
    for _ in range(3): 
        N = int(data[index])
        index += 1
        total_sum = 0
        
        for _ in range(N):
            total_sum += int(data[index])
            index += 1
        
        if total_sum > 0:
            results.append("+")
        elif total_sum < 0:
            results.append("-")
        else:
            results.append("0")
    
    print("\n".join(results))


if __name__ == "__main__":
    solution()
