import sys

X, Y = map(int, sys.stdin.readline().split())
Z = (Y * 100) // X
ans = -1

if Z >= 99:
    pass
else:
    start = 0
    end = 1000000000

    while start <= end:
        mid = (start + end) // 2
        new_Z = ((Y + mid) * 100) // (X + mid)
        
        if new_Z > Z:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
            
print(ans)