import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    
    max_stock = [0] * N
    max_stock[N-1] = stock[N-1]
    ans = 0
    
    for i in range(N-2, -1, -1):
        max_stock[i] = max(max_stock[i+1], stock[i])
        ans += max_stock[i] - stock[i]

    print(ans)