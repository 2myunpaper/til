## 함수 (Functions)

**특정 작업을 수행**하기 위한 재사용 가능한 코드 묶음

**재사용성**이 높아지고, 코드의 **가독성과 유지보수성** 향상

```python
# 두 수의 합을 구하는 코드
'''
num1 = 5
num2 = 3
sum_result = num1 + num2

print(sum_result)
'''

# 두 수의 합을 구하는 함수
def get_sum(num1, num2):
	return num1 + num2
```

### 함수 호출

함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블록을 실행하는 것

### 함수 구조

<aside>

**parameter** : 함수의 input

**function body** : 콜론(:) 다음에 들여쓰기 된 코드 블록, 함수가 실행 될 때 수행되는 코드를 정의

**Docstring** : 함수 body 앞에 선택적으로 작성 가능한 함수 설명서, 실행 결과에는 영향이 없음 → 주로 Library 만드는 사람들이 많이 쓴다.

**return value** : 함수는 필요한 경우 결과를 반환할 수 있음, `return` 이 없다면 `None` 이 반환 됨

*ex)* print() 함수는 반환하는 값이 없다.

</aside>

```python
def make_sum(pram1, pram2):  # parameter : 함수의 input
    # function body
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """  # Docstring : 함수의 설명서
    return pram1 + pram2  # return value : 함수의 output
```

### 함수와 반환 값

모든 함수가 반환 값이 있는 건 아니다.

```python
# 반환 값이 있는 함수 정의
def make_sum(pram1, pram2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2

# 함수 호출
result = make_sum(100, 50)
print(result)  # 150

# 함수와 반환 값
# print() 함수는 반환값이 없다.
return_value = print(1)  # 1
print(return_value)  # None

# 반환 값이 없는 함수 정의
def my_func():
    print('hello')

result = my_func()  # hello
print(result)  # None
```

## 매개변수와 인자 (중요!)

<aside>

**매개변수 (parameter)** : 함수를 정의할 때, 함수가 받을 값을 나타내는 변수

**인자 (argument)** : 함수를 호출할 때, 실제로 전달되는 값

</aside>

*굳이 구분하지 않고, 하나로 통합하는 경우도 있다. 하지만 엄연히 다른 것임!*

```python
def add_numbers(x, y):  # x, y는 parameter
	result = x + y
	return result = x + y

a = 5
b = 3
add_result = add_numbers(a, b)  # a, b는 argument
```

### Positional Arguments (위치 인자)

함수 호출 시 인자의 위치에 따라 전달되는 인자. 위치 인자는 함수 호출 시 반드시 값을 전달해야 함.

```python
# 1. Positional Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Alice', 25)  # 안녕하세요, Alice님! 25살이시군요.
greet(25, 'Alice')  # 안녕하세요, 25님! Alice살이시군요.
greet(
    'Alice'
)  # TypeError: greet() missing 1 required positional argument: 'age'
```

### Default Argument Values (기본 인자 값)

함수 정의에서 매개변수에 기본 값을 할당하는 것. 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨

```python
# 2. Default Argument Values
def greet(name, age=20):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob')  # 안녕하세요, Bob님! 30살이시군요.
greet('Charlie', 40)  # 안녕하세요, Charlie님! 40살이시군요.
```

### Keyword Arguments (키워드 인자)

함수 호출 시 인자의 이름과 함께 값을 전달하는 인자

매개변수와 인자를 일치 시키지 않고, 특정 매개변수에 값을 할당할 수 있음

인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달

**단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함!**

```python
# 3. Keyword Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name='Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.
greet(age=35, name='Dave')  # 안녕하세요, Dave님! 35살이시군요.
greet(age=35, 'Dave')  # 키워드 인자는 위치 인자 뒤에 위치해야 함!
greet('Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.
```

### Arbitrary Argument Lists (임의의 인자 목록)

정해지지 않은 개수의 인자를 처리하는 인자

함수 정의 시 매개변수 앞에 `*` 를 붙여 사용

여러 개의 인자를 **tuple**로 처리

※ tuple은 개발자의 의도 용도 보단, 주로 내부 동작에서 쓰인다.

```python
# 4. Arbitrary Argument Lists
def calculate_sum(*args):
    print(args)  # (1, 100, 5000, 30)
    print(type(args))  # <class 'tuple'>
```

### Arbitrary Keyword Argument Lists (임의의 키워드 인자 목록)

정해지지 않은 개수의 키워드 인자를 처리하는 인자

함수 정의 시 매개변수 앞에 `**` 를 붙여 사용

여러 개의 인자를 **dictionary**로 묶어 처리

```python
# 5. Arbitrary Keyword Argument Lists
def print_info(**kwargs):
    print(kwargs)

print_info(name='Eve', age=30)  # {'name': 'Eve', 'age': 30
```

### 함수 인자 권장 작성 순서

<aside>

**위치 → 기본 → 가변 → 가변 키워드**

</aside>

호출 시 인자를 전달하는 과정에서 혼란을 줄일 수 있도록 함

