## 분할 정복

문제를 분할해서 해결하는 분할 정복 기법을 이해한다.

대표적인 알고리즘인 **퀵 정렬, 병합 정렬, 이진 검색**에 대해 학습한다.

<aside>

*ex) 가짜 동전 찾기*

n개의 동전들 중에 가짜 동전이 하나 포함되어 있다. 가짜 동전은 진짜 동전에 비해 아주 조금 가볍다. 진짜 동전들의 무게가 동일하다고 할 때 양팔 저울을 이용해서 가짜 동전을 찾아보자.

양팔 저울을 최소로 해서 가짜 동전을 찾는 방법은 무엇인가?

예를 들어 동전이 24(진짜 23, 가짜 1)개 있다면?

</aside>

이러한 문제를 해결할 때 전략은 아래와 같다.

- **분할 (Divide)** : 해결할 문제를 여러 개의 작은 부분으로 나눈다.
- **정복 (Conquer)** : 나눈 작은 문제를 각각 해결한다.
- **통합 (Combine)** : (필요하다면) 해결된 해답을 모은다.

분할 정복 기법을 거듭 제곱 문제를 통해 이해해보자.

자연수 C의 n 제곱 값을 구하는 함수를 구현해보자.

```python
def Recursive_Power(x, n):
		if n == 1:
			return x
		
		if n // 2 == 0:
			y = Recursive_Power(x, n//2)
			return y * y
	
		else:
			y = Recursive_Power(x, (n-1)//2)
			return y * y * x
```

→ **O(logn)**

*이런 식으로 쪼개는 기법을 사용해서 문제를 효율적으로 푸는 방법이라고 알면 된다.*

## 병합 정렬 (Merge Sort)

여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식

**분할 정복 알고리즘**을 활용한다.

- 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어낸다.
- top-down 방식

시간 복잡도는 **O(nlogn)** 이다.

<aside>

*ex) **{69, 10,30, 2, 16, 8, 31, 22}** 병합 정렬 과정*

→ 분할 단계 : 전체 자료 집합에 대하여, **최소 크기의 부분집합이 될 때까지** 분할 작업을 계속한다.

{ 69, 10,30, 2, 16, 8, 31, 22 }

{ [ 69, 10, 30, 2 ] , [ 16, 8, 31, 22 ] }

{ [ 69, 10 ], [ 30, 2 ], [ 16, 8 ], [ 31, 22 ] }

{ [ 69 ], [ 10 ], [ 30 ], [ 2 ], [ 16 ], [ 8 ], [ 31 ], [ 22 ] }

→ 병합 단계 : 2개의 부분집합을 정렬하면서 하나의 집합으로 병합한다.

{ [ 69 ], [ 10 ], [ 30 ], [ 2 ], [ 16 ], [ 8 ], [ 31 ], [ 22 ] }

{ [ 10, 69 ], [ 2, 30 ], [ 8, 16 ], [ 22, 31 ] }

{ [ 2, 10, 30, 69 ] , [ 8, 16, 22, 31 ] }

**{ 2, 8, 10, 16, 22, 30, 31, 69 }**

</aside>

```python
# 1. 분할: 리스트의 길이가 1일 때까지 분할
# 2. 정복: 리스트의 길이가 1이 되면 자동으로 정렬됨
# 3. 병합
#   - 왼쪽, 오른쪽 리스트 중
#       작은 원소부터 정답 리스트에 추가하면서 진행
def merge(left, right):
    result = [0] * (len(left) + len(right))
    l = r = 0

    # 두 리스트에서 비교할 대상이 남아있을 때까지 반복
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    # 왼쪽 리스트에 남은 데이터들을 모두 result에 추가
    while l < len(left):
        result[l + r] = left[l]
        l += 1

    # 오른쪽 리스트에 남은 데이터들을 모두 result에 추가
    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result

def merge_sort(li):
    if len(li) == 1:
        return li

    # 1. 절반 씩 분할
    mid = len(li) // 2
    left = li[:mid]    # 리스트의 앞쪽 절반
    right = li[mid:]   # 리스트의 뒤쪽 절반

    left = merge_sort(left)
    right = merge_sort(right)

    # print(left, right)

    # 분할이 완료되면
    # 2. 병합
    merged_list = merge(left, right)

    return merged_list

arr = [69, 10, 30, 2, 16, 8, 31, 22]
sorted_arr = merge_sort(arr)

print(*sorted_arr)
```

## 퀵 정렬

주어진 배열을 두 개로 분할하고, 각각을 정렬한다.

병합 정렬과 다른 점은 아래와 같다.

1. 병합 정렬은 그냥 두 부분으로 나누는 반면, 퀵 정렬은 분할 할 때, **기준 아이템(pivot item) 중심으로 분할**한다. → **Partitioning**이라는 과정을 반복함.
2. 각 부분 정렬이 끝난 후, 병합 정렬은 “병합”이란 후처리 작업이 필요하나, 퀵 정렬은 필요로 하지 않는다.

시간 복잡도는 평균적으로 **O(nlogn)**이다. (최악의 경우에는 O(n^2))

### Partitioning

1. 작업 영역을 정한다.
2. 작업 영역 중 가장 왼족에 있는 수를 Pivot이라고 하자. (Pivot을 기준으로 해석한다.)
    
    → Pivot은 중간값, 우측 끝값으로 설정해도 상관은 없지만, 설명에서는 왼쪽으로 놓는다.
    
3. Pivot을 기준으로 **좌측에는 Pivot보다 작은 수**를 배치한다. **우측에는 Pivot보다 큰 수를 배치**시킨다.
4. 파티셔닝이 끝나고 Pivot의 위치는 확정(Fix)된다.
    
    → 정렬이 다 되었을 때에도 Pivot의 위치는 지금 위치 그대로 배정된다.
    

