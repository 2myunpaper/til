<aside>

**스택 (Stack)**

LIFO (Last In First Out) - 가장 마지막에 삽입된 데이터가 먼저 삭제되는 구조

*ex) 깊이 우선 탐색 (DFS) 알고리즘, 역순 문자열 생성, 실행 취소*

</aside>

## 스택 (Stack)

물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조이다.

스택에 저장된 자료는 선형 구조를 갖는다.

<aside>

**선형구조** : 자료 간의 관계가 1대1 의 관계를 갖는다.

**비선형구조** : 자료 간의 관계가 1대N 의 관계를 갖는다.

</aside>

스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.

### 스택의 특성

마지막에 삽입한 자료를 가장 먼저 꺼낸다.

**후입선출 (LIFO, Last-In-First-Out)** 이라고 부른다.

*ex)* 스택에 1,2,3 순으로 자료를 삽입한 후 꺼내면 역 순으로 3,2,1순으로 꺼낼 수 있다.

### 스택의 구현

스택을 프로그램에서 구현하기 위해서 필요한 건 무엇일까?

**자료를 선형으로 저장할 저장소가 필요하다.**

이는 배열을 사용할 수 있다. 그리고 저장소 자체를 스택이라 부르기도 한다.

스택에서 **마지막 삽입된 원소의 위치**를 **top**이라 부른다.

스택의 연산은 아래와 같다.

<aside>

**push(삽입)** : 저장소에 자료를 저장한다.

**pop(삭제)** : 저장소에서 자료를 꺼낸다. 꺼낸 자료는 삽입한 자료의 역순으로 꺼낸다.

**isEmpty** : 스택이 공백인지 아닌지를 확인하는 연산

**peek** : 스택의 top에 는 item(원소)을 반환하는 연산

</aside>

**스택의 삽입/삭제 과정** 을 예시로 알아보자.

아래는 빈 스택에 원소 A,B,C를 차례로 삽입 후 한번 삭제하는 연산 과정이다.

<aside>

*ex)* 스택 [ _ , _ , _ , _ , _ ] 이 주어진 경우

push A : **top (공백 스택)** [ _ , _ , _ , _ , _ ] ← A

push B : **top (A지점)** [ A , _ , _ , _ , _ ] ← B

push C : **top (B지점)** [ A , B , _ , _ , _ ] ← C

pop : **top (C지점)** [ A , B , C , _ , _ ] → C

**top (B지점)** [ A , B , _ , _ , _ ]

</aside>

스택 **push** 알고리즘은 우리가 배열에서 사용했던 `append()` 메소드를 통해서도 구현할 수 있다.

그러나 많은 작업이 발생하면, `append()` 는 느려질 수 있다는 단점이 있다.

이를 사용하지 않고, 아래와 같이 코드를 짜볼 수 있겠다.

```python
def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item

size = 10
stack = [0] * size
top = -1

push(10,size)  # stack[0] = 10

# 아래 코드는 함수를 쓰지 않고, push(20)을 구현한 것
top += 1
stack[top] = 20  # stack[1] = 20
```

스택의 **pop** 알고리즘은 배열의 `pop()` 메소드를 사용할 수도 있겠다.

`pop()` 메소드를 사용하지 않고, 아래와 같이 코드를 짜볼 수 있겠다.

```python
def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top+1]
    
print(pop())

# 아래 코드는 함수를 쓰지 않고, pop()을 구현한 것
if top > -1:
    top -= 1
    print(stack[top+1])
```

### 스택 구현 고려 사항

1차원 배열을 사용하여 구현할 경우 구현이 용이하다는 장점이 있지만 **스택의 크기를 변경하기가 어렵다**는 단점이 있다.

이를 해결하기 위한 방법으로 **저장소를 동적으로 할당**하여 스택을 구현하는 방법이 있다.

**동적 연결 리스트를 이용**하여 구현하는 방법을 의미한다.

구현이 복잡하다는 단점이 있지만 **메모리를 효율적으로 사용한다는 장점**을 가진다.

*Python 내장 메소드로 pop(), push() 가 존재하므로,*

