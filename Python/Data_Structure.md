## 데이터 구조

---

여러 데이터를 효과적으로 사용, 관리하기 위한 구조

컴퓨터 공학에서는 ‘자료 구조’라고 한다. 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은 것.

문자열, 리스트, 딕셔너리 등 각 데이터 구조의 **메서드**를 호출하여 다양한 기능을 활용할 수 있다.

## 메서드 (method)

---

객체에 속한 함수 → 객체의 상태를 조작하거나 동작을 수행

메서드는 **클래스(class) 내부에 정의되는 함수**이다.

클래스는 파이썬에서 ‘타입을 표현하는 방법’이며 이미 은연중에 사용해왔다.

ex) `help`함수를 통해 `str`을 호출해보면 **class** 였다는 것을 확인할 수 있다.

```python
print(type('1'))  # <class 'str'>
print(type([1, 2]))  # <class 'list'>
```

*결국 메서드는 어딘가에 속해 있는 함수이며, 각 데이터 타입별로 다양한 기능을 가진 메서드가 존재한다고 볼 수 있다.*

### 메서드 호출 방법

```python
def add(a, b):
    return a + b

class Calculator:
    def add(self, a, b):
        return a + b
    

# 함수 호출
print(add(1, 2))

# 메서드 호출
a = Calculator()
print(a.add(1, 2))  # 데이터 타입 객체.메서드()
```

```python
# 문자열 메서드 예시
print('hello'.capitalize())  # Hello

# 리스트 메서드 예시
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)  # [1, 2, 3, 4]
```

## 시퀀스 데이터 구조

---

### 문자열 - 조회/탐색 및 검증 메서드

`.find()` , `.index()` , `.isupper()` , `.islower()` , `isalpha()`

```python
# find -> 찾으려는 문자가 없으면 -1을 리턴함.
text = 'banana'
print(text.find('a'))  # 첫 번째로 a가 있는 자리(index)를 나타냄
print(text.find('z'))  # 문자가 없다면 -1을 리턴함.

# index -> 찾으려는 문자가 없으면 에러 발생.
print(text.index('a'))  # 1
# print(text.index('z'))  # ValueError

# isupper -> 모두 대문자인지 확인함.
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper())  # True
print(string2.isupper())  # False

# islower -> 모두 소문자인지 확인함.
print(string1.islower())  # False
print(string2.islower())  # False

# isalpha -> 모두 알파벳으로 되어있는지 확인함.
string1 = 'Hello'
string2 = '123heis98576ssh'
print(string1.isalpha())  # True
print(string2.isalpha())  # False
```

*‘is’ 로 시작하는 내장 함수나 메서드들은 반환 값이 boolean인 것이 대부분이다.*

*내가 함수를 만들 때도 참고해서 코딩하도록 하자!*

### 문자열 - 조작 메서드 (새 문자열 반환)

원래 문자열은 불변의 타입이다. 즉, 한 번 정하면 일부 수정을 할 수 없는 값이다.

그러기 때문에 문자열 조작 메서드는, 새로운 문자열을 반환하는 원리가 적용된다.

`.replace()` , `.strip()` , `.split()` , `.join()` , `.capitalize()` , `title()` , `upper()` , `lower()` , `swapcase()` 

```python
# replace
text = 'Hello, world! world world'
new_text1 = text.replace('world', 'Python')  # 모든 world를 Python으로 바꾼다.
new_text2 = text.replace('world', 'Python', 1)  # 처음부터 하나의 world를 Python으로 바꾼다.
print(new_text1)  # Hello, Python! Python Python
print(new_text2)  # Hello, Python! world world
print(text)  # Hello, world! world world
# 문자열은 불변하는 값으로 새 문자열을 반환한 것을 확인할 수 있음.

# strip -> 문자열의 시작과 끝에 있는 공백 혹은 지정한 문자를 제거
text = '  Hello, world!  '
new_text = text.strip()
print(new_text)  # 'Hello, world!'

# split -> sep를 구분자 문자열로 사용하여 문자열에 있는 단어들의 리스트를 반환함
text = 'Hello, world!'
words1 = text.split(',')  # ',' 기준으로 나눈다.
words2 = text.split()  # 공백 기준으로 나눈다.
print(words1)  # ['Hello', ' world!']
print(words2)  # ['Hello,', 'world!']

# join -> iterable(반복 가능한 객체)의 문자열을 연결한 문자열을 반환
words = ['Hello', 'world!']
new_text = '-'.join(words)
print(new_text)  # Hello-world!

# capitalize -> 제일 첫번째 문자를 대문자로 만든다. 나머지는 모두 소문자
text = 'heLLo, woRld!'
new_text1 = text.capitalize()
print(new_text1)  # Hello, world!

# title -> 제목에 맞게 대문자 소문자로 변경경
new_text2 = text.title()
print(new_text2)  # Hello, World!

# upper
new_text3 = text.upper()
print(new_text3)  # HELLO, WORLD!

# lower
new_text4 = text.lower()
print(new_text4)  # hello, world!

# swapcase
new_text5 = text.swapcase()
print(new_text5)  # HEllO, WOrLD!
```

