import sys

stack_l = list(sys.stdin.readline().strip())
stack_r = []
M = int(sys.stdin.readline())

for _ in range(M):
    inp = list(sys.stdin.readline().split())
    command = inp[0]
    if len(inp) != 1:
        word = inp[1]
    
    if command == 'L':
        if len(stack_l) == 0:
            continue
        tmp = stack_l.pop()
        stack_r.append(tmp)
    elif command == 'D':
        if len(stack_r) == 0:
            continue
        tmp = stack_r.pop()
        stack_l.append(tmp)
    elif command == 'B':
        if len(stack_l) == 0:
            continue
        stack_l.pop()
    elif command == 'P':
        stack_l.append(word)
        
ans = "".join(stack_l) + "".join(stack_r[::-1])  # stack_r은 뒤집어서 출력해야 됨.
print(ans)