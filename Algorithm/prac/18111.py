N, M, B = map(int, input().split())
arr = []
for i in range(N):
    arr.extend(list(map(int, input().split())))
    
max_h = max(arr)  # 블록 중 가장 높은 높이
h = [0] * (max_h+1)
for i in range(max_h+1):
    h[i] = arr.count(i)

arr_s = set(arr)
min_time = float('inf')
goal_h = max_h
for sh in range(257):
    time = 0
    find = 1
    B_tmp = B
    
    for x in list(arr_s):
        if x > sh:
            time += 2*(x - sh)*h[x]
        else:
            if B_tmp - (sh - x)*h[x] < 0:
                find = 0
                break
            else:
                time += (sh - x)*h[x]
                B_tmp -= (sh - x)*h[x]
    
    if find == 0:
        continue
    
    else:
        if time < min_time:
            min_time = time
            goal_h = sh

print(min_time, goal_h)