*개인적으로 만드는 함수는 my_pop(), my_push() 이런 식으로 구현하여 겹치지 않도록 주의한다.*

### 스택의 응용

1. **괄호 검사**

괄호의 짝을 맞추는 문제가 있다.

**괄호의 짝이 맞지 않으면 0, 맞으면 1을 출력**한다.

```python
txt = input()

top = -1
stack = [0] * 100

ans = 1
for x in txt:
    if x == '(':    # 여는 괄호 push
        top += 1
        stack[top] = x
    elif x == ')':  # 닫는 괄호인 경우
        if top == -1:   # 스택이 비어있으면 (여는 괄호가 없으면 )
            ans = 0
        else:           # 여는 괄호 하나 버림
            top -= 1    # pop
if top != -1:   # 여는 괄호가 남아있으면
    ans = 0

print(ans)
```

1. **Function Call**

프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리

→ 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 **후입 선출 구조**이므로, 후입 선출 구조의 스택을 이용하여 수행 순서 관리

→ 함수 호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 **스택 프레임(stack frame)**에 저장하여 시스템 스택에 삽입

<aside>

*ex)* 함수 사용 시 스택 활용 예시

`main`에서 `F1`함수를 사용하고, `F1`에서는 `F2`함수를 사용한다.

그럼 `F2`함수가 제일 늦게 추가되었으므로,

`F2` → `F1` → `main` 순으로 실행된다.

각 함수의 실행이 끝나면 시스템 스택의 top 원소를 삭제 하면서 프레임에 저장되어 있던 복귀주소를 확인하고 복귀한다.

함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 된다.

</aside>

이 개념은 **재귀 호출**을 이해하기 위한 꼭 필요한 개념이다.

## 재귀 호출

필요한 함수가 자신과 같은 경우 자신을 다시 호출하는 구조

함수에서 실행해야 하는 작업의 특성에 따라 일반적인 호출 방식보다 재귀 호출 방식을 사용하여 함수를 만들면 프로그램의 크기를 줄이고 간단하게 작성한다.

### 피보나치 수열

```python
def fibo(n) :
    global cnt
    cnt += 1
    if n < 2 :
        return n
    else :
        return fibo(n-1) + fibo(n-2)

cnt = 0             # 호출 횟수 기록
print(fibo(10), cnt)
```

### 모든 배열 원소에 접근하기

```python
def f(i, N):
		if i == N:
				return
		else:
				print(arr[i])
				f(i+1, N)
```

*재귀함수는 남용하면 안된다!*

*1000번만 호출하더라도 에러가 발생한다. 상황에 따른 유연한 판단이 중요하다.*

*그리고, debugger를 사용해도 재귀함수 실행 과정을 파악하기에는 어려우니,*

*원리를 미리 파악하고 있는 것도 중요하겠다.*

## Memoization

앞의 예에서 피보나치 수를 구하는 함수를 재귀함수로 구현한 알고리즘은 문제가 있다.

**엄청난 중복 호출**이 존재한다는 것이다.

피보나치 수열을 재귀함수로 표현하면 시간 복잡도는 **Theta(2^n)**이 된다.

이를 해결하는 방안은 **Memoization**이 되겠다.

<aside>

**Memoization**

컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행 속도를 빠르게 하는 기술이다. **동적 계획법**의 핵심이 되는 기술이다.

</aside>

피보나치 수를 구하는 알고리즘에서 `fibo(n)` 의 값을 계산하자마자 저장하면, 실행시간을 **Theta(n)**으로 줄일 수 있다.

```python
# recursive 방식 fibo1()
def fibo1(n) :
    global cnt
    cnt += 1
    if n >= 2 and memo[n] == 0 :
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

n = 10
cnt = 0                 # 호출 횟수 기록
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1

print(fibo1(n), cnt)  # 55 19
```

## DP (Dynamic Programming)

동적 계획 (Dynamic Programming) 알고리즘은 그리디 알고리즘과 같이 **최적화 문제**를 해결하는 알고리즘이다.

