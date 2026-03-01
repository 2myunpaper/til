import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 31
dp[2] = 3

i = 4
while i <= 30:
    for j in range(2, i+1, 2):
        if j == 2:
            dp[i] += dp[i-j] * dp[2]
        elif j == i:
            dp[i] += 2
        else:
            dp[i] += dp[i-j] * 2
    
    i += 2

print(dp[N])