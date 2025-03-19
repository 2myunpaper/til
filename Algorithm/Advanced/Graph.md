## 그래프 기본

그래프는 아이템(사물 또는 추상적 개념)들과 이들 사이의 연결 관계를 표현한다.

정점(vertex)들의 집합과 이들을 연결하는 간선(Edge)들의 집합으로 구성된 자료 구조

**V** : 정점의 개수, **E** : 그래프에 포함된 간선의 개수

→ V 개의 정점을 가진 그래프는 **최대 V(V-1)/2 간선이 가능**하다

→ ex) 5개 정점이 있는 그래프의 최대 간선 수는 10(=5*4/2)개

선형 자료구조나 트리 자료구조로 표현하기 어려운 N:N 관계를 가지는 원소들을 표현하기에 용이함.

### 그래프 유형

- **무향** 그래프 (**Undirected** Graph)
    
    방향성이 없다. 양방향이다.
    
- **유향** 그래프 (**Directed** Graph)
    
    방향성이 존재한다.
    
- **가중치** 그래프 (**Weighted** Graph)
    
    간선에 가중치를 부여한다.
    
- **사이클 없는 방향** 그래프 (**DAG, Directed Acylic Graph**)
- **완전** 그래프
    
    정점들에 대해 가능한 모든 간선들을 가진 그래프
    
- **부분** 그래프
    
    원래 그래프에서 일부의 정점이나 간선을 제외한 그래프
    
- **인접 (Adjacency)**
    
    두 개의 정점에 간선이 존재(연결됨)하면 서로 인접해 있다고 한다.
    
    완전 그래프에 속한 임의의 두 정점들은 모두 인접해 있다.
    

### 그래프 경로

간선들을 순서대로 나열한 것

<aside>

*ex) 간선 표현*

*간선들 : (0, 2), (2, 4), (4, 6)*

*정점들 : 0 - 2 - 4 - 6*

</aside>

경로 중 한 정점을 최대한 한 번만 지나는 경로를 **단순 경로**라 한다.

시작한 정점에서 끝나는 경로를 **사이클(Cycle)**이라고 한다.

### 그래프 표현

간선의 정보를 저장하는 방식, 메모리나 성능을 고려해서 결정

- **인접 행렬 (Adjacent matrix)**
    
    V x V 크기의 2차원 배열을 이용해서 간선 정보를 저장. 배열의 배열 (포인터 배열)
    
    두 정점이 인접되어 있으면 1, 그렇지 않으면 0으로 표현
    
    무향 그래프이면, **i번째 행의 합 = i번째 열의 합 = Vi의 차수**
    
    유향 그래프이면, **행 i의 합 = Vi의 진출 차수, 열 i의 합 = Vi의 진입 차수**
    
    인접 행렬의 단점은,
    
    메모리 낭비가 너무 심하다는 것이다. 가지 못하는 경로도 저장되어 있기 때문이다.
    

- **인접 리스트 (Adjacent List)**
    
    인접 행렬의 메모리 낭비를 해결할 수 있다.
    
    각 정점마다 해당 정점으로 나가는 간선의 정보를 저장
    
    단점은,
    
    노드를 찾아가는 과정에서 시간 소요가 비교적 커질 수도 있다.
    
- **간선의 배열**
    
    간선(시작 정점, 끝 정점)을 배열에 연속적으로 저장
    

## DFS

<aside>

*ex) 친구관계 문제*

*친구 관계를 그래프로 표현하였다.*

*A로 시작해서 한 명의 친구에게만 소식을 전달, 전달 할 수 있다면 최대 몇 명의 친구가 소식을 전달 받을 수 있을까? (단, 소식을 전달 받은 친구한테는 소식을 재 전달 할 수 없다.)*

*A로 시작해서 친구들에게 동시에 소식을 전달할 수 있다고 할 때, 가장 늦게 전달 받는 사람은 누구일까? (단, 친구에게 소식을 전달하는 속도는 동일하다.)*

</aside>

위와 같은 문제를 해결하기 위해서는 그래프 순회가 필요하다.

그래프 순회는 비선형 구조인 그래프로 표현된 모든 자료(정점)를 빠짐없이 탐색하는 것을 의미한다.

그 중, 깊이 우선 탐색은, 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 **후입선출 구조의 스택을 이용**한다.

DFS를 구현하는 코드는 아래와 같다.

```python
def dfs(node):
    # 보통 그래프 문제들에서
    # ex) K개의 노드 방문했다면 종료
    # ex) N 개를 모두 방문했다면 경로 출력
    # if 종료 시 해야할 것들 or 가지치기:
    #       return

    print(node, end=" ")
    # visited[node] = 1  # 개발자마다 초기화 위치가 다르다.

    # 현재 노드에서 인접한 노드들을 모두 확인하면서, 한 군데로 진행
    for next_node in graph[node]:
        # 이미 방문했다면 가지마라!
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)
    # 언젠가 끝날 반복문이기 때문에 종료 조건을 따로 주지 않는다.
    # 허나 가지치기 코드는 입력한다.

N, M = map(int, input().split())
# 1. 그래프를 저장하기
#   - 비어있는 그래프를 생성한다.
#   - 그래프 정보를 입력받아 넣는다.
# graph = [[0] * (N + 1) for _ in range(N + 1)]  # 인접 행렬 (N * N 의 0배열)
graph = [[] for _ in range(N+1)]# 인접 리스트 (N * N ([]))

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)  # 양방향이라면, 뒤집어서 저장되 해주어야 한다.

visited = [0] * (N+1) # 방문 여부 기록
visited[1] = 1
dfs(1)
```

