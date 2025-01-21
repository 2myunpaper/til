## Sequence Types

### list

여러 개의 값을 순서대로 저장하는 **변경 가능한 시퀀스 자료형**

```python
my_list_1 = []
my_list_2 = [1, 'a', 3, 'b', 5]
my_list_3 = [1, 2, 3, 'Python', ['hello', 'world']]
```

리스트 안에는 여러 타입이 들어갈 수 있음.

리스트 안에 리스트가 들어갈 수도 있음.

```python
my_list = [1, 'a', 3, 'b', 5]

# 인덱싱
print(my_list[1])  # a

# 슬라이싱
print(my_list[2:4])  # [3, 'b']
print(my_list[:3])  # [1, 'a', 3]
print(my_list[3:])  # ['b', 5]
print(my_list[0:5:2])  # [1, 3, 5]
print(my_list[::-1])  # [5, 'b', 3, 'a', 1], 리스트도 뒤집기가 가능하다.
# 문자열과 동일한 원리

# 길이
print(len(my_list))  # 5

# 중첩된 리스트 접근
my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
print(len())  # 5
print(my_list[4][2])  # !!!, my_list[-1][-1], my_list[4][-1], my_list[-1][2]
print(my_list[-1][1][0])  # w, my_list[4][-2][0] 등등...
# world는 문자열이므로, 각 문자마다 인덱스가 존재함.
```

리스트도 문자열과 비슷한 원리가 적용된다. (인덱싱, 슬라이싱 등)

```python
# 리스트는 가변
my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)  # [100, 2, 3]

my_list_test = [1, 'world', 3]
my_list_test[1] = 100
print(my_list_test)  # [1, 100, 3]
```

`str`은 부분으로 변할 수 없다!

허나, `list`는 각 요소마다 주소 값을 가지고 있기 때문에 부분으로 변할 수 있다.

```python
# immutable (불변)
my_str = 'hello'
my_str[0] = 'z'  # TypeError: 'str' object does not support item assignment

# mutable (가변)
my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)  # [100, 2, 3]
```

※ `list`를 탐색할 때는 선형 탐색으로 진행된다. (순서대로 탐색)

### tuple

여러 개의 값을 순서대로 저장하는 **변경 불가능한 시퀀스 자료형**

```python
my_tuple_1 = ()

# 단일 요소 튜플을 만들 대는 반드시 Trailing comma (후행 쉼표)를 사용해야 함
# (1) -> int, (1,) -> tuple
my_tuple_2 = (1,)
my_tuple_3 = (1, 'a', 3, 'b', 5)
```

```python
# 인덱싱
print(my_tuple[1])  # a

# 슬라이싱
print(my_tuple[2:4])  # (3, 'b')
print(my_tuple[:3])  # (1, 'a', 3)
print(my_tuple[3:])  # ('b', 5)
print(my_tuple[0:5:2])  # (1, 3, 5)
print(my_tuple[::-1])  # (5, 'b', 3, 'a', 1)

# 길이
print(len(my_tuple))  # 5

# 튜플은 불변
# TypeError: 'tuple' object does not support item assignment
my_tuple[1] = 'z'
```

튜플의 불변 특성을 사용하여 **내부 동작과 안전한 데이터 전달에 사용**된다.

→ 다중 할당, 값 교환, 그룹화, 함수 다중 반환 값 등

*→ 사실 튜플보다 리스트가 더 중요할 것임!!!*

```python
# 다중 할당
x, y = 10, 20
print(x)  # 10
print(y)  # 20
# 실제 내부 동작
(x, y) = (10, 20)

# 값 교환
x, y = 1, 2
x, y = y, x
# 실제 내부 동작
temp = (y, x)  # 튜플 생성
x, y = temp  # 튜플 언패킹
print(x, y)  # 2 1

# 그룹화
student = ('Kim', 20, 'CS')
name, age, major = student  # 언패킹
print(name, age, major)  # Kim 20 CS
```

### range

**연속된 정수 시퀀스를 생성**하는 **변경 불가능**한 자료형

```python
# range(시작 값, 끝 값, 증가 값)
# range(n) : 0부터 n-1까지 1씩 증가, n개의 정수 시퀀스를 만드는 것. = range(0, n)
# range(n, m) : n부터 m-1까지의 1씩 증가
# range(n, m, step) : n부터 m-1까지 step만큼 증가

my_range_1 = range(5)
my_range_2 = range(1, 10)
my_range_3 = range(5, 0, -1)

print(my_range_1)  # range(0, 5)
print(my_range_2)  # range(1, 10)
print(my_range_3)  # range(5, 0, -1)

# 리스트로 형 변환 시 데이터 확인 가능
print(list(my_range_1))  # [0, 1, 2, 3, 4]
print(list(my_range_2))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(my_range_3))  # [5, 4, 3, 2, 1]
```

기본 증가 값은 1이다.

