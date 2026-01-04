T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    q_c = [0] * N
    for i in range(N):
        if i == M:
            q_c[i] = 1
            
    cnt = 0
    while True:
        c1, c2 = q[0], q_c[0]
        b = 0
        for i in range(1, len(q)):
            if c1 < q[i]:
                b = 1
                break
        
        if b == 1:
            q.append(c1)
            q_c.append(c2)
            q.pop(0)
            q_c.pop(0)
            continue
        
        else:
            cnt += 1
            if c2 == 1:
                break
            q.pop(0)
            q_c.pop(0)
            
    print(cnt)