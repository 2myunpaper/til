import sys

def DFS(n, dist):
    ans = 'sad'
    stack = []
    visited = [0] * (n+2)
    
    stack.append(0)
    visited[0] = 1
    
    while stack:
        p = stack.pop()
        
        if abs(dist[p][0] - dist[n+1][0]) + abs(dist[p][1] - dist[n+1][1]) <= 1000:
            ans = 'happy'
            break
        
        for i in range(1, n+1):
            if not visited[i]:
                if abs(dist[p][0] - dist[i][0]) + abs(dist[p][1] - dist[i][1]) <= 1000:
                    visited[i] = 1
                    stack.append(i)
    
    return ans


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    dist = []
    
    for _ in range(n+2):
        x, y = map(int, sys.stdin.readline().split())
        dist.append([x, y])
    
    print(DFS(n, dist))