동적 계획 알고리즘은 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘이다.

그럼 피보나치 수열에 DP를 적용해보자.

피보나치 수는 부분 문제의 답으로부터 본 문제의 답을 얻을 수 있으므로 “최적 부분 구조”로 이루어져 있다.

1. 문제를 부분 문제로 분할한다.

<aside>

`Fi(n)` 함수는 `Fi(n-1)`과 `Fi(n-2)`의 합

`Fi(n-1)` 은 `Fi(n-2)`과 `Fi(n-3)`의 합

…

`Fi(n)`은 `Fi(n-1)`, `Fi(n-2)`, …, `Fi(2)`, `Fi(1)`, `Fi(0)` 의 부분집합으로 나뉜다.

</aside>

1. 부분 문제로 나누는 일을 끝냈으면 가장 작은 부분 문제부터 해를 구한다.
2. 그 결과는 테이블에 저장하고, 테이블에 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 구한다.

| **테이블 인덱스** | **저장되어 있는 값** |
| --- | --- |
| [0] | 0 |
| [1] | 1 |
| [2] | 1 |
| [3] | 2 |
| [4] | 3 |
| … | … |
| [n] | fibo(n) |

```python
# iterative 방식 fibo2()
def fibo2(n) :
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1) :
        f[i] = f[i-1] + f[i-2]

    return f[n]

print(fibo2(10))
```

### DP의 구현 방식

**recursive** 방식 : `fb1()`

**iterative** 방식 : `fb2()` 

memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능 면에서 보다 효율적이다.

재귀적 구조는 내부에 시스템 호출 스택을 사용하는 **오버헤드가 발생**하기 때문이다.

## DFS (Depth First Search)

깊이 우선 탐색. 스택과 관련 있는 알고리즘

비선형 구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함.

다른 방법으로는 BFS (Breadth First Search), 너비 우선 탐색이 있다.

시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, **가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서** 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회 방법

가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 **후입 선출 구조의 스택 사용**

### DFS 알고리즘

시작 정점 v를 결정하여 방문한다.

정점 v에 인접한 정점 중에서

1. 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문한다.
    
    그리고 w를 v로 하여 다시 2를 반복한다.
    
2. 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2를 반복한다.

스택이 공백이 될 때까지 2. 를 반복한다.

### 연습문제

<aside>

연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열 해 놓은 것이다.

모든 정점을 깊이 우선 탐색하여 화면에 깊이 우선 탐색 경로를 출력하시오.

시작 정점을 1로 시작하시오.

1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

출력 결과는 다음과 같이 나타난다. → 1 2 4 6 5 7 3

</aside>

`adj_list` 를 만든다.

이 리스트는 각 정점을 행으로 놓고, 인접한 정점을 저장해 놓는다.

```python
def dfs(v, N):
    visited = [0] * (N + 1)  # 방문 표시
    stack = []

    while True:
        if visited[v] == 0:  # 첫 방문이면,
            visited[v] = 1
            print(v)
        for w in adj_list[v]:  # v에 인접하고 방문 안한 w가 있으면
            if visited[w] == 0:
                stack.append(v)  # 현재 정점 push
                v = w  # w로 이동
                break
        else:  # 더 이상 갈 곳이 없는 경우
            if stack:
                v = stack.pop()
            else:  # 스택이 비어 있으면,
                break

V, E = map(int, input().split())
graph = list(map(int, input().split()))
adj_list = [[] for _ in range(V+1)]  # 인접 리스트

for i in range(E):
    v, w = graph[i*2], graph[i*2+1]

    adj_list[v].append(w)
    adj_list[w].append(v)

dfs(1, V)
```

## 계산기

문자열로 된 계산식이 주어질 때, 스택을 이용하여 이 계산식의 값을 계산할 수 있다.

**문자열 수식 계산의 일반적 방법**은 다음과 같이 이뤄질 수 있다.

**step1. 중위 표기법의 수식을 후위 표기법으로 변경한다.**

**step2. 후위 표기법의 수식을 스택을 이용하여 계산한다.**

<aside>

