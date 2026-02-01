import sys
input = sys.stdin.readline

N, K = map(int, input().split())
scores = list(map(int, input().split()))

start = 0
end = sum(scores)
ans = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    cnt = 0     # 부분합이 최소 mid값이 되는가에 대한 cnt
    
    for score in scores:
        total += score
        if total >= mid:
            cnt += 1
            total = 0
    
    if cnt >= K:    # 최소 mid값이 되는 파티션이 K 이상이다. -> 충분하다.
        ans = mid   # 그 값을 ans로 업데이트
        start = mid + 1     # 최대인 ans가 나오기 위해 start 점 업데이트
    else:
        end = mid - 1
    
print(ans)