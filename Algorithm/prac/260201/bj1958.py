s1 = input()
s2 = input()
s3 = input()

N = len(s1)
M = len(s2)
O = len(s3)
dp = [[[0] * (O + 1) for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        for k in range(1, O+1):
            if s1[i-1] == s2[j-1] == s3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[N][M][O])