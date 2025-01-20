## 프로그래밍

명령어들의 집합 → 문제를 해결하기 위함.

### 프로그래밍 언어

컴퓨터에게 작업을 지시하고 문제를 해결하는 도구

## Python

<aside>

**장점**

- 쉽고 간결한 문법
- 파이썬 커뮤니티 지원 → 세계적인 규모의 풍부한 온라인 커뮤니티
- 광범위한 응용 분야 → 웹 개발, 데이터 분석, 인공지능, 자동화 스크립트 등
</aside>

AI와 ML에 가장 일반적으로 사용되는 프로그래밍 언어는 Python이다.

*※ JavaScript가 최근에는 제일 많이 사용되는 언어임. (배워야 할듯..)*

<aside>

**알고리즘 방면**

- 직관적인 문법
- 강력한 표준 라이브러리 → 다양한 알고리즘 구현에 필요한 도구를 제공
- 빠른 프로토타이핑 → 알고리즘을 빠르게 테스트하고 수정할 수 있음
</aside>

### 파이썬 프로그램이 실행되는 과정

인터프리터가 사용자의 명령어를 운영체제가 이해하는 언어로 바꿈

*→ low level Lang(어셈블리어, 기계어 등)과 high level Lang(Python, Java, C 등) 사이에 인터프리터가 있다고 생각하면 된다.*

※ Java와 C언어는 인터프리터가 아닌 **컴파일러**가 중간에서 처리해주는 역할을 한다.

※ Interpreter는 한 줄씩, 컴파일러는 통으로 기계어로 번역해줌.

파이썬 프로그램 ↔ **파이썬 인터프리터** ↔ 운영체제(& CPU)

훨씬 더 사용하기 쉽고 운영체제 간 이식도 가능함.

1. shell 이라는 프로그램으로 한 번에 한 명령어씩 입력해서 실행

```bash
$ python
>>> print('hello')
hello
```

1. 확장자가 .py인 파일에 작성된 파이썬 프로그램을 실행 *← 이 방법을 채택할 예정.*

```bash
$ python 01-basic.py
hello
```

### 표현식

값으로 평가될 수 있는 코드 조각

<aside>

**값** : 표현식이 평가된 결과

*ex)* 3 + 5 = 8 → 3 + 5는 표현식, 8은 값을 의미한다.

</aside>

표현식이 평가되어 값이 반환(return)됨. *→ 그냥 식이라고 생각하면 됨.*

### 문장

**Statement**, 실행 가능한 동작을 기술하는 코드 (조건문, 반복문, 함수 정의 등)

→ 문장은 보통 여러 개의 표현식을 포함

### 타입

변수나 값이 가질 수 있는 데이터의 종류를 의미

→ 어떤 종류의 데이터인지, 어떻게 해석되고 처리되어야 하는지를 정의

2가지 요소로 이루어짐 → “값”, “값에 적용할 수 있는 연산”


| Type Category | Types |
| --- | --- |
| Numeric Type | int(정수), float(실수), complex(복소수) |
| Sequence Types | list, tuple, range |
| Text Sequence Type | str(문자열) |
| Non-sequence Types | set, dict |
| 기타 | Boolean, None, Functions |

데이터 타입에 맞는 연산을 수행해야 하기 때문에 타입 파악은 중요하다.

### 산술 연산자 (헷갈리는 것만 표시)

| 종류 | 설명 |
| --- | --- |
| // | 정수의 나눗셈 (몫) |
| % | 나머지 |
| ** | 지수 (거듭제곱) |

### 연산자 우선순위

****  >  -(음수 부호)  >  *, /, //, %  >  +,-**

*ex)* -2 ** 4 = -16, -(2 ** 4) = -16, (-2) ** 4 = 16

### 변수와 메모리

<aside>

**변수** : 값을 저장하기 위한 이름 → 값을 참조하기 위한 이름

**변수 할당** (assign) : 표현식을 통해 변수에 값을 저장

*ex)*

degrees = 36.5 → 변수 degrees에 값 36.5를 할당했다.

degrees = ‘abc’ → 변수 degrees에 값 ‘abc’를 재할당했다.

</aside>

메모리의 모든 위치에는 그 위치를 고유하기 식별하는 메모리 주소가 존재함.

※ **객체(Object)** - 타입을 갖는 메모리 주소 내 값

```bash
number = 10
double = 2 * number
print(double) # 20

number = 5
print(double) # 20, double은 20을 가리키는 Object를 가리키고 있음.
```

## Data Types

데이터 타입이 필요한 이유는,

값들을 구분하고, 어떻게 다뤄야 하는지 알 수 있다.

