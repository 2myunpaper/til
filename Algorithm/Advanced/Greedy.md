완전 검색/Greedy에 들어가기 전에, 

문제를 마주쳤을 때 생각해야 할 순서를 적어보자.

<aside>

1. 문제를 잘 읽어야 한다.
    - 숨겨진 규칙들이 없는가?
2. 완전 탐색
    - 단순 조건 및 반복문으로 구현이 가능한가?
    - 재귀 호출로 모든 경우를 본다면?

***시간, 공간이 부족하다면(그래프가 아닌 경우),***

1. 규칙성을 찾는다.
    - 문제에 숨겨진 규칙이나 패턴이 있는가? (예시를 잘 보자!)
    - 순간마다 최선의 선택이 정답이다. (Greedy)
2. 재계산을 하지 말자
    - 중복되는 문제의 결과를 저장해놓고 재활용하자 (DP)

---

***데이터 간 관계가 존재하면(그래프일 경우),***

1. 전체 노드를 탐색하자.
    - DFS : 가능한 경우 끝까지 탐색하면서 나아가자
    - BFS : 내 기준으로 퍼져나가면서 탐색하자

---

***N이 너무 크다 (새로운 알고리즘이나 자료구조를 고민해야 하는 단계)***

***알고리즘을 적용***

1. 재귀 호출 접근법의 경우
    - 백트래킹 (가지치기)
2. 정렬하자 (sort)
    - 최소값/구간, 최대값/구간 등
    - 내장 함수 `sort()` - O(NlogN) 이 보장되는 함수
    - 탐색해야 한다 : 이진 탐색
3. 심화 문제들
    - 최단 거리 : dijkstra
    - 최소 비용 : MST

***자료구조를 적용 (한 번 만들어 놓고 여러 번 조회한다.)***

- 이진 탐색 트리
- 힙 (우선순위 큐)
- 그룹화 (UNION-FIND)
- Trie, Segment Tree …
</aside>

## 반복과 재귀

반복과 재귀는 유사한 작업을 수행할 수 있다.

- **반복**은 수행하는 작업이 **완료될 때까지 계속 반복**하는 것이다.
- **재귀**는 주어진 문제의 해를 구하기 위해 **동일하면서 더 작은 문제의 해를 이용하는 방법**이다.

<aside>

*ex) 출력 11 12 13 21 22 23 … 33*

→ 2중 `for`문을 이용하면 된다.

*ex) 출력 1111 1112 1113 1121 1122 … 3333*

→ 4중 `for` 문을 이용하면 된다.

*ex) 출력 111111111 111111112 … 333333333*

→ 9중 `for` 문으로 해야 할까?

→ 재귀 함수로 `for` 문을 구현할 수 있겠다.

</aside>

### 함수의 특징

1. 함수를 호출할 때 쓰이는 변수와, 함수 선언에서 사용되는 매개변수는 다른 객체이다.
    
    ```python
    def KFC(x):  # 여기에서의 x와
    	x += 1
    	return x
    
    x = 3
    KFC(x)  # 여기에서의 x는 다른 객체이다.
    print(x)  # 3
    ```
    
2. 함수가 끝나면, main으로 되돌아 오는 것이 아니라, **해당 함수를 호출했던 곳으로 돌아온다.**

그럼 재귀 함수는 몇 번까지 돌릴 수 있을까? → 대략 1000번 정도 된다.

그러므로 재귀 함수를 구현할 때는,

조건과 실행이 잘 돌아가는 지 알아보기 위해, **디버깅**을 잘해주는 것이 중요하다.

*※ 참고로 Pycharm에서 디버깅 중 breakpoint 기준으로 다음 단계로 넘어가려면* `F9`*를 누르면 됨.*

```python
def KFC(num):
    # 언제 재귀호출을 중지할까?
    # 재귀호출의 특징1. 항상 종료 조건과 함께 한다.
    if num == 5:
        return

    print(num, end=' ')      # 재귀 호출 전 들어가야 할 로직
    KFC(num + 1)             # 다음 재귀 호출 (매개변수를 변경하면서 전달)
    print(num, end=' ')      # 돌아 오면서 해야 할 로직

KFC(0)
print("끝")

# 0 1 2 3 4 4 3 2 1 0 끝
```

재귀 함수 구조는 어떻게 보면, 트리 구조와 같다.

만약 재귀 함수로 2개를 그려본다면, 포화 이진 트리로 그려볼 수 있겠다.