음수 증가 값은 감소하는 수열을 생성하고, 양수 증가 값은 증가하는 수열을 생성한다.

음수 증가 시, 시작 값이 끝 값보다 커야 하고, 양수 증가 시 시작 값이 끝 값보다 작아야 한다.

`range`는 주로 반복문에서 많이 사용된다.

```python
# 주로 반복문과 함께 활용 예정
# range는 iterator로써 작동함.
for i in range(1, 10):
    print(i)  # 1 2 3 4 5 6 7 8 9

for i in range(1, 10, 2):
    print(i)  # 1 3 5 7 9
```

## Non-sequence Types

순서가 없다는 것은 index가 없다는 말과 같다.

### dict

**key-value 쌍**으로 이루어진 **(key값에 관한) 순서와 중복이 없는** **변경 가능**한 자료형

key는 변경 불가능한 자료형(`str`, `int`, `float`, `tuple`, `range`…)만 사용 가능하다. key 값은 중복으로 넣을 수 없다.

value는 모든 자료형 사용 가능하다.

※ key순서가 존재하지 않기 때문에, index도 존재하지 않는다.

```python
# 딕셔너리 표현
my_dict_1 = {}
my_dict_2 = {'key': 'value'}
my_dict_3 = {'apple': 12, 'list': [1, 2, 3]}
print(my_dict_1)  # {}
print(my_dict_2)  # {'key': 'value'}
print(my_dict_3)  # {'apple': 12, 'list': [1, 2, 3]}
```

```python
# 딕셔너리는 키에 접근해 값을 얻어냄
my_dict = {'apple': 12, 'list': [1, 2, 3]}

print(my_dict['apple'])  # 12
print(my_dict['list'])  # [1, 2, 3]
print(my_dict['list'][1])  # 2

# 추가
my_dict['banana'] = 50
print(my_dict)  # {'apple': 12, 'list': [1, 2, 3], 'banana': 50}

# 변경
my_dict['apple'] = 100
print(my_dict)  # {'apple': 100, 'list': [1, 2, 3], 'banana': 50}
```

### set

**순서와 중복이 없는 변경 가능**한 자료형 = **집합** 자료형

```python
# 세트 표현
my_set_1 = set()  # {} -> dict, 빈 set를 만들려면 set()를 사용.
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}
print(my_set_1)  # set()
print(my_set_2)  # {1, 2, 3}
print(my_set_3)  # {1}
```

중복이 허용되지 않는 자료형이기 때문에, 아래와 같이 집합 연산이 가능하다.

```python
# 세트의 집합 연산산
my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}

# 합집합
print(my_set_1 | my_set_2)  # {1, 2, 3, 6, 9}

# 차집합
print(my_set_1 - my_set_2)  # {1, 2}

# 교집합
print(my_set_1 & my_set_2)  # {3}
```

## Other Types

### None

파이썬에서 **‘값이 없음’**을 표현하는 자료형

```python
# None
variable = None
print(variable)  # None
```

### Boolean

참과 거짓을 표현하는 자료형

```python
# Boolean
bool_1 = True
bool_2 = False

print(bool_1)  # True
print(bool_2)  # False
print(3 > 1)  # True
print('3' != 3)  # True, 문자열 3과 정수 3은 같지 않다.
```

## Collection

여러 개의 항목 또는 요소를 담는 자료 구조 → `str`, `list`, `tuple`, `set`, `dict`

| 컬렉션 | 변경 가능 여부 | 순서여부 |
| --- | --- | --- |
| `str` | X | O |
| `list` | O | O |
| `tuple` | X | O |
| `dict` | O | X |
| `set` | O | X |

*※ 앞으로 데이터 타입에서 가장 중요한 것은 **list, dict** 이다.*

## 형변환

한 데이터 타입을 다른 데이터 타입으로 변환하는 과정

*ex)* `range` → `list`로 바꾼 것

종류는 암시적 형변환, 명시적 형변환이 있다.

### 암시적 형변환

파이썬이 자동으로 수행하는 형변환

```python
# 암시적 형변환
print(3 + 5.0)  # 8.0
print(True + 3)  # 4
print(Ture + False)  # 1

# True -> 1, False -> 0
```

### 명시적 형변환

프로그래머가 직접 지정하는 형변환

```python
# 명시적 형변환
# str -> int
print(int('1'))  # 1

# ValueError: invalid literal for int() with base 10: '3.5'
print(int('3.5'))

# float -> int
print(int(3.5))  # 3

# str -> float
print(float('3.5'))  # 3.5

# int -> str : 모두 가능
print(str(1) + '등')  # 1등
```

*명시적 형변환은 프로그래밍을 계속 해보면서 알아가는 것이 최고임! ~~(다 못외움 ㅎㅎ)~~*

## 연산자

### 복합 연산자

C언어랑 비슷하니까 알아두기로 하자.