### 리스트 값 추가 및 삭제 메서드

`.append()` , `extend()` , `insert()` , `remove()` , `pop()` , `clear()` 

```python
# append -> 리스트 마지막에 항목 추가
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]
print(my_list.append(4))  # None, append에는 return값이 존재하지 않음!

# extend -> += 과 같은 기능
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # [1, 2, 3, 4, 5, 6] -> [1, 2, 3] += [4, 5, 6]

# append와의 비교
my_list.append([4, 5, 6])  # [1, 2, 3, [4, 5, 6]]
print(my_list)
# extend는 추가하려는 리스트(iterable)의 요소들을 추가하는 것이고,
# append는 추가하려는 요소 통째로 추가하는 것이다.
# 그리고 extend는 추가하려는 요소가 iterable가 아니면 에러가 발생한다.
```

<aside>

`append(self, object, /)` : Append object to the end of the list.

`extend(self, iterable, /)` : Extend list by appending elements from the iterable.

</aside>

```python
# insert(i, x) -> 리스트의 지정한 인덱스 i 위치에 항목 x를 삽입
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list)  # [1, 5, 2, 3]

# remove -> 리스트에서 첫 번째로 일치하는 항목을 삭제
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list)  # [1, 3, 2, 2, 2]

# pop -> 리스트에서 지정한 인덱스의 항목을 제거하고 반환
# ()안에 작성하지 않을 경우 마지막 항목을 제거
# remove에서는 return 해주지 않는다. pop은 return 해줌!
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1)  # 5
print(item2)  # 1
print(my_list)  # [2, 3, 4]

# clear -> 리스트의 모든 항목을 삭제
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # []
```

### 리스트 탐색 및 정렬 메서드

`.index()` , `.count()` , `.reverse()` , `sort()`

```python
# index -> 리스트에서 첫 번째로 일치하는 항목 x의 인덱스를 반환
my_list = [1, 2, 3]
index = my_list.index(2)
print(index)  # 1

# count -> 리스트에서 항목 x의 개수를 반환
my_list = [1, 2, 2, 3, 3, 3]
counting_number = my_list.count(3)
print(counting_number)  # 3

# reverse -> 리스트의 순서를 역순으로 변경 (정렬 X)
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
# print(my_list.reverse())  # None
print(my_list)  # [9, 1, 8, 2, 3, 1]
# reversed() 함수도 존재한다! 이 함수는 메서드는 아니고,
# sequence에 적용할 수 있는 함수이다.
# reverse()는 list 객체에만 사용할 수 있는 메서드이다.

# sort -> 원본 리스트를 오름차순으로 정렬
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list)  # [1, 2, 3, 100]

# sort(내림차순 정렬)
my_list.sort(reverse=True)
print(my_list)  # [100, 3, 2, 1]
```

*그리고 모르는 메서드는 공식 문서를 참고하는 게 좋다!*

*~~전공서적처럼 보이는~~ 사이트를 두려워 하지 말고, 가벼운 마음으로 찾고자 하는 것만 발견하자!*

## 복사

---

코딩을 할 때, 복사와 재할당을 헷갈릴 때가 있다.

### 객체와 참조

<aside>

**Mutable 객체** : 생성 후 내용을 변경할 수 있는 객체

생성 후에도 그 내용을 수정할 수 있음

객체의 내용이 변경되어도 같은 메모리 주소를 유지

ex) list, dict, set

**Immutable 객체** : 생성 후 내용을 변경할 수 없는 객체

생성 후 그 값을 변경할 수 없음

새로운 값을 할당하면 새로운 객체가 생성되고, 변수는 새 객체를 참조하게 됨

ex) int, float, str, tuple

</aside>

파이썬에서 변수 할당은 객체에 대한 참조를 생성하는 과정이다.

변수는 객체의 메모리 주소를 가리키는 label 역할을 한다고 생각하면 된다.

할당 시 새로운 객체가 생성되거나 기존 객체에 대한 참조가 생성된다.

→ 변수는 객체의 ‘메모리 주소’를 저장, 여러 변수가 동일한 객체를 참조할 수 있음.

```python
print('가변(mutable) 객체 예시')
a = [1, 2, 3, 4]
b = a
b[0] = 100

print(f'a의 값: {a}')  # [1, 2, 3, 4]
print(f'b의 값: {b}')  # [1, 2, 3, 4]
print(f'a와 b가 같은 객체를 참조하는가? {a is b}')  # True

print('\n불변(immutable) 객체 예시')
a = 20
b = a
b = 10

print(f'a의 값: {a}')  # 20
print(f'b의 값: {b}')  # 10
print(a is b)  # False
```

```python
print('\n메모리 주소 확인')
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(f'x의 id: {id(x)}')  # 198357657216
print(f'y의 id: {id(y)}')  # 198357657216
print(f'z의 id: {id(z)}')  # 198357687808
print(f'x와 y는 같은 객체인가? {x is y}')  # True
print(f'x와 z는 같은 객체인가? {x is z}')  # False
```

