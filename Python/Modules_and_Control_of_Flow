## 모듈 (Module)

과학자, 수학자가 모든 이론을 새로 만들거나 증명하지 않는 것처럼 개발자 또한 프로그램 전체를 모두 혼자 힘으로 작성하는 것은 드문 일이다.

코딩에서도, 다른 프로그래머가 이미 작성해 놓은 코드를 활용하는 것은 생산성에서 중요한 일이다!

<aside>

**모듈 (Module)**

한 파일로 묶인 변수화 함수의 모음. 특정한 기능을 하는 코드가 작성된 파이썬 파일 (.py)

</aside>

*쉽게 말해 모듈은 함수들의 집합이라고 볼 수도 있을듯!*

```python
# math 내장 모듈 : 파이썬이 미리 작성해 둔 수학 관련 변수와 함수가 작성된 모듈
import math  # math.py로 저장이 되어 있다.
             # python을 설치하면 자동으로 저장되는 모듈 중 하나.

print(math.pi)  # 3.141592653589793
print(math.sqrt(4))  # 2.0

# random 내장 모듈
import random

print(random.randint(1,10))  # 1부터 10까지 랜덤의 숫자를 출력

# datetime 내장 모듈
import datetime

now = datetime.datetime.now()  # 현재 시간이 저장됨.
print(now)

# os, sys 등등 많이 존재함.
```

### 모듈을 가져오는 방법

`import` , `from` 을 사용한다.

```python
# from 절 사용
from math import sqrt  # math를 사용할 순 없다. sqrt만 사용 가능해짐.

print(sqrt(4))
```

### 모듈 사용하기

`. (dot)` 연산자 → “점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라”라는 의미

### 모듈 주의사항

서로 다른 모듈이 같은 이름의 함수를 제공할 경우 문제 발생

마지막에 `import` 된 이름으로 대체됨

```python
from math import pi, sqrt
from my_math import sqrt

# 그래서 모듈 내 모든 요소를 한번에 import 하는 * 표기는 권장하지 않음!
# from math import *
```

`as` 키워드를 사용하여 별칭을 부여할 수 있다.

두 개 이상의 모듈에서 동일한 이름의 변수, 함수 클래스 등을 가져올 때 발생하는 이름 충돌을 해결한다.

```python
from math import sqrt
from my_math import sqrt as my_sqrt

sqrt(4)
my_sqrt(4)
```

*파이썬에서는 import를 쓰는 것을 권장하고 있다. (맞다 틀리다가 아니다!)*

*가시성, 가독성, 이중 충돌 방지 등을 위해 그런 것이긴 한데, 정도껏 알아서 잘 사용하면 될 듯!*

### 사용자 정의 모듈

.py 파일을 만들어 사용자 정의 모듈을 만들 수 있다.

함수로 채워 넣으면 다른 파일에서도 사용할 수 있게 된다!

```python
# my_math.py
def add(x, y):
    return x + y
```

```python
# sample.py
import my_math

print(my_math.add(1, 2))
```

*위의 예시는 두 개의 파일 모두 같은 경로에 있다는 조건이 있어야 한다.*

## 파이썬 표준 라이브러리 (PSL)

파이썬 언어와 함께 제공되는 다양한 **모듈**과 **패키지**의 모음이다.

파이썬을 설치하면서 같이 설치되는 라이브러리이다.

### 패키지 (Package)

연관된 모듈들을 하나의 디렉토리에 모아 놓은 것

**함수 < 모듈 < 패키지 < 라이브러리** 라고 생각하면 된다.

```python
# my_package/math/my_math.py
def add(x, y):
    return x + y
```

```python
# my_package/math/tools.py
def mod(x, y):
    return x % y
```

```python
# sample.py
from my_package.math import my_math
from my_package.statistics import tools

print(my_math.add(1, 2))
print(tools.mod(1, 2))

# from my_package.math.my_math import add
# from my_package.statistics.tools import mod

# print(add(1, 2))
# print(mod(1, 2))
```

*from 뒤에는 폴더 경로를 쓰는 것처럼 작성하면 되겠다.*

**PSL내부 패키지**는 설치 없이 바로 `import` 하여 사용할 수 있지만