## BFS

너비 우선 탐색은 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 진행해야 하므로, **선입선출 형태의 자료구조인 큐를 활용**한다.

BFS를 구현하는 코드는 아래와 같다.

```python
def bfs(start_node):
    # q에 들어가는 노드들의 의미 : 다음에 방문해야 할 노드들(대기열)
    q = [start_node]    # 시작점을 넣은 상태로 출발

    while q:
        # 1. 가장 앞에 있는 노드를 뽑는다.
        # 2. 해당 노드에서 갈 수 있는 노드들을 queue 에 넣는다.
        now = q.pop(0)

        print(now, end=' ')

        # 인접한 노드들을 확인하면서
        for next_node in graph[now]:
            # 방문 했으면 pass
            if visited[next_node]:
                continue
            visited[next_node] = 1
            q.append(next_node)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)  # 양방향

visited[1] = 1
bfs(1)
```

## Union-Find (Disjoint set) - 서로소 집합

서로소 또는 상호배타 집합들은 서로 중복 포함된 원소가 없는 집합들이다. 다시 말해 **교집합이 없다.**

집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분한다. 이를 **대표자(representative)**라 한다.

- **상호배타 집합을 표현하는 방법**
    
    연결 리스트, 트리
    
- **상호배타 집합 연산**
    
    `Make-Set(x)` : 자기 자신을 대표자로 설정. x개의 집합을 생성
    
    `Find-Set(x)` : 대표자가 누구냐 물어보는 것
    
    `Union(x, y)` : x, y를 하나의 집합으로 묶어주는 것.
    
- **연산의 효율**을 높이는 방법
    - **Rank를 이용한 Union**
        
        각 노드는 자신을 루트로 하는 subtree의 높이를 랭크(Rank)라는 이름으로 저장한다.
        
        두 집합을 합칠 때 rank가 낮은 집합을rank가 높은 집합에 붙인다.
        
    - **Path compression**
        
        Find-Set을 행하는 과정에서 만나는 모든 노도들이 직접 root를 가리키도록 포인터를 바꾸어 준다. 
        

```python
# 6개의 원소(1~6)이 존재하는 경우
# 1. 각 집합을 만들어 주는 함수
def make_set(n):
    # 1~n 까지의 원소가 있다고 가정 -> 총 n 개의 집합을 생성
    # --> 각 원소의 부모(!= 대표자)를 자신으로 초기화
    parents = [i for i in range(n + 1)]
    ranks = [0] * (n + 1)  # rank 를 모두 0으로 초기화
    return parents, ranks

# def find_set(x):
#     # 자신 == 부모노드 -> 해당 집합의 대표자다
#     if parents[x] == x:
#         return x
#
#     # x의 부모노드를 기준으로 다시 대표자를 검색
#     return find_set(parents[x])

# # 경로 압축 추가
# def find_set(x):
#     if parents[x] == x:
#         return x
#
#     # 경로 압축 (path compression)를 통해
#     # x의 부모를 대표자로 변경
#     # parents[x] = find_set(parents[x])
#
#     return parents[x]

# 할 때 마다, 모든 노드의 대표자를 변경하자!
def find_set(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]  # 경로 압축
        x = parents[x]
    return x

def union(x, y):
    # 1. x, y 의 대표자를 검색
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 만약 이미 같은 집합이라면 ?
    # -> 끝!
    if ref_x == ref_y:
        return

    # 다른 집합이라면 합친다
    # -> 문제에 따라 우선되는 집합으로 합쳐주면 된다.
    # --> 이번 예시: 더 작은 노드로 합친다.
    # if ref_x < ref_y:
    #     parents[ref_y] = ref_x
    # else:
    #     parents[ref_x] = ref_y

    # rank 가 작은 쪽으로 병합
    if ranks[ref_x] < ranks[ref_y]:
        parents[ref_x] = ref_y
    elif ranks[ref_x] > ranks[ref_y]:
        parents[ref_y] = ref_x
    else:
        # rank 가 같으면 한 쪽으로 병합하고, 대표자의 rank 증가
        parents[ref_y] = ref_x
        ranks[ref_x] += 1

N = 6
parents, ranks = make_set(N)

union(1, 3)
union(2, 3)
union(5, 6)

print(parents)

# 3과 5는 같은 집합인가요 ??
# if parents[3] == parents[5]   => 대표자가 아니라 부모 노드를 기준으로 비교
if find_set(3) == find_set(5):
    print("같은 집합입니다,")
else:
    print("다른 집합입니다.")
```