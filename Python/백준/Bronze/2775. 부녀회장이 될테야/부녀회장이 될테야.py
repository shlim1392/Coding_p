def num_people(k, n):
    floor = [i for i in range(1, n+1)]

    for _ in range(k):
        for i in range(1, n):
            floor[i] += floor[i-1]
    
    return floor[-1]

T = int(input())
results = []
for _ in range(T):
    k = int(input())
    n = int(input())
    results.append(num_people(k, n))


for result in results:
    print(result)