**외부 패키지**는 `pip` 를 사용하여 설치 후 `import` 해야 한다.

아래는 파이썬의 여러 외부 패키지를 모아 놓은 대표적인 사이트이다.

[PyPI · The Python Package Index](https://pypi.org/)

`pip install SomePackage` : 최신 버전으로 설치

`pip install SomePackage==1.0.5` : 1.0.5 버전으로 설치
`pip uninstall SomePackage` : 패키지 삭제
`pip install requests` : 외부 API 서버로 요청하는 패키지인 requests, 무조건 쓰임!!
`pip list` : 설치한 패키지를 list형태로 확인할 수 있음

*외부 패키지는 설명 문서가 존재하기 때문에, 읽어보면서 설치하는 게 중요하다.*

```python
# requests 패키지 사용 예시
# HTTP 요청을 보낼 수 있도록 도와주는 requests 라이브러리 import
import requests

# 무작위 사용자 정보를 제공해주는 API의 URL
url = 'https://random-data-api.com/api/v2/users'

# requests.get(url)을 통해 API에 요청을 보냄
# 서버로부터 응답(Response)을 JSON 형태로 받아 Python 객체(딕셔너리/리스트 등)로 변환
response = requests.get(url).json()

# 받은 응답 데이터(딕셔너리 형태)를 출력
print(response)
```

**패키지의 사용 목적**은 모듈들의 이름 공간을 구분하여 충돌을 방지하고,

모듈들을 효율적으로 관리하고 재사용할 수 있도록 돕는 역할을 한다!

## 제어문

코드의 실행 흐름을 제어하는 데 사용되는 구문

조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행

**조건문, 반목문, 반복문 제어**가 있음.

<aside>

조건문 : `if` `elif` `else`

반복문 : `for` `while`

반복문 제어 : `break` `continue` `pass`

</aside>

### 조건문 (Conditional Statement)

```python
# ex1
dust = 35

if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')

# ex2
dust = 480

if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('위험해요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
```

`if`를 만들었다면, `elif` `else`는 필수가 아니므로 선택적으로 사용하면 됨!

### 반복문 (Loop Statement)

주어진 코드 블록을 여러 번 반복해서 실행하는 구문

<aside>

`for` : 특정 작업을 반복적으로 수행

`for 변수 in 반복 가능한(iterable) 객체:`

※ for 반복문에서 반복 가능한 객체는 시퀀스 객체 뿐만 아니라 `dict` , `set` 등도 포함한다.

</aside>

```python
# list를 이용한 for문
items = ['apple', 'banana', 'coconut']

for item in items:
    print(item)
    
"""
apple
banana
coconut
"""

# 문자열을 이용한 for문
country = 'Korea'

for char in country:
    print(char)

"""
K
o
r
e
a
"""

# dict을 이용한 for문
my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict:  # 원래 dict은 순서가 없지만, 개발자가 작성해 놓은 dict 순서에 맞춰준다.
    print(key)
    print(my_dict[key])
    
"""
x
10
y
20
z
30
"""

# 인덱스를 이용한 for문 -> 알고리즘 문제를 풀 때 많이 사용된다.
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)  # [8, 12, 20, -16, 10]
```

중첩 반복문을 이용할 수도 있다.

```python
# 이중 for문 이용하기
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)
"""
A c
A d
B c
B d
"""

# 다중 List에 중첩 반복문을 적용함
elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    print(elem)  # ['A', 'B'] ['c', 'd']

for elem in elements:
    for item in elem:
        print(item)  # A B c d
```

<aside>

`while` : 주어진 조건이 참인 동안 반복해서 실행 = 조건식이 거짓이 될 때까지 반복

</aside>

while 문은 반드시 종료 조건이 필요하다.

```python
# while문 기본 예시
a = 0

while a < 3:
    print(a)
    a += 1

print('끝')
"""
0
1
2
끝
"""

# while문을 이용한 양의 정수 판단기
number = int(input('양의 정수를 입력해주세요.: '))
while number <= 0:
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    number = int(input('양의 정수를 입력해주세요.: '))
print('잘했습니다!')

```

*반복 횟수가 명확하게 있는 건 for문, 명확하지 않는 것은 while문을 사용하도록 하자.*

### 반복문 제어

<aside>

`break` : 반복문을 멈춤.

`continue` : 반복문에서 다음 반복으로 넘어가게 하는 명령어

`pass` : 아무런 작업도 안 함.

1. **코드 작성 중 미완성 부분이 있을 때 주로 사용된다.**
2. 조건문에서 아무런 동작을 하지 말아야 할 때 사용된다.
3. 무한 루프에서 조건이 충족되지 않을 때 pass를 사용하여 루프를 계속 진행.
</aside>

```python
# break 예시
# "프로그램 종료 조건 만들기"
number = int(input('양의 정수를 입력해주세요.: '))
while number <= 0:
    if number == -9999:
        print('프로그램을 종료합니다.')
        break
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    number = int(input('양의 정수를 입력해주세요.: '))
print('잘했습니다!')

# "리스트에서 첫번째 짝수만 찾은 후 반복 종료하기"
numbers = [1, 3, 5, 6, 7, 9, 10, 11]

# 첫 번째 짝수를 찾았는지 여부를 저장하는 플래그 변수
# 초기값은 찾지 못했다(False)로 설정
found_even = False

for number in numbers:
    if number % 2 == 0:
        print(f'첫번째 짝수 {number}를 찾았습니다.')
        # 짝수를 찾은 상태이므로 True로 변경
        found_even = True
        break

# 반복문이 끝날 때까지 짝수를 찾지 못한 경우
if found_even == False:
    print('짝수를 찾지 못함')
```

```python
# continue 예시 - "리스트에서 홀수만 출력하기"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

"""
1
3
5
7
9
"""
```

## List comprehension (리스트 표현식)

간결하고 효율적인 리스트 생성 방법

*파이썬스러운 방식이라고도 말한다.*

```python
numbers = [1, 2, 3, 4, 5]

# 기존 방식
# squared_numbers = []

# for num in numbers:
#     squared_numbers.append(num**2)  # 리스트에 값 추가 리스트.append(값)

# print(squared_numbers)

# 리스트 컴프리헨션
squared_numbers_2 = [num**2 for num in numbers]
# squared_numbers_2 = list(num**2 for num in numbers)
print(squared_numbers_2)
```

```python
# List Comprehension 활용 예시 - "2차원 배열 생성 시 (인접행렬 생성 시)"
data1 = [[0] * (5) for _ in range(5)]
print(data1)
# 또는
data2 = [[0 for _ in range(5)] for _ in range(5)]
print(data2)

"""
[[0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]]
"""
```

*그러나 list comprehension을 남용하는 것은 좋지 않다.*

*상황에 따라 무엇이 더 좋을지 생각은 해봐야 한다.*

```python
# 리스트 컴프리헨션 with 조건문
# 기존 방식
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)

print(evens)  # [0, 2, 4, 6, 8]

# 리스트 컴프리헨션
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# 기존 방식의 코드가 더 가독성이 뛰어나다고 볼 수 있음.
```

### 리스트 생성 방법 비교

<aside>

**List Comprehension**

파이썬스러운 방식의 간결한 코드 작성 가능, 가독성을 해치지 않을 선에서 사용하는 것이 중요

**map**

이미 정의된 함수를 적용해야 할 때 유용, 여러 값을 한꺼번에 적용할 때 가독성이 좋아짐.

**기본 Loop**

직관적 이해 용이, 특정 조건에 따라 continue/break가 필요한 경우 유리

</aside>

*성능은 적은 순서와 같다! → 하지만 아주 미미한 차이임으로 상황에 따라 잘 선정하는 게 중요하겠다.*

## 참고

### 모듈 내부 살펴보기

`help(모듈)` 

### enumerate

`enumerate(iterable, start = 0)` 

iterable 객체의 각 요소에 대해 **인덱스와 함께 반환**하는 내장함수

```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

"""
0 apple
1 banana
2 cherry
"""

for index, fruit in enumerate(fruits, 3):
    print(index, fruit)

"""
3 apple
4 banana
5 cherry
"""
```