import sys

# 소수 구하기
def prime_numbers():
    prime_test = [True] * 1000001
    prime_test[0] = False
    prime_test[1] = False

    prime = []
    i = 2
    while i <= 1000000:
        if prime_test[i]:
            prime.append(i)
            j = 2
            
            while i * j <= 1000000:
                prime_test[i * j] = False
                j += 1
        
        i += 1
    
    return prime


# 투포인터(?) 합수
def find_goldbach(n):
    start = 0
    end = len(prime) - 1
    cnt = 0
    
    while start <= end:
        x = prime[start]
        y = prime[end]
        
        if x + y == n:
            cnt += 1
            start += 1
            end -= 1
        elif x + y > n:
            end -= 1
        else:
            start += 1

    return cnt


# 문제 풀이
T = int(sys.stdin.readline())
prime = prime_numbers()

for _ in range(T):
    num = int(sys.stdin.readline())
    print(find_goldbach(num))