```python
def KFC(num):
    if num == 5:  # 트리 구조에서의 높이를 결정
        return

    print(num, end=' ')
    KFC(num + 1)
    KFC(num + 1)  # 호출 개수 만큼 트리 구조에서의 가지 수를 결정
    print(num, end=' ')

KFC(0)
print("끝")
```

## 순열

서로 다른 N개에서, R개를 중복 없이, 순서를 고려하여 나열하는 것

→ 중복 순열을 구현해보고, 이후 중복이 없는 순열 구현을 학습한다.

### 중복 순열 구현

1. 재귀 호출을 할 때 마다, 이동 경로를 흔적으로 남긴다.
2. 가장 마지막 레벨에 도착했을 때, 이동 경로를 출력한다.

```python
# [0, 1, 2] 3개의 카드가 존재
# 2개를 뽑을 예정

path = []       # 뽑은 카드들을 저장
# cnt = 재귀호출마다 누적되어서 전달되어야 하는 값
def recur(cnt):
    # 카드를 2개 뽑으면 종료
    if cnt == 2:
        # 종료 시에 해야 할 로직들을 작성
        print(*path)
        return

    # # 1. 1개의 카드를 뽑는다
    # path.append(0)
    # # 2. 다음 재귀 호출 (뽑은 카드가 1개 추가되었다.)
    # recur(cnt + 1)
    # path.pop()  # 돌아왔을 때 카드 하나를 제거한다.
    #
    # path.append(1)
    # recur(cnt + 1)
    # path.pop()
    #
    # path.append(2)
    # recur(cnt + 1)
    # path.pop()

    for num in range(3):
        path.append(num)
        recur(cnt + 1)
        path.pop()

# 제일 처음 호출할 때 시점이므로
# 초기값을 전달하면서 시작
recur(0)
```

```python
path = []       
def recur(cnt):
    if cnt == 3: # 뽑을 카드 개수
        print(*path)
        return
		
		# 카드를 1~7중에서 뽑기
    for num in range(1, 7):
        path.append(num)
        recur(cnt + 1)
        path.pop()

recur(0)
```

### 중복을 제거

0을 선택하고 재귀 호출 한 후에는 또 다시 0을 선택하지 못하도록 막아야 한다.

```python
path = []
used = [False] * 7  # 1~6 숫자 사용 여부를 기록
# 0번 인덱스는 버림, 안 쓰기로 약속

# 조금 더 어려운 문제의 경우 (숫자 법위가 매우 크다)
# -> 위와 같은 리스트 방식은 메모리 초과 가능성이 존재
# -> dictionary(O(1)), set(O(1)) 이런 자료구조로 해결

def recur(cnt):
    if cnt == 3: # 뽑을 카드 개수
        print(*path)
        return
		
		# 카드를 1~7중에서 뽑기
    for num in range(1, 7):
			  # 이미 num을 뽑았다면 뽑지 마라
			  # == num을 뽑지 않았을 때만 뽑아라
			  # if num in path:
				#	    continue
				# 모든 path를 다 검토하는 것이므로, 시간 복잡도에서 불리함.
				
        if used[num] is True:
            continue

        used[num] = True
        path.append(num)
        recur(cnt + 1)
        used[path.pop()] = False

recur(0)
```

## 완전 탐색

**Brute-Force**, 모든 가능한 경우를 모두 시도를 해보아, 정답을 찾아내는 알고리즘

*ex) 자전거 열쇠 비밀번호 맞추기 (1111~9999)*

여러가지 예시 문제를 보면서 개념을 파악해보자.

<aside>

***ex) 3개의 주사위를 던져 나올 수 있는 중복 순열에 대해, 합이 10 이하가 나오는 경우는 총 몇 가지인가?***

→ 가능한 모든 케이스를 탐색한다. (완전 탐색 알고리즘이라고 한다.)

</aside>

```python
# 주사위 3개를 던져 합이 10 이하인 경우는 몇 개인가?
# 종료 조건 : 3번 던진다.
# 나올 수 있는 범위 : 주사위는 1~6

path = []
result = 0

def recur(cnt, total):
    global result

    # 기저 조건 : 이미 10을 넘으면 더 이상 볼 필요가 없다.
    # 경우의 수들을 많이 줄여주는 기법, 가지 치기
    if total > 10:
        return

    if cnt == 3:
        # 합이 10 이하인건 몇 개인가?
        # sum: path 길이만큼 반복되기 때문에 비효율(O(N))
        # if sum(path) <= 10:
        if total <= 10:
            result += 1
            print(path)
        return

    for num in range(1, 7):
        path.append(num)
        recur(cnt + 1, total + num) # 주사위 결과를 더해서 전달
        path.pop()

recur(0, 0)
```

<aside>

