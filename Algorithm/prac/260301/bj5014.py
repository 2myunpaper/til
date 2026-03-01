from collections import deque
import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())   # 1 ≤ S + (U*a - d*b) = G ≤ F
visited = [-1] * (F+1)
visited[S] = 0
q = deque()
q.append(S)

while q:
    floor = q.popleft()
    
    for da, db in [[0, 1], [1, 0]]:
        p_floor = floor + U * da - D * db
        
        if 1 <= p_floor <= F and visited[p_floor] == -1:
            q.append(p_floor)
            visited[p_floor] = visited[floor] + 1

if visited[G] == -1:
    print("use the stairs")
    
else:
    print(visited[G])