T = int(input())
for i in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    
    for j in range(M):
        n, m = map(int, input().split())
        tree[n] = m

    start = N
    while start >= L:
        if start % 2 == 1:
            tree[start // 2] = tree[start] + tree[start - 1]
            start -= 2
        else:
            tree[start // 2] = tree[start]
            start -= 1

    print(f"#{i} {tree[L]}")
