import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    wanted = [0]
    wanted.extend(list((map(int, input().split()))))
    check = [0] * (N+1)
    check[0] = 1
    ans = 0
    
    for i in range(1, N+1):
        if i == wanted[i]:
            check[i] = 1
    
    for i in range(1, N+1):
        if check[i] == 1:
            continue
        
        check[i] = 1
        p = wanted[i]
        cnt = 1
        
        while True:
            if i == p:
                break
            
            if check[p] == 1:
                ans += cnt
                break
            
            check[p] = 1    
            cnt += 1
            p = wanted[p]
    
    print(ans)