import sys

def cal(a, b, shape):
    if shape == '+':
        return a + b
    elif shape == '-':
        return a - b
    elif shape == '*':
        return a * b


def recur(susik):
    global ans
    
    if len(susik) == 1:
        ans = max(ans, int(susik))
        return
    
    for i in range(1, len(susik), 2):
        ref_a = int(susik[i-1])
        ref_b = int(susik[i+1])
        shape = susik[i]
        tmp = []
        
        if i != 1:
            tmp.extend(susik[:i+1])
        
        tmp.append(cal(ref_a, ref_b, shape))
        
        if i != len(susik) - 2:
            tmp.extend(susik[i+2:])
        
        recur(tmp)
        

N = int(sys.stdin.readline())
input_susik = list(sys.stdin.readline().strip())
ans = -float('inf')

recur(input_susik)
print(ans)