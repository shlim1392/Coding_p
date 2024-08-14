from collections import defaultdict, deque

def bfs(start, graph, n):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 0
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
                
    return count

def main():
    n, m = map(int, input().split())
    
    heavier = defaultdict(list)
    lighter = defaultdict(list)
    
    for _ in range(m):
        heavy, light = map(int, input().split())
        heavier[light].append(heavy)
        lighter[heavy].append(light)
    
    impossible = 0
    mid = (n + 1) // 2
    
    for i in range(1, n + 1):
        heavier_count = bfs(i, heavier, n)
        lighter_count = bfs(i, lighter, n)
        
        if heavier_count >= mid or lighter_count >= mid:
            impossible += 1
    
    print(impossible)

if __name__ == "__main__":
    main()