**단, 모든 상황에 적용되는 절대적인 규칙은 아니며, 상황에 따라 유연하게 조정될 수 있다!**

*인자의 모든 종류를 적용한 예시*

```python
# 인자의 모든 종류를 적용한 예시
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)

func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
"""
pos1: 1
pos2: 2
default_arg: 3
args: (4, 5, 6)
kwargs: {'key1': 'value1', 'key2': 'value2'}
"""
```

*부딪혀가면서 안되는 상황에 대해서 알아가야 한다. 많이 적용해보자!*

## 함수의 종류

### 재귀 함수 (Recursion)

함수 내부에서 자기 자신을 호출하는 함수

특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며, 코드의 가독성이 높아짐

1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성

*ex)* 팩토리얼, 피보나치 수열

```python
def factorial(n):
    # 종료 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    else:
        # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
        return n * factorial(n - 1)

# 팩토리얼 계산 예시
print(factorial(5))  # 120
```

*위의 코드에서 함수 호출은 Callstack에 쌓이는데, LIFO 형태로 호출된다고 생각해볼 수 있을 것이다.*

*알고리즘 문제를 풀 때 재귀함수로 풀리는 문제들이 생각보다 많다.*

재귀 함수를 사용하는 이유는,

문제의 자연스러운 표현, 코드 간결성, 수학적 문제 해결을

위함이라 생각해볼 수 있다!

주의해야 할 점은,

종료 조건을 명확히, 반복되는 호출이 종료 조건을 향하도록 해야 한다!

### 내장 함수 (Built-in function)

파이썬이 기본적으로 제공하는 함수 (별도의 import 없이 바로 사용 가능)

```python
numbers = [1, 2, 3, 4, 5]

print(numbers)  # [1, 2, 3, 4, 5]

# 주로 사용될 내장 함수
print(len(numbers))  # 5
print(max(numbers))  # 5
print(min(numbers))  # 1
print(sum(numbers))  # 15
print(sorted(numbers, reverse=True))  # [5, 4, 3, 2, 1]
```

<aside>

`abs(number)` : 절댓값

`sum(list)` : list내의 값 총 합

`sorted(list, reverse= False)`  : list 오름차순 정리

`input('--> ')` : ‘—>’를 출력하고 시작하여 입력 받음. 입력값은 문자열 형태

 … 그 외는 아래 사이트 참고

[Built-in Functions](https://docs.python.org/3/library/functions.html)

</aside>

### 유용한 함수

<aside>

`map(function, iterable)` 

순회 가능한 데이터 구조(iterable)의 모든 요소에 함수를 적용하고, 

그 결과를 map object로 변환

</aside>

```python
# map
numbers = [1, 2, 3]
result = map(str, numbers)
print(result)  # <map object at 0x00000239C915D760>
print(list(result))  # ['1', '2', '3']

# map 활용
# 1 2 3을 입력한다.
numbers1 = input().split()  # 입력 받는 함수 input()
print(numbers1)  # ['1', '2', '3']  # 숫자로 입력해도 모두 str로 저장됨.

numbers2 = list(map(int, input().split()))  # map함수로 각 요소에 int로 형변환함.
print(numbers2)  # [1, 2, 3]  # 숫자로 입력한 것이 int로 저장됨.
```

※ map() 의 결과는 iterator이다. 즉, map의 결과를 가지고 함수 또는 변수에 적용 시켜야 온전히 원하는 결과가 나오는 것이다! → *준비하는 단계라고 생각하면 좋을 듯!! 그저 묶어주는 단계일 뿐!*

<aside>

`zip(*iterables)`   *※ *는 가변 인자 (임의)*

임의의 iterable을 모아 tuple을 원소로 하는 zip object를 반환

</aside>

```python
# zip
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)
print(pair)  # <zip object at 0x000001C76DE58700>
print(list(pair))  # [('jane', 'peter'), ('ashley', 'jay')]

# zip 활용
kr_scores = [10, 20, 30, 50]
math_scores = [20, 40, 50, 70]
en_scores = [40, 20, 30, 50]

for student_scores in zip(kr_scores, math_scores, en_scores):
    print(student_scores)

scores = [
    [10, 20, 30],
    [40, 50, 39],
    [20, 40, 50],
]

for score in zip(*scores):
    print(score)
```

## 함수와 Scope

함수는 코드 내부에 local scope를 생성하며, 그 외의 공간이 global scope로 구분

<aside>

**scope**

- global scope : 코드 어디에서든 참조할 수 있는 공간
- local scope : 함수가 만든 scope (함수 내부에서만 참조 가능)

**variable**

- global variable : global scope에 정의된 변수
- local variable : local scope에 정의된 변수
</aside>

### 변수 수명주기(lifecycle)

1. built-in scope : 파이썬이 실행된 이후부터 영원히 유지
2. global scope : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
3. local scope : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

### 이름 검색 규칙(Name Resolution)

Local → Enclosed → Global → Built-in 순으로 이름을 찾아감. (LEGB Rule) *안쪽에서 바깥으로~*

**함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음.**

```python
print(sum)   # <built-in function sum>
print(sum(range(3)))   # 3 (= 0 + 1 + 2)

sum = 5

print(sum)   # 5
print(sum(range(3)))   # TypeError
```

```python
# LEGB Rule 퀴즈
a = 1
b = 2

def enclosed():
    a = 10
    c = 3

    def local(c):
        print(a, b, c)

    local(500)  # 10 2 500
    print(a, b, c)  # 10 2 3

enclosed()

print(a, b)  # 1 2
```

### `global` 키워드

변수의 스코프를 전역 범위로 지정하기 위해 사용

일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용

```python
num = 0  # 전역 변수

def increment():
    global num  # num를 전역 변수로 선언
    num += 1

print(num)  # 0

increment()

print(num)  # 1
```

※ `global` 키워드 선언 전에 참조 불가, 매개변수에는 `global` 키워드 사용 불가

## 함수 스타일 가이드

### 함수 이름 작성 규칙

<aside>

- 소문자와 언더스코어(_) 사용
- 동사로 시작하여 함수의 동작 설명
- 약어 사용 지양 (길어도 상관 없다.)
</aside>

### 단일 책임 원칙 (Single Responsibility Principle)

모든 객체는 하나의 명확한 목적과 책임만을 가져야 함

*여러 책임이 섞이면 관리하기 어렵다!!! → 책임을 분리시키는 게 좋다.*

*ex)* 비밀번호 유효성 검사, 비밀번호 암호화 및 저장, 환영 이메일 발송 → 합치지 말고 따로따로

