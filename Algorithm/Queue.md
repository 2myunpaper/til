<aside>

**큐 (Queue)**

FIFO (First In First Out) - 가장 먼저 삽입된 데이터가 먼저 삭제되는 구조

*ex) 너비 우선 탐색 (BFS) 알고리즘, 작업 스케줄링, 캐시 구현*

</aside>

## 큐(Queue)

스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조

→ 큐의 뒤에서는 삽입만 하고, 큐의 앞에서는 삭제만 이루어지는 구조

**선입선출구조 (FIFO : First In First Out)**

<aside>

**※ 스택 (Stack) → LIFO : Last In First Out, 후입선출**

</aside>

→ 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입된 원소는 가장 먼저 삭제 된다.

### 큐의 구조

머리(**Front**)와 꼬리(**Rear**)가 존재함.

삽입은 **enQueue**, 삭제는 **deQueue** 라고 칭한다.

### 큐의 주요 연산

| **연산** | **기능** |
| --- | --- |
| `enQueue(item)` | 큐의 뒤쪽에 원소를 삽입하는 연산 |
| `deQueue()` | 큐의 앞쪽에서 원소를 삭제하고 반환하는 연산 |
| `createQueue()` | 공백 상태의 큐를 생성하는 연산 |
| `isEmpty()` | 큐가 공백 상태 인지를 확인하는 연산 |
| `isFull()` | 큐가 포화 상태 인지를 확인하는 연산 |
| `Qpeek()` | 큐의 앞쪽에서 원소를 삭제 없이 반환하는 연산 |

## 큐의 구현

### 선형 큐

1차원 배열을 이용한 큐, 큐의 크기 = 배열의 크기

<aside>

**front** : 저장된 첫 번째 원소의 인덱스

**rear** : 저장된 마지막 원소의 인덱스

초기 상태 : front = rear = -1

공백 상태 : front == rear

포화 상태 : rear == n-1 (n: 배열의 크기, n-1: 배열의 마지막 인덱스)

</aside>

**삽입 :** `enQueue(item)`

마지막 원소 뒤에 새로운 원소를 삽입하기 위해,

rear 값을 하나 증가 시켜 새로운 원소를 삽입할 자리를 마련.

그 인덱스에 해당하는 배열 원소 `Q[rear]` 에 item을 저장.

**삭제 :** `deQueue()`

가장 앞에 있는 원소를 삭제하기 위해,

front 값을 하나 증가 시켜 큐에 남아있는 첫 번째 원소 이동

새로운 첫 번째 원소를 리턴 함으로써 삭제와 동일한 기능함

**공백 상태 및 포화 상태 검사 :** `isEmpty()`, `isFull()`

공백 상태 : `front == rear`

포화 상태 : `rear == n-1` (n: 배열의 크기, n-1: 배열의 마지막 인덱스)

`Qpeek()`

가장 앞에 있는 원소를 검색하여 반환하는 연산

현재 front의 한자리 뒤(front+1)에 있는 원소, 즉 큐의 첫 번째에 있는 원소를 반환

```python
# 방법 1.
# 큐 생성
queue = [0] * 3
front = rear = -1

# 1,2,3 enQueue
rear += 1           # enQueue 1
queue[rear] = 1

rear += 1           # enQueue 2
queue[rear] = 2

rear += 1           # enQueue 3
queue[rear] = 3

# deQueue
while front != rear:    # 큐에 원소가 남아있으면
    front += 1
    t = queue[front]
    print(t)

# 위와 같이 큐를 구현하면,
# 사실 큐에 있는 데이터는 삭제된 게 아니라, 인덱스만 변한 것이다.
print(queue)  # [1, 2, 3]
```

```python
# 방법 2.
q = []
q.append(1)  # enQueue 1
q.append(2)  # enQueue 2
q.append(3)  # enQueue 3
print(q.pop(0))  # deQueue
print(q.pop(0))
print(q.pop(0))
print(q)  # []
```

*방법2가 방법1보다 효율적으로 보이지만, 사실 그렇지 않다!*

*이유에 대해서는 뒤에서 배울 예정.*

## 원형 큐

### 선형 큐 이용 시의 문제점

선형 큐를 이용하여 원소의 삽입과 삭제를 계속할 경우,

배열의 앞 부분에 활용할 수 있는 공간이 있음에도 불구하고,

