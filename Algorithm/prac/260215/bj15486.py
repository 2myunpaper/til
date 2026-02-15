import sys
input = sys.stdin.readline

N = int(input())
T = []
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N+1)
for i in range(N+1):
    if i > 0:
        dp[i] = max(dp[i], dp[i-1])
    
    if i < N and i + T[i] <= N:
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])

print(dp[N])