## Packing & Unpacking

### Packing

여러 개의 값을 하나의 변수에 묶어서 담는 것

```python
# 한 변수에 콤마로 구분된 값을 넣으면 자동으로 튜플로 처리
packed_values = 1, 2, 3, 4, 5
print(packed_values)  # (1, 2, 3, 4, 5)
```

**‘*’을 활용한 패킹**

```python
# '*변수명' 을 사용하면 나머지 모든 값을 리스트로 묶어서 받을 수 있음
a, *b, c = numbers

print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

# '*매개변수' 를 사용하면 호출 시 여러 개의 인자를 한 변수에 묶어서 받을 수 있음
def my_func(*args):
    print(args)  # (1, 2, 3, 4, 5)
    print(type(args))  # <class 'tuple'>

my_func(1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)
# <class 'tuple'>
```

`print` 함수의 정보를 공식 문서에서 보면, 순서 인자가 존재하지 않는 것을 확인할 수 있다.

### Unpacking

패킹된 변수를 풀어서 개별 변수나 함수 인자로 전달

```python
# 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당
packed_values = 1, 2, 3, 4, 5
a, b, c, d, e = packed_values

print(a, b, c, d, e)  # 1 2 3 4 5
```

**‘*’을 활용한 언패킹**

```python
# 시퀀스(리스트, 튜플 등)를 함수에 전달할 때, 각 요소를 풀어서 개별 인자로 넘겨줄 수 있음
def my_function(x, y, z):
    print(x, y, z)

names = ['alice', 'jane', 'peter']
my_function(*names)  # alice jane peter
```

*쉽게 생각하면, list였던 것을  *붙이면 Unpacking, 여러 개의 Argument에 *붙이면 Packing이 된다고 이해하면 된다.*

**‘**’을 활용한 언패킹 (딕셔너리 → 함수 키워드 인자)**

```python

def my_function(x, y, z):
    print(x, y, z)

my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict)  # 1 2 3
```

```python
def my_function(x, y, z):
    print(x, y, z)

my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict)  # 1 2 3

# 이렇게 사용하고 싶은 경우, 함수의 매개변수와 dict의 key가 일치해야 한다!
```

## 참고

### 람다 표현식 (Lambda expressions)

익명 함수를 만드는 데 사용되는 표현식 → 한 줄로 간단한 함수를 정의

```python
# def addition(x, y):
#     return x + y

# result = addition(3, 5)
# print(result)  # 8

# lambda 표현식으로 작성한 addition 함수
addition = lambda x, y: x + y
print(addition(3, 5))
```

*당연히 문법적인 한계는 존재함! 그래도 알아 놓으면 좋겠다!!!*

```python
# with map 함수
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x**2

# lambda 미사용
squared1 = list(map(square, numbers))
print(squared1)  # [1, 4, 9, 16, 25]

# lambda 사용
squared2 = list(map(lambda x: x**2, numbers))
print(squared2)  # [1, 4, 9, 16, 25]
```

### VS Code 꿀팁

함수 이름을 잘못 설정했는데,

끝까지 사용해버렸다.. 그럼 하나하나 다 수정해야 될까?

→ Nope, 수정하고 싶은 함수 이름에 커서를 놓고 F2를 누르면 잘못 설정한 함수 이름을 한꺼번에 수정이 가능하다!

### print() 함수

print() 함수는 기본적으로 끝에 ‘\n’ 이 포함되어 있다.

이것을 변경하려면 `print(내용, end='')` 이런 식으로 하면 된다.