`rear = n-1`인 상태 즉, 포화 상태로 인식하여 더 이상의 삽입을 수행하지 않게 된다.

해결 방법은 아래와 같다.

<aside>

**해결 방법 1.**

매 연산이 이루어질 때마다 저장된 원소들을 배열의 앞 부분으로 모두 이동 시킴

→ 원소 이동에 많은 시간이 소요되어 큐의 효율성이 급격히 떨어진다.

**해결 방법 2.**

1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 **원형 형태의 큐**를 이룬다고 가정하고 사용.

</aside>

### 원형 큐의 구조

<aside>

- **초기 공백 상태**
    
    `front = rear = 0`
    
- **Index의 순환**
    
    front와 rear의 위치가 배열의 마지막 인덱스인 n-1을 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야 함.
    
    이를 위해 나머지 연산자 mod를 사용한다.
    
- **front 변수**
    
    공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠.
    
- **삽입 위치 및 삭제 위치**
    
    
    | **큐 종류** | **삽입 위치** | **삭제 위치** |
    | --- | --- | --- |
    | 선형큐 | `rear = rear + 1`  | `front = front + 1` |
    | 원형큐 | `rear = (rear + 1) mod n`  | `front = (front + 1) mod n` |
</aside>

연산 과정은 아래와 같이 진행된다.

<aside>

`create Queue`

| [1] | [2] |
| --- | --- |
| [0] **front, rear** | [3] |

→ `enQueue(A)`

| [1] : A **rear** | [2] |
| --- | --- |
| [0] **front** | [3] |

→ `enQueue(B)`

| [1] : A | [2] B **rear** |
| --- | --- |
| [0] **front** | [3] |

→ `deQueue()`

| [1] **front** | [2] B **rear** |
| --- | --- |
| [0] | [3] |

→ `enQueue(C)`

| [1] **front** | [2] B |
| --- | --- |
| [0] | [3] C **rear** |

→ `enQueue(D)`

| [1] **front** | [2] B |
| --- | --- |
| [0] D **rear** | [3] C |

→ Queue는 Full

</aside>

**공백 상태 및 포화 상태 검사 :** `isEmpty()`, `isFull()`

공백 상태 : `front == rear`

포화 상태 : 삽입할 rear의 다음 위치 == 현재 front → `(rear + 1) mod n == front`

**삽입 :** `enQueue(item)`

마지막 원소 뒤에 새로운 원소를 삽입하기 위해

rear 값을 조정하여 새로운 원소를 삽입할 자리를 마련한다.

`rear = (rear+1) mod n`

그 인덱스에 해당하는 배열 원소 `Q[rear]` 에 item을 저장

**삭제 :** `deQueue()` , `delete()`

가장 앞에 있는 원소를 삭제하기 위해

front 값을 조정하여 삭제할 자리를 준비함

새로운 front 원소를 리턴 함으로써 삭제와 동일한 기능함

## 연결 큐

**단순 연결 리스트(Linked List)를 이용한 큐**

연결 리스트는 값과, 다음 리스트의 주소 값을 담고 있음.

### 연결 큐의 구조

<aside>

- **큐의 원소** : 단순 연결 리스트의 노드
- **큐의 원소 순서** : 노드의 연결 순서. 링크로 연결되어 있음
- **front** : 첫 번째 노드를 가리키는 링크 (주소 값)
- **rear** : 마지막 노드를 가리키는 링크 (주소 값)
- **상태 표현**
    
    초기 상태 : `front = rear = null`
    
    공백 상태 : `front = rear = null`
    
</aside>

### 참고 : deque(덱)

컨테이너 자료형 중 하나

**양쪽 끝에서 빠르게 추가와 삭제를 할 수 있는 리스트류 컨테이너**

`append(x)` : 오른쪽에 x 추가

`popleft()` : 왼쪽에서 요소를 제거하고 반환. 요소가 없으면 IndexError

```python
from collections import deque

deque_q = deque()
for i in range(1000000):
    deque_q.append(1)
for i in range(1000000):
    deque_q.popleft()

print('end')  # 일반적인 큐보다 훨씬 빠르다.
```

## 우선순위 큐

우선순위를 가진 항목들을 저장하는 큐

FIFO 순서가 아니라 **우선순위가 높은 순서대로 먼저 나가게 된다.**

우선순위 큐의 적용 분야는,