**중위표기법 (infix notation)**

연산자를 피연산자의 가운데 표기하는 방법

**후위표기법 (postfix notation)**

연산자를 피연산자 뒤에 표기하는 방법

</aside>

### step1. 중위표기식의 후위표기식 변환 방법

<aside>

A*B-C/D

1단계 : **(** **(**A*B**)** **-** **(**C/D**)** **)**

2단계 : **(** **(**AB**)***  **(**CD**)/** **)-**

3단계 : AB*CD/-

</aside>

이런 식으로 되는 것이다.

스택을 이용하면 아래와 같이 정리할 수 있다.

<aside>

1. 입력 받은 중위 표기식에서 토큰을 읽는다.
2. 토큰이 피연산자이면 토큰을 출력한다.
3. 토큰이 연산자(괄호포함)일 때, 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고, 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop 한 후 토큰의 연산자를 push한다. 만약 top에 연산자가 없으면 push한다.
4. 토큰이 오른쪽 괄호이면 스택 top에 왼쪽 괄호가 올 때까지 스택에 pop연산을 수행하고 pop 한 연산자를 출력한다. 왼쪽 괄호를 만나면 pop만 하고 출력하지는 않는다.
5. 중위 표기식에 더 읽을 것이 없다면 중지하고, 더 읽을 것이 있다면 1부터 다시 반복한다.
6. 스택에 남아 있는 연산자를 모두 pop하여 출력한다.
    
    스택 밖의 왼쪽 괄호는 우선 순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선 순위가 가장 낮다.
    

| **토큰** | **isp (incoming priority)** | **icp (in-stack priority)** |
| --- | --- | --- |
| ) | - | - |
| *, / | 2 | 2 |
| +, - | 1 | 1 |
| ( | 0 | 3 |
</aside>

예시 문제를 풀어보자.

<aside>

(6+5*(2-8)/2) 수식을 예로 들어보자.

⇒ 6528-*2/+

</aside>

<aside>

2 + 3 * 4 / 5 → 234*5/+

2 + 3 * 4 + 5 → 234*+5+

</aside>

### step2. 후위 표기법의 수식을 스택을 이용하여 계산

<aside>

1. 피연산자를 만나면 스택에 push한다.
2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산 결과를 다시 스택에 push한다.
3. 수식이 끝나면, 마지막으로 스택을 pop하여 출력한다.
</aside>

예시 문제를 풀어보자.

<aside>

6528-*2/+

→ 6, 5, 2, 8 스택에 push된다.

stack [ **6 5 2 8** ]

→ **-** 연산 기호가 나왔으므로, 스택을 두 번 pop한다. 8, 2 순으로 pop이 이루어지고 2-8을 계산하고 push한다.

stack [ 6 5 **-6** ]

→ ***** 연산 기호가 나왔으므로, 스택을 두 번 pop한다. -6, 5 순으로 pop이 이루어지고 5*(-6)을 계산하고 push한다.

stack [ 6 **-30** ]

→ 2 스택에 push 된다.

stack [ 6 -30 **2** ]

→ / 연산 기호가 나왔으므로, 스택을 두 번 pop한다. 2, -30 순으로 pop이 이루어지고 -30/2를 계산하고 push한다.

stack [ 6 **-15** ]

→ + 연산 기호가 나왔으므로, 스택을 두 번 pop한다. -15, 6 순으로 pop이 이루어지고 6+(-15)를 계산하고 push한다.

stack [ **-9** ]

→ 더 이상 토큰이 없으므로 stack에 남은 한 값을 출력한다.

계산 결과 : **-9**

</aside>

```python
'''
(6+5*(2-8)/2)
6528-*2/+
'''
stack = [0]*100
top = -1
icp = {'(':3, '*':2, '/':2, '+':1, '-':1}
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}

fx = '(6+5*(2-8)/2)'
susik = ''
for x in fx:
    if x not in '(+-*/)':   # 피연산자
        susik += x
    elif x == ')':      # '('까지 pop()
        while stack[top] != '(':    # peek
            susik += stack[top]
            top -= 1
        top -= 1        # '(' 버림. pop
    else:   # '(+-*/'
        if top==-1 or isp[stack[top]] < icp[x]: # 토큰의 우선순위가 더 높으면
            top += 1    # push
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik += stack[top]
                top -= 1
            top += 1  # push
            stack[top] = x

