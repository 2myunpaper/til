import sys

delta = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
cross = [delta[1], delta[3], delta[5], delta[7]]    # 대각선 방향 0, 2, 4, 6

N, M = map(int, sys.stdin.readline().split())
ground = []
for _ in range(N):
    ground.append(list(map(int, sys.stdin.readline().split())))
    
cloud = [[N-2, 0], [N-2, 1], [N-1, 0], [N-1, 1]]
for _ in range(M):
    d, s = map(int, sys.stdin.readline().split())
    # 인덱스 정리
    d -= 1
    s %= N
    
    is_cloud = [[False] * N for _ in range(N)]
    # cloud 이동 후 물 1 추가
    for n in range(len(cloud)):
        cloud[n][0] = (cloud[n][0] + delta[d][0] * s + N) % N
        cloud[n][1] = (cloud[n][1] + delta[d][1] * s + N) % N

        is_cloud[cloud[n][0]][cloud[n][1]] = True
        ground[cloud[n][0]][cloud[n][1]] += 1
    
    # cloud 대각선 방향 물 확인 후 추가
    for n in range(len(cloud)):
        for i, j in cross:
            di = cloud[n][0] + i
            dj = cloud[n][1] + j
            
            if 0 <= di < N and 0 <= dj < N and ground[di][dj] > 0:
                ground[cloud[n][0]][cloud[n][1]] += 1

    # cloud 업데이트
    tmp = []
    for i in range(N):
        for j in range(N):
            if is_cloud[i][j] == False and ground[i][j] >= 2:
                tmp.append([i, j])
                ground[i][j] -= 2
    cloud = tmp


print(sum(map(sum, ground)))