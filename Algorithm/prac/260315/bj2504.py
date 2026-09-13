import sys
input = sys.stdin.readline

inp = input()
inp = inp.replace('()', '2')
inp = inp.replace('[]', '3')
inp = inp.replace('(2)', '4')
inp = inp.replace('[2]', '6')
inp = inp.replace('(3)', '6')
inp = inp.replace('[3]', '9')

while len(inp) != 1:
    fix = []
    num = []
    mul = 1
    start = 0
    end = 0
    
    for i in range(len(inp)):
        if inp[i] == '(':
            start = i
            mul = 2
            
        elif inp[i] == '[':
            start = i
            mul = 3
        
        elif inp[i] == ')' or inp[i] == ']':
            end = i
            fix.append([start, end, sum(num)*mul])
            start = 0
            end = 0
            num = []
        
        