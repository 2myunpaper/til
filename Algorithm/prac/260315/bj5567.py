import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
vertex = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    vertex[x].append(y)
    vertex[y].append(x)
    
ans = 0
check = [0] * (n+1)
check[1] = 1
for v in vertex[1]:
    if check[v] == 0:
        check[v] = 1
        ans += 1
        
    for w in vertex[v]:
        if check[w] == 0:
            check[w] = 1
            ans += 1

print(ans)