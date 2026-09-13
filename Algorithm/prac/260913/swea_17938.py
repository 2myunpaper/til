T = int(input())

for i in range(1, T+1):
    x, y, z = map(int, input().split())
    
    ybj = [[[0, 1], x], [[1, 2], y], [[2, 0], z]]     # ex) [[a, b], LCS(a, b)]
    dp = [[0, 0], [0, 0], [0, 0]]                     # a, b, c에 대한 1과 0 개수
    
    ybj.sort(key=lambda x: x[1])    # LCS 값으로 sorting
        
    # dp[sort된 첫번째], dp[sort된 두번째]
    dp[ybj[0][0][0]][0] = dp[ybj[0][0][1]][0] = ybj[0][1]
    
    # dp[sort된 두번째], dp[sort된 세번째]
    dp[ybj[1][0][0]][0] = dp[ybj[1][0][1]][0] = ybj[1][1]
    
    # dp[sort된 세번째], dp[sort된 첫번째]
    dp[ybj[2][0][0]][1] = dp[ybj[2][0][1]][1] = ybj[2][1] - ybj[0][1]
    
    print(f"#{i}", end=" ")
    print("1"*dp[0][0] + "0"*dp[0][1], end=" ")
    print("1"*dp[1][0] + "0"*dp[1][1], end=" ")
    print("1"*dp[2][0] + "0"*dp[2][1])