```python
# 피벗: 제일 왼쪽 요소
def hoare_partitioning(left, right):
    pivot = arr[left]

    i = left + 1
    j = right

    while i <= j:
        # i는 큰 값을 검색하면서 오른쪽으로 진행
        while i <= j and arr[i] <= pivot:
            i += 1
        # j는 작은 값을 검색하면서 왼족으로 진행
        while i <= j and arr[j] >= pivot:
            j -= 1

        # sWAP
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # pivot 위치를 확정시켜주기 (j와 바꾸기)
    arr[left], arr[j] = arr[j], arr[left]
    return j

# left, right : 작업 범위
def quick_sort(left, right):
    if left < right:
        # pivot을 기준으로 정렬시킨다.
        pivot = hoare_partitioning(left, right)
        # 왼쪽 진행
        quick_sort(left, pivot-1)
        # 오른쪽 진행
        quick_sort(pivot + 1, right)

arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(0, len(arr)-1)
print(arr)
```

위에 있는 quick sort는 `hoare_partitioning`을 사용한다.

다른 파티셔닝으로 `Lomuto_partitioning` 이 있는데,

비교적 느리고, 최악의 경우는 위와 동일하다.

```python
def lomuto_partitioning(arr, p, r):
		x = arr[r]
		i = p-1
		
		for j in range(p, r):
				if arr[j] <= x:
						i++
						arr[i], arr[j] = arr[j], arr[i]
		arr[i+1], arr[r] = arr[r], arr[i+1]
		
		return i+1
```

아래와 같이 퀵 정렬의 특징을 정리해보자.

- **최악의 경우는 언제일까?**
    
    → **역순 정렬**이 되어 있을 때 최악의 성능 or **pivot 설정 잘못했을 때**
    
    → **O(n^2)**
    
    - `Hoare_partition`
        
        pivot 기준, i, j를 좌우 끝에서부터 가운데로 이동
        
    - `Lomuto_partition`
        
        pivot을 제일 우측, i,j를 왼쪽에서 같이 이동
        
- 퀵 정렬은 **평균적인 속도가 O(NlogN)**으로 빠르다.
- 특히 **대규모의 데이터일 때 효과적으로 동작**한다.

## 이진 탐색

자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함.

**이진 검색을 하기 위해서는 자료가 정렬된 상태**여야 한다.

- **검색 과정**
    1. 자료의 중앙에 있는 원소를 고른다.
    2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
    3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
    4. 찾고자 하는 값을 찾을 때까지 1. ~ 3. 과정을 반복한다.

<aside>

*ex) {2, 4, 7, 9, 11, 19, 23} → 이진 검색으로 7을 찾는 경우* 

{2, 4, 7, | **9**, 11, 19, 23}

{2, **4**, | 7, | 9, 11, 19, 23}

{2, 4, | **7**, | 9, 11, 19, 23}

</aside>

```python
def binary_search_while(target):
    left = 0
    right = len(arr) - 1
    cnt = 0

    while left <= right:
        mid = (left + right) // 2
        cnt += 1

        if arr[mid] == target:
            return mid, cnt      # mid index 에서 검색 완료! (index, cnt)

        # 왼쪽에 정답이 있다.
        if target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1, cnt      # 찾지 못했을 경우

def binary_search_recur(left, right, target):
    global cnt
    # left, right를 작업 영역으로 검색
    # left <= right 만족하면 반복
    if left > right:
        return -1, cnt

    mid = (left + right) // 2
    cnt += 1
    # 검색하면 종료
    if target == arr[mid]:
        return mid, cnt
    # 한 번 할 때마다 left와 right를 mid 기준으로 이동시켜 주면서 진행
    # 왼쪽을 봐야한다.
    if target < arr[mid]:
        return binary_search_recur(left, mid - 1, target)
    else:
        return binary_search_recur(mid + 1, right, target)

arr = [4, 2, 9, 7, 11, 23, 19]

# 이진 검색은 항상 정렬된 데이터에 적용해야 한다!
arr.sort()

print(f'9 - {binary_search_while(9)}')      # 9 - (3, 1)
print(f'2 - {binary_search_while(2)}')      # 2 - (0, 3)
print(f'20 - {binary_search_while(20)}')    # 20 - (-1, 3)

cnt = 0
print(f'9 - {binary_search_recur(0, len(arr)-1, 9)}')   # 9 - (3, 1)
cnt = 0
print(f'2 - {binary_search_recur(0, len(arr)-1, 2)}')   # 2 - (0, 3)
cnt = 0
print(f'20 - {binary_search_recur(0, len(arr)-1, 20)}') # 20 - (-1, 3)
```

## 분할 정복 알고리즘 정리

- **병합 정렬**
    - 외부 정렬(External Sort)의 기본이 되는 정렬 알고리즘이다.
    - 멀티코어(Multi-Core) CPU나 다수의 프로세서에서 정렬 알고리즘을 병렬화하기 위해 병합 정렬 알고리즘이 활용된다.
- **퀵 정렬**
    - 매우 큰 입력 데이터에 대해서 좋은 성능을 보이는 알고리즘이다.
- **이진 검색**
    - 정렬된 데이터를 기준으로 특정 값이나 범위를 검색하는 데 사용
    - [이진 검색을 활용한 심화 학습 키워드] Lower Bound, Upper Bound
        - 정렬된 배열에서 특정 값 이상(이하)가 처음으로 나타나는 위치를 찾는 알고리즘
        - 특정 데이터의 범위 검색 등에서 활용