이러한 동작 방식은 **성능 최적화, 메모리 효율성**이 높다.

### 얕은 복사 (Shallow Copy)

객체의 최상위 요소만 새로운 메모리에 복사하는 방법

내부에 중첩된 객체가 있다면 그 객체의 참조만 복사된다.

구현 방법은 리스트 슬라이싱, `copy()` 메서드, `list()` 함수를 사용하는 것이다.

```python
print('\n얕은 복사 예시')

# 1차원 리스트
a = [1, 2, 3]
b = a[:]  # 슬라이싱
c = a.copy()  # copy() 메서드
d = list(a)  # list() 함수

b[0] = 100
c[0] = 999
d[0] = 8080
print(a)  # [1, 2, 3]
print(b)  # [100, 2, 3]
print(c)  # [999, 2, 3]
print(d)  # [8080, 2, 3]

# 다차원 리스트
print('\n다차원 리스트 얕은 복사의 한계')
a = [1, 2, [3, 4, 5]]
b = a[:]

b[0] = 999
print(a)  # [1, 2, [3, 4, 5]]
print(b)  # [999, 2, [3, 4, 5]]

b[2][1] = 100
print(a)  # [1, 2, [3, 100, 5]]
print(b)  # [999, 2, [3, 100, 5]]
print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  # True
```

1차원 list에는 적합하지만, 다중 list에는 한계가 발생한다.

### 깊은 복사 (Deep Copy)

객체의 모든 수준의 요소를 새로운 메모리에 복사하는 방법

중첩된 객체까지 모두 새로운 객체로 생성된다.

구현 방법은 `copy` 모듈에서 제공하는 `deepcopy()` 함수를 사용한다.

```python
import copy

print('\n깊은 복사 예시')
a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a)

b[2][1] = 100
print(a)  # [1, 2, [3, 4, 5]]
print(b)  # [1, 2, [3, 100, 5]]
print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  # False

# 복잡한 중첩 객체 예시
print('\n복잡한 중첩 객체 깊은 복사')
original = {
    'a': [1, 2, 3],
    'b': {
        'c': 4,
        'd': [5, 6],
    },
}
copied = copy.deepcopy(original)

copied['a'][1] = 100
copied['b']['d'][0] = 500

print(f'원본: {original}')  # {'a': [1, 2, 3], 'b': {'c': 4, 'd': [5, 6]}}
print(f'복사본: {copied}')  # {'a': [1, 100, 3], 'b': {'c': 4, 'd': [500, 6]}}
print(
    f'original["b"]와 copied["b"]가 같은 객체인가? {original["b"] is copied["b"]}'
)  # False
```

## 참고

---

### 메서드 체이닝

여러 메서드를 연속해서 호출하는 방식

```python
# 문자열 메서드 체이닝
text = 'heLLo, woRld!'
new_text = text.swapcase().replace('l', 'z')
print(new_text)  # HEzzO, WOrLD!

# 1. 단계별로 실행하기
text = 'heLLo, woRld!'
step1 = text.swapcase()
print('1단계 결과:', step1)  # HEllO, WOrLD!

step2 = step1.replace('l', 'z')
print('2단계 결과:', step2)  # HEzzO, WOrLD!

# 2. 한 줄로 실행하기 (위와 동일한 결과)
new_text = text.swapcase().replace('l', 'z')
print('최종 결과:', new_text)  # HEzzO, WOrLD!
```

그러나 각 메서드에 대해 잘 파악하고 사용해야 한다.

반환 값이 있는지, 없는지 확인을 해야 한다!

제일 많이 실수하는 유형은 아래와 같다.

```python
# 리스트 메서드 체이닝 예시

# 잘못된 체이닝 방식 1
numbers = [3, 1, 4, 1, 5, 9, 2]
result = numbers.copy().sort()
print(result)  # None (sort()는 None을 반환하므로 체이닝이 중단됨)
print(numbers)  # [3, 1, 4, 1, 5, 9, 2] (원본은 변경되지 않음)

# 잘못된 체이닝 방식 2
result = numbers.append(7).extend([8, 9])  # AttributeError
# append()에서는 반환값이 존재하지 않으므로, extend를 할 때 에러가 발생한다.

# 개선된 방식
# 리스트 조작에서 메서드 체이닝을 사용할 때는 각 메서드가 적절한 값을 반환하는지 확인하고,
# 필요한 경우 새로운 리스트 객체를 반환하는 함수를 사용하는 것이 좋음
sorted_numbers = sorted(numbers.copy())
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 9]
```

### 문자 유형 판별 매서드

<aside>

`isdecimal()` 

문자열이 모두 숫자 문자(0~9)로만 이루어져 있어야 True

`isdigit()` 

`isdecimal()` 과 비슷하지만, 유니코드 숫자도 인식

`isnumeric()` 

`isdigit()` 과 유사하지만, 몇 가지 추가적인 유니코드 문자들을 인식 (분수, 지수, 루트 기호도 숫자로 인식)

</aside>