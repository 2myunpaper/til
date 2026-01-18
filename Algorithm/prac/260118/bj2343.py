import sys

def sum_lectures(i, j):
    hap = 0
    for l in range(i, j+1):
        hap += lectures[l]
        
    return hap


N, M = map(int, sys.stdin.readline().split())
lectures = list(map(int, sys.stdin.readline().split()))

disc = []
disc.append([0, N-1, sum(lectures)])  # start, end, 총합
cnt = M-1
while cnt > 0:
    start, end, hap = disc.pop()
    
    if start == end:
        continue
    
    mid = (start + end) // 2
    
    hap1 = sum_lectures(start, mid)
    hap2 = sum_lectures(mid, end)
    
    if hap1 <= hap2:
        disc.append([start, mid, hap1])
        disc.append([mid+1, end, hap2-lectures[mid]])
    else:
        disc.append([start, mid-1, hap1-lectures[mid]])
        disc.append([mid, end, hap2])
    
    disc.sort(key=lambda x:x[2])
    cnt -= 1
    
ans = disc.pop()
print(ans[2])