타입을 명시적으로 지정하면 코드를 읽는 사람이 변수의 의도를 더 쉽게 이해할 수 있고, 잘못된 데이터 타입으로 인한 오류를 미리 예방한다.

```python
# type() : 데이터 타입 함수

string = '문자열'
integer = 10
floating_point = 3.14
a_list = [1, 2, 3, 4, 5]
dictionary = {'name': '홍길동', 'age': 20}
a_set = {1, 2, 3, 4, 5}
a_range = range(11)
a_tuple = (1, 2, 3)
boolean = True

print(type(string))
print(type(integer))
print(type(floating_point))
print(type(a_list))
print(type(dictionary))
print(type(a_set))
print(type(a_range))
print(type(a_tuple))
print(type(boolean))

"""
<class 'str'>
<class 'int'>
<class 'float'>
<class 'list'>
<class 'dict'>
<class 'set'>
<class 'range'>
<class 'tuple'>
<class 'bool'>
"""
```

### int (정수형)

```python
# 정수 자료형
a = 10
b = 0
c = -5

# 진수 표현
# 2진수(binary)
print(0b10)  # 2

# 8진수(octal)
print(0o30)  # 24

# 16진수(hexadecimal)
print(0x10)  # 16
```

<aside>

**2진수(binary)** : 0b

**8진수(octal)** : 0o

**16진수(hexadecimal)** : 0x

</aside>

### float (실수 자료형)

float는 정확히 부동 소수점이라고 부름.

```python
d = 3.14
e = -2.7

# e 또는 E를 사용한 지수 표현 (e = 1/10)
# 314 * 0.01
number = 314e-2
#3.14
print(number)
```

사실 프로그래밍 언어에서 float는 실수에 대한 **근삿값**이다.

컴퓨터 메모리 용량이 한정돼 있고 한 숫자에 대해 저장하는 용량이 제한된다.

컴퓨터는 2진수를 사용하기에, 10진수 0.1은 2진수로 표현하면 0.0001100110011001100110… 이런 식으로 무한으로 반복된다. 그래서 컴퓨터는 사람이 사용하는 10진법의 근삿값만 표시한다.

이로 인해 **부동소수점 에러**가 나온다.

<aside>

**부동소수점** : 컴퓨터가 실수를 표현하는 방식으로 인해 발생하는 작은 오차

</aside>

이를 해결하기 위해 `decimal` 모듈을 사용해 부동소수점 연산의 정확성을 보장한다.

```python
a = 3.2 - 3.1
b = 1.2 - 1.1

# 문제 발생
print(a)  # 0.10000000000000009
print(b)  # 0.09999999999999987
print(a == b)  # False

# 해결 방법
from decimal import Decimal
a = Decimal('3.2') - Decimal('3.1')
b = Decimal('1.2') - Decimal('1.1')

print(a)  # 0.1
print(b)  # 0.1
print(a == b)  # True
```

## Sequence Types

여러 개의 값들을 **순서대로 나열하여 저장**하는 자료형.  *ex)* str, list, tuple, range

<aside>

1. **순서 (Sequence)** → 값들이 순서대로 저장
2. **인덱싱 (Indexing)** → 각 값에 고유한 번호를 가지고 있으며, 인덱스를 사용하여 특정 위치의 값을 선택하거나 수정할 수 있음.
3. **슬라이싱 (Slicing)** → 인덱스 범위를 조절해 부분적인 값을 추출할 수 있음
4. **길이 (Length)** → len() 함수를 사용하여 저장된 값의 개수(길이)를 구할 수 있음
5. **반복 (Iteration)** → 반복문을 사용하여 저장된 값들을 반복적으로 처리할 수 있음
</aside>

### str (문자열)

문자들의 순서가 있는 **변경 불가능한** 시퀀스 자료형

```python
# Hello, world!
print('Hello, World!')

# str
print(type('Hello, World!'))
```

사실 큰 따옴표든, 작은 따옴표든 상관없다.

그러나 공식 python 문서에는 일관성 있게 사용하는 것을 권장하고 있다.

```python
# 중첩 따옴표
print(
    '문자열 안에 "큰따옴표"를 사용하려면 작은 따옴표로 묶는다.'
)  # 문자열 안에 "큰따옴표"를 사용하려면 작은 따옴표로 묶는다.
print(
    "문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다."
)  # 문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다.
```

### Escape sequence

| 종류 | 설명 |
| --- | --- |
| \n | 줄 바꿈 |
| \t | 탭 |
| \\ | 백 슬래시 |
| \’ | 작은 따옴표 |
| \” | 큰 따옴표 |

```python
# Escape sequence
print('철수야 \'안녕\'')
# 철수야 '안녕'
# 문자열 안에 작은 따옴표를 사용함)

print('이 다음은 엔터\n입니다.')
# 이 다음은 엔터
# 입니다.
# 행 바꿈 이용
```