***ex) A, J, Q, K 네 종류의 카드들이 다량으로 쌓여져 있다. 이 중 5장의 카드를 뽑아 나열하고자 하는데, 같은 종류의 카드가 세 장 연속으로 나오는 경우의 수를 구하여라.***

→ [A, J, Q, K] 카드에 대해 [AAAAA ~ KKKKK] 까지 출력해보기.

→ 같은 종류의 카드가 연속 세 장이 나왔다면 Counting.

</aside>

```python
# 카드 5장을 뽑아라
# 5장 뽑았을 때, 연속된 3개가 나오면 counting

card = ['A', 'J', 'Q', 'K']
path = []
result = 0

def count_three():
    if path[0] == path[1] == path[2]: return True
    if path[1] == path[2] == path[3]: return True
    if path[2] == path[3] == path[4]: return True
    return False

def recur(cnt):
    global result

    if cnt == 5:
        # 연속된 3개가 나오면 counting
        if count_three():
            result += 1
            print(*path)
        return

    for idx in range(4):
        path.append(card[idx])
        recur(cnt + 1)
        path.pop()
        
recur(0)
```

*순열 문제는,*

1. *전체를 보고,*
2. *끝날 때 무언가 하고,*
3. *중복 제거를 하는*

*문제들로 구성되어 있으니 참고하자.*

<aside>

***ex) 0~9 번호가 적혀있는 카드가 6장 있다.***

***3장의 카드가 연속적인 번호를 갖는 경우 “run”이라고 하고, 3장의 카드가 동일한 번호를 갖는 경우는 “triplet”이라고 한다.***

***6장의 카드가 “run”과 “triplet”으로만 구성된 경우를 “baby-gin”으로 부른다.***

***baby-gin 여부를 판단하는 프로그램을 작성하라.***

→ 순서를 다 나열해보아야 한다.

→ 정렬을 먼저 해보아도 좋다.

</aside>

```python
# baby-gin 검사
# - 숫자 3개가 연속되었는가 (run)
# - 숫자 3개가 같은가 (triplet)
# 6자리 숫자를 입력
# -> 모든 순서를 보아야 한다 (순열)

'''
6 6 7 7 6 7
0 5 4 0 6 0
1 0 1 1 2 3
'''

path = []
used = [0] * 6
baby_gin_result = False

def is_baby_gin():
    cnt = 0
    # run + triplet 개수의 합 = 2
    # 앞쪽 숫자 3개 체크
    a, b, c = path[0], path[1], path[2]
    if a == b == c:  # triplet
        cnt += 1
    elif a == (b-1) == (c-2):  # run
        cnt += 1

    # 뒤쪽 숫자 3개 체크
    a, b, c = path[3], path[4], path[5]
    if a == b == c:  # triplet
        cnt += 1
    elif a == (b - 1) == (c - 2):  # run
        cnt += 1

    return cnt == 2

def recur(cnt):
    if cnt == 6:
        # baby-gin 인지 검사
        if is_baby_gin():
            pass
        return

    for idx in range(6):
        # idx를 이미 썼다면, 뽑지마라
        if used[idx]:
            continue

        used[idx] = 1
        path.append(arr[idx])
        recur(cnt + 1)
        path.pop()
        used[idx] = 0

# arr = list(map(int, input().split()))
arr = [6, 6, 7, 7, 6, 7]
recur(0)

print('YES') if baby_gin_result else print('NO')
```

## 부분집합

집합에 포함된 원소들을 선택하는 것 (공집합도 포함)

### 부분 집합을 찾아내는 구현 방법

아래 예시를 보면서 부분 집합을 구현해보자.

<aside>

*ex) 민철이에게는 세 명의 친구가 있다.*

*함께 영화관에 갈 수 있는 멤버를 구성 하고자 한다.*

*모든 경우를 출력해보자.*

</aside>

- **완전 탐색**
    
    **재귀 호출**을 이용한 완전 탐색 이용
    
    위의 예시에 적용하면,
    
    → O, X로 집합에 포함 시킬지 말지 결정하는 완전 탐색을 이용하여 구현한다.
    
    → Branch 2개, Level 3개
    
    ```python
    def recur():
    if # 3명을 판단했으면
    		return
    recur(포함하는 경우)
    recur(포함하지 않는 경우)
    ```
    
    위의 예시의 재귀 호출로 나타내면 아래와 같을 것이다.
    
    ```python
    # 완전 탐색을 이용한 예시 풀이
    arr = ['O', 'X']
    path = []
    name = ['MIN', 'CO', 'TIM']
    
    def print_name():
    		print('{ ', end = '')
    		for i in range(3):
    				if path[i] == 'O':
    						print(name[i], end = ' ')
    		print('}')
    
    def run(lev):
    		if lev == 3:
    				print_name()
    				return
    				
    		for i in range(2):
    				path.append(arr[i])
    				run(lev + 1)
    				path.pop()
    				
    run(0)
    ```
    
