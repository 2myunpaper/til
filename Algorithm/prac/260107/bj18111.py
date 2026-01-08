import sys

N, M, B = map(int, sys.stdin.readline().split())
input_blocks = {}
max_height = 0
min_height = float('inf')

for i in range(257):
    input_blocks[i] = 0

for i in range(N):
    blocks = list(map(int, sys.stdin.readline().split()))
    max_height = max(max_height, max(blocks))
    min_height = min(min_height, min(blocks))
    for j in blocks:
        input_blocks[j] += 1

ans = [N*M*256*2, 0]    # 걸린 시간, 평탄화 높이
for i in range(min_height, max_height+1):  # i층으로 평탄화
    inven = B
    time = 0
    for j in range(min_height, max_height+1):  # input_blocks 순회 -> index j
        if i == j or input_blocks[j] == 0:
            continue
        elif i > j:
            time += input_blocks[j]*(i-j)
            inven -= input_blocks[j]*(i-j)
        else:
            time += 2*input_blocks[j]*(j-i)
            inven += input_blocks[j]*(j-i)
    
    if inven < 0:
        continue
    else:
        if ans[0] > time:
            ans[0] = time
            ans[1] = i
        elif ans[0] == time:
            ans[1] = i
        
print(ans[0], ans[1])