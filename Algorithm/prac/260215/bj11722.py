import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 수열을 뒤집어서 가장 긴 증가하는 문제로 바꿈
arr.reverse()

tails = [arr[0]]

for i in range(1, N):
    num = arr[i]
    
    # 현재 숫자가 tails의 가장 큰 숫자보다 크다면?
    # 그냥 뒤에 붙인다.
    if tails[-1] < num:
        tails.append(num)
        
    # 아니라면, 중간 어딘가에 끼워 넣어서 값을 작게 유지해야 함
    else:
        l, r = 0, len(tails) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            # num보다 크거나 같은 첫 번째 숫자 위치
            if tails[mid] < num:
                l = mid + 1
            else:
                r = mid
        
        # 더 작은 값으로 갱신
        tails[r] = num

print(len(tails))