- **Binary Counting**
    
    2진수 & 비트연산을 이용하여, 부분 집합을 구할 수 있음.
    
    부분 집합이 필요할 때 사용하는 추천 방법
    
    위의 예시에 적용하면,
    
    → 원소 수에 해당하는 N개의 비트열을 이용한다.
    
    *→ ex) 000 → {}, 101 → {A,C} …*
    
    → 만들 수 있는 집합의 총 개수는 2^n이다.
    
    → `1<<n` 공식을 이용하여 빠르게 구할 수 있다.
    
    ```python
    arr = ['A', 'B', 'C']
    n = len(arr)
    
    def get_sub(tar):
        for i in range(n):
            if tar & 0x1:  # 각각 원소가 포함되어 있나요?
            # 1도 되고, 0b1도 되고, 0x1 도 되는데
            # 왜 0x1 인가?
            # 비트 연산임을 명시하는 권장하는 방법
                print(arr[i], end='')
            tar >>= 1  # 맨 우측 비트를 삭제한다 == 다음 원소를 확인하겠다.
    
    for tar in range(0, 1 << n):  # range(0, 8)
        print('{', end='')
        get_sub(tar)
        print('}')
    ```
    
    Binary Counting의 다른 예로 아래와 같은 코드를 만들어 볼 수 있겠다.
    
    ```python
    # *친구 5명 중 2명 이상의 친구와 영화를 보러 가는 경우의 수 구하기*
    arr = {'A', 'B', 'C', 'D', 'E'}
    arr_len = len(arr)
    
    def find_friends(tar):
        cnt = 0
        for _ in range(arr_len):
            if tar & 0x1:
                cnt += 1
            tar >>= 1
    
        # 같은 표현
        # for i in range(arr_len):
        #     if (tar << i) & 0x1:
        #         cnt += 1
    
        if cnt >= 2:
            return True
    
        return False
    
    ans = 0
    for i in range(1 << arr_len):
        if find_friends(i) is True:
            ans += 1
    
    print('경우의 수 :', ans)
    ```
    

## 조합

서로 다른 n개의 원소 중 r개를 순서 없이 골라낸 것을 조합(combination)이라고 부른다.

※ 순열과 조합 차이

- 순열 *ex) 1등, 2등, 3등 뽑기*
- 조합 *ex) 3명 뽑기*

조합도 마찬가지로 **재귀 호출**을 이용한다.

```python
arr = ['A', 'B', 'C', 'D', 'E']
n = 3
path = []

def recur(cnt, start):
    # N명을 뽑으면 종료
    if cnt == n:
        print(*path)
        return

    # 5명을 고려해야 한다
    # for i in range(이전에 뽑았던 인덱스 + 1부터, len(arr)):
    # start : 이전 재귀로부터 넘겨받아야 하는 값
    for i in range(start, len(arr)):
        path.append(arr[i])
        # i: i번째를 뽑겠다.
        # i + 1을 매개변수로 전달: 다음 재귀부터는 i+1부터 고려
        recur(cnt + 1, i + 1)
        path.pop()

recur(0, 0)
```

조합의 다른 예로 아래와 같은 코드를 만들어 볼 수 있겠다.

```python
# 주사위 눈금 N개를 던져서 나올 수 있는 모든 조합을 출력하시오.
N = 4
path = []

def recur(cnt, start):
    if cnt == N:
        print(path)
        return

    for i in range(start, 7):
        path.append(i)
        recur(cnt+1, i)
        path.pop()

recur(0, 1)
```

## Greedy

**현재 기준으로 가장 좋아 보이는 선택지로 결정**하여 답을 구하는 알고리즘

*도대체 어떤 문제가 그리디 문제인가?*

*그냥 무조건 최적해만 선택하면 되는건가?*

<aside>

조건을 확인하기 전에 선행되어야 할 것

- 규칙성을 찾아야 한다.
    
    → 규칙을 못 찾으면 못 푼다.
    
- 그리디로 풀 수 있는 조건
    1. **탐욕적 선택 조건 (Greedy Choice Property)**
        
        각 단계의 최적 해 선택이 이후 단계 선택에 영향을 주지 않는다.
        
        즉, 각 단계 규칙이 변하면 안된다.
        
    2. **최적 부분 구조 (Optimal Substructure)**
        
        각 단계의 최적 해 선택을 합하면, 전체 문제의 해결책이어야 한다.
        
    3. **반례 고려**
