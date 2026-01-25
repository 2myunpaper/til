import sys
from collections import deque

def BFS(i, j):
    dist = [[-1] * col for _ in range(row)]
    q = deque()
    q.append((i, j))  # i좌표, j좌표, 걸린 시간
    dist[i][j] = 0
    hour = 0  # 걸린 시간 최대값
    
    while q:
        pi, pj = q.popleft()
        
        if dist[pi][pj] > hour:
            hour = dist[pi][pj]
        
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ti = pi + di
            tj = pj + dj
            
            if 0<=ti<row and 0<=tj<col and input_map[ti][tj] == 'L':
                if dist[ti][tj] == -1:
                    dist[ti][tj] = dist[pi][pj] + 1
                    q.append((ti, tj))
                
    return hour


row, col = map(int, sys.stdin.readline().split())
input_map = []
max_hour = 0

for n in range(row):
    line = sys.stdin.readline()
    input_map.append(line)
    
for i in range(row):
    for j in range(col):
        if input_map[i][j] == 'L':
            land_cnt = 0
            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                ti = i + di
                tj = j + dj
                
                if 0<=ti<row and 0<=tj<col and input_map[ti][tj] == 'L':
                    land_cnt += 1
            
            # 상하좌우 중 3곳 이상이 육지라면 그 지점은 탐색할 필요가 없다.
            if land_cnt < 3:
                max_hour = max(max_hour, BFS(i, j))

print(max_hour)