시뮬레이션 시스템, 네트워크 트래픽 제어, 운영체제의 테스크 스케줄링 등이 존재한다.

우선순위 큐의 구현은 **배열**, **링크 리스트**로 구현할 수 있다.

**배열**을 이용하여 우선순위 큐를 구현하면,

원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조로 구현해야 한다.

가장 앞에 최고 우선순위의 원소가 위치하게 된다.

하지만 이에 대한 문제점은,

배열을 사용하므로, 삽입이나 삭제 연산이 일어날 때 원소의 재배치가 발생하고,

소요되는 시간이나 메모리 낭비가 크다.

그러므로 **링크 리스트**를 이용하는 것이 바람직 할 것이다.

## 버퍼 (Buffer)

데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역이다.

버퍼링이란 말은, 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미한다.

버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용된다.

순서대로 입력/출력/전달되어야 하므로 FIFO 방식의 자료구조인 큐가 활용된다.

예를 들어, 키보드 버퍼를 생각해보자.

A, P, S, enter 순 대로 입력을 받았다면,

프로그램에서는 입력 받은 순서대로 A, P, S enter에 해당되는 출력이 진행되어야 한다.

## BFS (Breadth First Search)

너비우선탐색은 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식.

인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비 우선탐색을 진행해야 하므로,

선입선출 형태의 자료구조인 큐를 활용함

<aside>

*ex)*

A

[ B C D ]

[ E F ] [ ] [ G H I ]

→ A, B, C, D, E, F, G, H, I 순으로 탐색하게 됨.

</aside>

```python
def BFS(G, v):  # 그래프 G, 탐색 시작점 v
    visited = [0] * (n + 1)     # n : 정점의 개수
    queue = []                  # 큐 생성
    queue.append(v)             # 시작점 v를 큐에 삽입
    while queue:                # 큐가 비어있지 않은 경우
        t = queue.pop(0)        # 큐의 첫번째 원소 반환
        if not visited[t] :     # 방문되지 않은 곳이라면
            visited[t] = True   # 방문한 것으로 표시
            visit(t)            # 정점 t에서 할 일
            for i in G[t]:      # t와 연결된 모든 정점에 대해
                if not visited[i]:  # 방문되지 않은 곳이라면
                    queue.append(i) # 큐에 넣기
```

*BFS는 목표점까지 최소한 1개를 지날 경우, 최소한 2개를 지날 경우 … 를 순서대로 조사하는 방법이나 다름없다.*

### 연습문제

<aside>

연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열 해 놓은 것이다. 모든 정점을 너비우선탐색 하여 경로를 출력하시오. 시작 정점을 1로 시작하시오.

→ 인접하는 점 정보 입력: 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7

</aside>

인접 리스트를 생성한다.

```python
'''
adj = [
    [],         # 0번행
    [2, 3],     # 1번행 - 1 정접과 이웃하는 정점
    [1, 4, 5],  # 2번행 - 2 정점과 이웃하는 정점
    ...         # n번행 - n 정점과 이웃하는 정점
]
'''

adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)    # 방향이 없는 경우
```

<aside>

NxN 크기의 미로에서 출발지 목적지가 주어진다.

이때 최소 몇개의 칸ㅇ르 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.

경로가 있는 경우 출발에서 도착까지 간느데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.

</aside>

```python
def bfs(i, j, N):
    # 준비
    visited = [[0]*N for _ in range(N)] # visited 생성
    q = []      # 큐생성
    q.append([i,j])# 시작점 인큐
    visited[i][j] = 1# 시작점 인큐 표시
    # 탐색
    while q:
        ti, tj = q.pop(0)   # 디큐
        if maze[ti][tj] == 3:   # visit(t)
            return visited[ti][tj] - 1 - 1 # 경로의 빈칸 수, -1 추가
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 미로내부고, 인접이고 벽이아니면,
            wi, wj = ti+di, tj+dj
            if 0<=wi<N and 0<=wj<N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                # 미로를 벗어나지 않고, 벽이 아니고,
                q.append([wi, wj])# 인큐
                visited[wi][wj] = visited[ti][tj] + 1   # 인큐 표시
    return 0

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

N = int(input())
maze = [list(map(int, input())) for _ in range(N)]
sti, stj = find_start(N)
ans = bfs(sti, stj, N)
print(ans)

```