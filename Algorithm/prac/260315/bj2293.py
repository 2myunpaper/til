import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort()

dp = [0] * (k+1)
for c in coins:
    dp[c] = 1
    
for i in range(coins[0]+coins[0], k+1):
    

print(coins)