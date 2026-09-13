import sys
input = sys.stdin.readline

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

water = 0
for N in range(1, H+1):
    flag = -1
    
    for i in range(W):
        if blocks[i] >= N:
            if flag != -1:
                water += i - flag - 1
            
            flag = i

print(water)