</aside>

그리디로 풀 수 있는 조건을 반영하여 아래 동전교환 예시를 보자.

<aside>

*ex) **10, 50, 100, 500**의 동전이 있다.*

*만약 1730원을 거슬러주기 위해 사용할 수 있는 최소 동전 수는 몇 개인가?*

1. **탐욕적 선택 조건**을 따져보자.
    
    → 첫 번째 단계 : 500원으로 가능한 만큼 주자
    
    → 두 번째 단계 : 남은 동전 중 가장 큰 동전인 100원
    
    → 각 단계를 진행하면서 규칙이 유지되었다.
    
2. **최적 부분 구조**를 따져보자.
    
    [명제] 가장 큰 동전부터 고르면 최소 동전 수가 나온다.
    
    [간접 증명] 가장 큰 동전부터 고르면 최적 해가 안 나온다고 가정
    
    → 작은 동전부터 골랐을 때 최적 해가 나온다고 가정
    
    → 더 작은 수로 나눴을 때 최소 몫이 나올 수 있다. ⇒ 가정에서 모순이 발생
    
    → 그러므로 명제는 참이다.
    
3. **반례**는 없는가?
    
    만약 동전이 10, 50, 70이 있고 100원을 거슬러 줘야 할 경우, 위의 가정을 사용한다면 최적 해가 나오지 않는다.
    
    → 이처럼 그리디 알고리즘은 쉬워 보이나 예외 없이 모든 경우가 맞는 규칙인지 아닌지 증명이 어렵다.
    
</aside>

반례를 적용하지 않은 코드는 아래와 같다.

```python
coin_list = [500, 100, 50, 10]      # 큰 동전 순으로 나열
target = 1730
cnt = 0

for coin in coin_list:
    possible_cnt = target // coin   # 현재 동전으로 가능한 최대 수
    cnt += possible_cnt             # 정답에 더해준다.
    target -= coin * possible_cnt   # 금액을 빼준다.
```

다른 문제를 살펴보자.

<aside>

*ex) 기숙사에는 하나의 화장실만 존재한다.*

*A ~ D 학생은 각자의 평균 화장실 사용 시간이 아래와 같다.*

***A : 15분, B : 30분, C : 50분, D : 10분***

*어떤 기준으로 접근해야, 대기 시간의 누적합이 최소가 될지 고민해보고 직접 구현해보자.*

→ 이 문제도 그리디로 풀 수 있는 조건들을 참고하여 풀이를 진행해야 한다.

</aside>

```python
people = [15, 30, 50, 10]
n = len(people)

# 규칙, 최소 시간인 사람부터 화장실로 들어가자.
people.sort()  # 오름차순 정렬

total_time = 0         # 전체 대기 시간
remain_people = n - 1  # 대기인원 수

for turn in range(n):
    time = people[turn]
    total_time += time * remain_people
    remain_people -= 1
print(total_time)
```

### Knapsack 문제

<aside>

*ex) 아래와 같이 물건들이 있다.*

|  | **무게** | **값** |
| --- | --- | --- |
| 물건1 | 5kg | 50만원 |
| 물건2 | 10kg | 60만원 |
| 물건3 | 20kg | 140만원 |

*물건은 하나씩만 존재하고, 최대 30kg까지 짐을 담고자 할 때, 어떤 물건을 담아야 최대로 수익을 낼 수 있을까?*

</aside>

이 문제는 kg 당 가치가 가장 높은 것을 먼저 담으면 안된다.

위의 답은 물건2와 물건3을 가져가는 것이 정답이지만,

kg당 값이 가장 높은 것은 물건1이라, 오류가 발생할 수 있다.

→ **0-1 Knapsack** 문제는 그리디로 해결할 수 없다. (각 물건을 한꺼번에 하나로 골라야 하는 경우)

반면, **Fractional Knapsack** 문제인 경우, (각 물건을 잘라서 고를 수 있는 경우)

0-1 Knapsack과 달리, 물건을 원하는 만큼 자를 수 있다.

|  | **무게** | **값** | **값/kg** |
| --- | --- | --- | --- |
| 물건1 | 5kg | 50만원 | 10만원/kg |
| 물건2 | 10kg | 60만원 | 6만원/kg |
| 물건3 | 20kg | 140만원 | 7만원/kg |

최대 수익은

kg당 금액이 가장 높은 물건 1, 전체 사용 (50만원)

두 번째로 kg당 금액이 높은 물건3, 전체 사용 (140