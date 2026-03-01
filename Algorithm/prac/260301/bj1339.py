import sys
input = sys.stdin.readline

input_list = []
N = int(input())

for _ in range(N):
    input_list.append(input().strip())

word = {}

for w in input_list:
    cnt = 0
    for i in range(len(w)-1, -1, -1):
        if w[i] in word.keys():
            word[w[i]] += 10 ** cnt
        
        else:
            word[w[i]] = 10 ** cnt
        
        cnt += 1

word_sorted = sorted(word.items(), key=lambda x: x[1], reverse=True)
limit = 9
ans = 0

for w in word_sorted:
    ans += limit * w[1]
    limit -= 1
    
print(ans)