print(susik)

#susik = '6528-*2/+'
for x in susik:
    if x not in '+-/*': # 피연산자면...
        top += 1            # push(x)
        stack[top] = int(x)
    else:
        op2 = stack[top]  # pop()
        top -= 1
        op1 = stack[top]  # pop()
        top -= 1
        if x=='+':  # op1 + op2
            top += 1                # push()
            stack[top] = op1 + op2
        elif x=='-':
            top += 1
            stack[top] = op1 - op2
        elif x=='/':
            top += 1
            stack[top] = op1 / op2
        elif x=='*':
            top += 1
            stack[top] = op1 * op2

print(stack[top])
```

## 백트래킹

백트래킹 기법은 해를 찾는 도중에 ‘막히면(즉, 해가 아니면)’ 되돌아가서 다시 해를 찾아 가는 기법이다.

백트래킹 기법은 최적화 (optimization) 문제와 결정 (decision) 문제를 해결할 수 있다.

<aside>

**결정 문제** : 문제의 조건을 만족하는 해가 존재하는지의 여부를 ‘yes’ 또는 ‘no’가 답하는 문제

*ex)* 미로 찾기, n-Queen 문제, Map coloring, 부분 집합의 합(Subset Sum) 문제 등

</aside>

### 백트래킹과 깊이우선탐색과의 차이

어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄인다. (**Prunning 가지치기**)

깊이우선탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단한다.

깊이우선탐색을 가하기에는 경우의 수가 너무나 많다. 즉 N! 가지의 경우의 수를 가진 문제에 대해 깊이우선탐색을 가하면 당연히 처리 불가능한 문제이다.

백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 **최악의 경우에는 여전히** **지수함수 시간**(Exponential Time)을 요하므로 처리 불가능하다.

### 백트래킹 기법

어떤 노드의 유망성을 점검한 후에 유망(promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 간다.

어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 한다.

<aside>

**가지치기(prunning)**

유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않는다.

</aside>

백트래킹은 다음과 같은 절차로 진행된다.

<aside>

1. 상태 공간 트리의 깊이 우선 검색을 실시한다.
2. 각 노드가 유망한 지를 점검한다.
3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속한다.
</aside>

### 미로찾기

더 이상 진행할 수 없으면 진행할 수 있는 상태로 되돌아가면 된다. (stack의 pop을 이용한다.)

…

## 부분집합

어떤 집합의 공집합과 자기자신을 포함한 모든 부분집합을 **powerset**이라고 하며 구하고자 하는 어떤 집합의 원소 개수가 n일 경우 부분집합의 개수는 2^n개이다.

백트래킹 기법으로 **powerset**을 만들어 보자.

*예전에 앞에서 봤던 이진법을 이용하는 내용이 적용되는 것 같다.*

## 순열1

단순하게 순열을 생성하는 방법은 아래와 같이 표현할 수 있을 것이다.

<aside>

*ex)* 집합 (1, 2, 3}에서 모든 순열을 생성하는 함수

동일한 숫자가 포함되지 않았을 때, 각 자리 수 별로 loop를 이용해 구현할 수 있다.

```python
for i1 in range(1, 4):
		for i2 in range(1, 4):
				if i2 != i1:
						for i3 in range(1, 4):
								if i3 != i1 and i3 != i2:
										print(i1, i2, i3)
```

</aside>

백트래킹을 이용하여 {1, 2, 3, …, NMAX}에 대한 순열을 구해보자.

아래 코드와 위의 코드를 비교해보자.

```python
def backtrack(a, k, n):  # a 주어진 배열, k 결정할 원소, n 원소 개수
    c = [0] * MAXCANDIDATES

    if k == n:
        process_solution(a, k)  # 답이면 원하는 작업을 한다
    else:
        ncandidates = construct_candidates(a, k, n, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k + 1, n)
            
