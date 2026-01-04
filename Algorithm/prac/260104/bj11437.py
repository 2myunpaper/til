import sys

N = int(sys.stdin.readline())
parent = [-1] * (N+1)
depth = [0] * (N+1)
parent[1] = 0

for _ in range(N-1):
    n1, n2 = map(int, sys.stdin.readline().split())
    
    p = n1
    c = n2
    
    if parent[n2] != -1 and parent[n1] == -1:
        p = n2
        c = n1
    
    parent[c] = p

# depth 정보 생성
for i in range(2, N+1):
    n = i
    while n != 1:
        depth[i] += 1
        n = parent[n]
    
    print(depth[i])

M = int(sys.stdin.readline())
for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    
    while depth[n1] != depth[n2]:
        if depth[n1] > depth[n2]:
            n1 = parent[n1]
        else:
            n2 = parent[n2]
    
    while n1 != n2:
        n1 = parent[n1]
        n2 = parent[n2]
        
    print(n1)