import sys

def solve():
    # 입력 받기
    N, K = map(int, sys.stdin.readline().split())
    
    # 각 무게별 최대 가치를 저장할 DP 테이블
    # dp[w] = 무게 w일 때 담을 수 있는 최대 가치
    dp = [0] * (K + 1)
    
    for _ in range(N):
        w, v = map(int, sys.stdin.readline().split())
        
        # 무게 한도(K)부터 현재 물건의 무게(w)까지 거꾸로 순회
        # 거꾸로 순회하는 이유는 '현재 단계'에서 물건을 중복해서 담지 않기 위해서야!
        for j in range(K, w - 1, -1):
            # 기존의 가치 vs (현재 물건 가치 + 현재 물건을 넣기 전 남은 무게의 최대 가치)
            if dp[j] < dp[j - w] + v:
                dp[j] = dp[j - w] + v
                
    # 배낭 무게 K일 때의 최대 가치 출력
    print(dp[K])

solve()