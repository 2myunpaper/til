import sys

def numbers(cnt, array):
    if cnt == M:
        for n in array:
            print(n, end=' ')
        print()
        return
    
    for i in range(1, N+1):
        tmp = array[:]
        
        tmp.append(i)
        numbers(cnt+1, tmp)
        tmp.pop()
        

N, M = map(int, sys.stdin.readline().split())
numbers(0, [])