| 기호 | 예시 | 의미 |
| --- | --- | --- |
| `**=` | `a **= b`  | `a = a ** b` |
| `+=`  | `a += b`  | `a = a + b` |

*~~하지만 무조건 줄인다고 좋은 건 아니다. 둘 다 골고루 써보는 걸 추천한다나 뭐라나~~*

```python
# 복합 연산자
y = 10
y -= 4
# y = y - 4
print(y)  # 6

z = 7
z *= 2
# z = z * 2
print(z)  # 14

w = 15
w /= 4
# w = w / 4
print(w)  # 3.75

q = 20
q //= 3
# q = q // 3
print(q)  # 6
```

### 비교 연산자

| 기호 | 내용 |
| --- | --- |
| `<=` | 이하 |
| `>=` | 이상 |
| `is` | 같음 |
| `is not` | 같지 않음 |

`==`는 값이 같은지를 비교하는 비교 연산자이다.

```python
print(2.0 == 2)  # True
print(2 != 2)  # False
print('HI' == 'hi')  # False
print(1 == True)  # True
```

`is`는 객체 자체가 같은지를 비교한다.

is는 객체의 식별성을 비교하므로, 숫자나 문자열 같은 값 자체를 비교하려는 상황에서는 적절하지 않다.

그러므로 값을 비교할 때는 `==` 을 사용해야 한다.

그럼 `is` 연산자는 언제 사용하나?

1. None과 비교할 때

```python
# None과 비교할 때
x = None

# 권장
if x is None:
    print('x는 None입니다.')

# 비권장
if x == None:
    print('x는 None입니다.')
```

1. 싱글턴 객체를 비교할 때

```python
# 싱글턴 객체
x = True
y = True

# True, False, None은 실제로 같은 객체를 가리킨다.
print(x is y)  # True
print(True is True)  # True
print(False is False)  # True
print(None is None)  # True
```

+) 추가 예시 코드

```python
# 추가 예시: 리스트나 객체 비교
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True (두 리스트의 값은 동일)
print(a is b)  # False (서로 다른 리스트 객체)

# b가 a를 그대로 참조하도록 할 경우
b = a
print(a is b)  # True (같은 객체를 가리키므로 True)
```

### 논리 연산자

`and` , `or` , `not`

```python
# 논리 연산자
print(True and False)  # False, and는 모두 True 여야지 True가 나옴.
print(True or False)  # True, or는 하나라도 True 여야지 True가 나옴.
print(not True)  # False, not은 반대
print(not 0)  # True
```

### 단축 평가

`and` 는 False가 나오기 전까지 모든 조건을 본다.

`or` 은 맨 앞 조건만 True이면 뒤에 조건을 보지 않는다.

```python
# 단축 평가

vowels = 'aeiou'

print(('a' and 'b') in vowels)  # False -> 'b' in vowels
print(('b' and 'a') in vowels)  # True -> 'a' in vowels
# a와 b가 둘 다 vowels에 속해있는가를 물어보는 것이 아니다!
# 'a' and 'b' -> 'b'
# 'b' and 'a' -> 'a'

print(3 and 5)  # 5
print(3 and 0)  # 0
print(0 and 3)  # 0
print(0 and 0)  # 0

print(5 or 3)  # 5
print(3 or 0)  # 3
print(0 or 3)  # 3
print(0 or 0)  # 0
```

### 멤버십 연산자

```python
# 멤버십 연산자

word = 'hello'
numbers = [1, 2, 3, 4, 5]

print('h' in word)  # True
print('z' in word)  # False

print(4 not in numbers)  # False
print(6 not in numbers)  # True
```

### 시퀀스형 연산자

| 연산자 | 역할 |
| --- | --- |
| + | 결합 |
| * | 반복 |

```python
# 시퀀스형 연산자

print('Gildong' + ' Hong')  # Gildong hong
print('hi' * 5)  # hihihihihi

print([1, 2] + ['a', 'b'])  # [1, 2, 'a', 'b']
print([1, 2] * 2)  # [1, 2, 1, 2]
```

## 참고

### Trailing Comma

<aside>

- 컬렉션의 마지막 요소 뒤에 붙는 쉼표, 일반적으로 작성은 **선택사항**임.
- 단, 하나의 요소로 구성된 `tuple` 을 만들 때는 필수!
- 각 요소를 별도의 줄에 작성
- 마지막 요소 뒤에  trailing comma 추가
- 닫는 괄호는 새로운 줄에 배치
</aside>

```python
# Good
items = [
    'item1',
    'item2',
    'item3',
]

config = {
    'host': 'localhost',
    'port': 8080,
    'debug': True,
}

# Bad
items = ['item1', 'item2', 'item3',]
config = {'host': 'localhost', 'port': 8080, 'debug': True,}
# 한 줄 작성 시에는 불필요
items = ['item1', 'item2', 'item3']
config = {'host': 'localhost', 'port': 8080, 'debug': True}
```