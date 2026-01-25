import sys

def find_set(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x != root_y:
        if root_x < root_y:
            parents[root_y] = root_x
        else:
            parents[root_x] = root_y


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parents = [i for i in range(N+1)]

for i in range(1, N+1):
    connection = [0]
    connection.extend(list(map(int, sys.stdin.readline().split())))
    
    for n in range(1, N+1):
        if connection[n]:
            union(i, n)
    
places = list(map(int, sys.stdin.readline().split()))
i = 0
ans = 'YES'

while i < len(places) - 1:
    ref_x = find_set(places[i])
    ref_y = find_set(places[i+1])
    
    if ref_x != ref_y:
        ans = 'NO'
        break
    
    i += 1
    
print(ans)