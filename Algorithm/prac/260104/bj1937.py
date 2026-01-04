import sys

N = int(sys.stdin.readline())
bamboo = []
for _ in range(N):
    bamboo.append(list(map(int, sys.stdin.readline().split())))
    
history = []
visited = [[4] * N for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        for di, dj in [[-1, 0], [0, -1], [1, 0], [0, 1]]:  # 좌상우하
            ti = i + di
            tj = j + dj
            
            if 0 <= ti < N and 0 <= tj < N:
                if bamboo[i][j] > bamboo[ti][tj]:
                    visited[i][j] -= 1
        
        if visited[i][j] == 4:
            history.append([i, j])
            cnt += 1

ans = 1
while cnt < N**2:
    new_history = []
    
    for i, j in history:
        for di, dj in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            ti = i + di
            tj = j + dj
            
            if 0 <= ti < N and 0 <= tj < N and visited[ti][tj] != 4:
                visited[ti][tj] += 1
                
                if visited[ti][tj] == 4:
                    cnt += 1
                    new_history.append([ti, tj])
    
    history = new_history
    ans += 1

print(ans)