def construct_candidates(a, k, n, c):   # 후보 추천천
    c[0] = True                             # 원소의 포함 여부 
    c[1] = False
    return 2

def process_solution(a, k):
    for i in range(k):
        if a[i]:
            print(num[i], end = ' ')
    print()

MAXCANDIDATES = 2
NMAX = 4
a = [0] * NMAX
num = [1,2,3,4]
backtrack(a, 0, 3)
```

```python
def backtrack(a, k, n):
    c = [0] * MAXCANDIDATES

    if k == n:
        for i in range(0, k):
            print(a[i], end=" ")
        print()
    else:
        ncandidates = construct_candidates(a, k, n, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k + 1, n)

def construct_candidates(a, k, n, c):
    in_perm = [False] * (NMAX + 1)

    for i in range(k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, NMAX + 1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates

MAXCANDIDATES = 3
NMAX = 3
a = [0]*NMAX
backtrack(a, 0, 3)

```

## 가지치기

```python
def f(i, k, s, t):  # i원소, k 집합의 크기, s i-1까지 고려된 합, t목표
    global cnt
    global fcnt
    fcnt += 1
    if s > t:   # 고려한 원소의 합이 찾는 합보다 큰경우
        return
    elif s == t:    # 남은 원소를 고려할 필요가 없는 경우
        cnt += 1
        return
    elif i == k:    # 모든원소 고려
        return
    else:
        bit[i] = 1
        f(i+1, k, s+A[i], t)    # A[i] 포함
        bit[i] = 0
        f(i+1, k, s, t)         # A[i] 미포함

#A = [1,2,3,4,5,6,7,8,9,10]
N = 10
A = [ i for i in range(1, N+1)]

key = 55
cnt = 0
bit = [0]*N
fcnt = 0
f(0,N,0,key)
print(cnt, fcnt)      # 합이 key인 부분집합의 수
```

## 순열2

<aside>

{1, 2, 3}을 순열로 만드는 방법

**i = 0** : [1, 2, 3] j=0 → [**2**, **1**, 3] j=1 (i와 바꿈) → [**3**, 2, **1**] j=2 (i와 바꿈)

**i = 1 (1)** : [1, 2, 3] j=1 → [1, **3**, **2**] j=2 (i와 바꿈)

**i = 1 (2)** : [2, 1, 3] j=1 → [2, **3**, **1**] j=2 (i와 바꿈)

**i = 1 (3)** : [3, 2, 1] j=1 → [3, **1**, **2**] j=2 (i와 바꿈)

**i = 2 (1)** : [1, 2, 3] j=2

… 모두 그대로임.

총 6개가 나온다.

</aside>

```python
def f(i, N):    # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    if i == N:  #
        print(p)
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N)   # i+1자리 결정
            p[i], p[j] = p[j], p[i]

p = [1, 2, 3]
N = 3
f(0, N)
```

### 순열 문제에서의 가지치기

<aside>

NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.

조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.

예를 들어 다음과 같이 배열이 주어진다.

2 1 2

5 8 5

7 2 2

이 경우 1, 5, 2를 고르면 합이 8로 최소가 된다.

</aside>

이 문제는 완전 탐색으로 풀이 가능할 것이다.

P[ ] 만들어, 각 행에서 고른 열 번호를 저장하는 리스트로 선정한다. (열 번호는 겹치면 안된다.)

백트래킹과 순열 만드는 원리를 이용하면 아래와 같이 코드를 짜볼 수 있겠다.

```python
T = int(input())
def f(i, N, s):    # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    global min_v
    if i == N:
        min_v = min(min_v, s)

    elif min_v < s:  # 중간 합계가 최소합보다 크면
        return

    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]     # 자리 교환
            f(i+1, N, s + arr[i][p[i]])   # i+1자리 결정
            p[i], p[j] = p[j], p[i]     # 원상 복구

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    p = [i for i in range(N)]
    min_v = 10000
    f(0, N, 0)
    print(f'#{test_case} {min_v}')
```