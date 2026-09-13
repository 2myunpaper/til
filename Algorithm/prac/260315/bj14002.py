import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

cnt = max(dp)
ans = []
for i in range(N-1, -1, -1):
    if dp[i] == cnt:
        ans.append(array[i])
        cnt -= 1

print(len(ans))
print(*ans[::-1])