### String Interpolation (문자열 보간법)

문자열 내에 변수나 표현식을 삽입하는 방법

**f-stringx`**

```python
# String Interpolation "f-string"

bugs = 'roaches'
counts = 13
area = 'living room'

# Debugging roaches 13 living room
print(f'Debugging {bugs} {counts} {area}')
# print(f'Debugging') 이렇게 해도 출력이 됨 -> Debugging
```

### 문자열의 시퀀스 특징

| 종류 | 설명 |
| --- | --- |
| 인덱스 | 시퀀스 내의 값들에 대한 고유한 번호로, 각 값의 위치를 식별하는 데 사용되는 숫자
*ex)* 문자열의 길이가 5개일 때, (0, 1, 2, 3, 4) = (-5, -4, -3, -2, -1) |
| 슬라이싱 | 시퀀스의 일부분을 선택하여 추출하는 작업
시작 인덱스와 끝 인덱스를 지정하여 해당 범위의 값을 포함하는 새로운 시퀀스를 생성
*ex)* my_str = ‘hello’를 ‘el’로 나오게 하려면 → `my_str[2:4]` 
*ex)* `my_str[:3]` → ‘hel’
step을 지정하여 추출할 수 있음.
*ex)* `my_str[0:5:2]` → ‘hlo’
*ex)* `my_str[::-1]` → ‘olleh’ (음수 인덱스)
※ 슬라이싱 할 때, **숫자는 자르는 위치라고 생각**하면 편하다. |
| 길이 | `len(*문자열*)`  |
| 문자열은 불변 | 요소를 변경할 수 없음. |

```python
# 문자열의 시퀀스 특징
my_str = 'hello'
# 1. 인덱싱
print(my_str[1])  # e

# 2. 슬라이싱
print(my_str[2:4])  # ll
print(my_str[:3])  # hel
print(my_str[3:])  # lo
print(my_str[::2])  # hlo
print(my_str[::-1])  # olleh

# 3. 길이
print(len(my_str))  # 5

# 4. 문자열은 불변
# TypeError: 'str' object does not support item assignment
my_str[1] = 'z'

# 재할당 (문자열을 바꾼 것이 아님)
my_str = 'hzllo'
```

- **문자열 심화 Code**
    
    ```python
    password = "In the bustling city, where life is a constant race against time, uoy often find yourself wondering if there's a shortcut to success. The vibrant lights of the cityscape illuminate the night, casting shadows on the short-lived dreams of those who seek fortune. As you navigate through the crowded streets, you realize the deen for guidance, like a compass pointing python. You need direction in this chaotic journey called life."
    # 아래에 코드를 작성하시오.
    first_char = password[28:36] # password[28]부터 password[35]까지
    second_word = password[113:118] # 문자열의 113번째부터 총 5글자 
    third_word = password[68:65:-1] # 66번째부터 68번째까지 작성된 글자 뒤집어서 출력
    fourth_word = password[325:321:-1] # 322번째부터 총 4글자를 뒤집어서 출력
    fifth_word = password[365:371] # 365번째부터 작성된 'python'
    
    print(f'{first_char}{second_word} {third_word} {fourth_word} "{fifth_word}".')
    ```
    

## 참고

### Style Guide

코드의 일관성과 가독성을 향상시키기 위한 규칙과 권장 사항들의 모음

<aside>

- 변수명은 무엇을 위한 변수인지 직관적인 이름을 가져야 함
- 공백(spaces) 4칸을 사용하여 코드 블록을 들여쓰기
- 한 줄의 길이는 79자로 제한하며, 길어질 경우 줄 바꿈을 사용
- 문자와 밑줄(_)을 사용하여 함수, 변수, 속성의 이름을 작성
- 함수 정의나 클래스 정의 등의 블록 사이에는 빈 줄을 추가

… 등

</aside>

### 변수명 규칙

<aside>

- 영문 알파벳, 언더스코어(_), 숫자로 구성
- 숫자로 시작할 수 없음
- 대소문자를 구분
- 파이썬의 내부 예약어를 변수로 사용할 수 없음 *ex)* False, None, True, and 등
</aside>

### 주석

프로그램 코드 내에 작성되는 설명이나 메모, 인터프리터에 의해 실행되지 않음

VisualCode에서 주석 단축키는 **Ctrl + /** 

```python
# 이것은 주석입니다
"""
이것은 어려 줄 주석입니다.
"""
```

### 파이썬 튜터

[Python Tutor - Python Online Compiler with Visual AI Help](https://pythontutor.com)

파이썬 프로그램이 어떻게 실행되는지 도와주는 시각화 도우미

나중에 알고리즘 공부할 때 유용할 것임.