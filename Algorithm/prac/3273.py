N = int(input())
arr = list(map(int, input().split()))
n = int(input())

arr.sort()
l = 0
r = N-1
cnt = 0

while l < r:
    sum = arr[l] + arr[r]
    
    if sum == n:
        cnt += 1
        l += 1
        r -= 1
    elif sum > n:
        r -= 1
    else:
        l += 1
        
print(cnt)