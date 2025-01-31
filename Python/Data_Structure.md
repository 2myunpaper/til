## 데이터 구조

여러 데이터를 효과적으로 사용, 관리하기 위한 구조

컴퓨터 공학에서는 ‘자료 구조’라고 한다. 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은 것.

문자열, 리스트, 딕셔너리 등 각 데이터 구조의 **메서드**를 호출하여 다양한 기능을 활용할 수 있다.

## 메서드 (method)

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

## 비시퀀스 데이터 구조

### 딕셔너리 메서드

`clear()` , `get(k)` , `get(k, v)` , `keys()` , `values()` , `items()` , `pop(k)` , `pop(k, v)` , `setdefault(k)` , `setdefault(k, v)` , `update(other)` 

```python
# clear : 딕셔너리의 모든 키/값 쌍을 제거
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person)  # {}

# get : 키에 연결된 값을 반환
person = {'name': 'Alice', 'age': 25}
print(person.get('name'))  # Alice
print(person.get('country'))  # None, 키가 없으면 None을 반환
print(person.get('country', 'Unknown'))  # Unknown, 키가 없으면 기본 값을 반환
# print(person['country'])  # KeyError: 'country'

# keys : 키를 모은 객체를 반환
person = {'name': 'Alice', 'age': 25}
print(person.keys())  # dict_keys(['name', 'age'])
for item in person.keys():
    print(item)
"""
name
age
"""

# values : 값을 모은 객체를 반환
person = {'name': 'Alice', 'age': 25}
print(person.values())  # dict_values(['Alice', 25])
for item in person.values():
    print(item)
"""
Alice
25
"""

# items : 키/값 쌍을 모은 객체를 반환
person = {'name': 'Alice', 'age': 25}
print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])
for key, value in person.items():
    print(key, value)
"""
name Alice
age 25
"""

# pop : 키를 제거하고 연결됐던 값을 반환
person = {'name': 'Alice', 'age': 25}
print(person.pop('age'))  # 25
print(person)  # {'name': 'Alice'}
print(person.pop('country', None))  # None
# print(person.pop('country'))  # KeyError: 'country'

# setdefault : 키와 연결된 값을 반환
person = {'name': 'Alice', 'age': 25}
print(person.setdefault('country', 'KOREA'))
# KOREA, 키가 없으면 값과 연결한 키를 추가하고 값을 반환
print(person)  # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}

# update : 각 키의 값을 업데이트함. 키가 없다면 키를 새로 추가하여 값을 부여함.
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'country': 'KOREA'}

person.update(other_person)
print(person)  # {'name': 'Jane', 'age': 25, 'country': 'KOREA'}

person.update(age=100, address='SEOUL')
print(
    person
)  # {'name': 'Jane', 'age': 100, 'country': 'KOREA', 'address': 'SEOUL'}
```

※ update는 주소 재 할당이 아니라 그대로 복사하는 것이라고 생각하면 된다.

```python
a.update(b)
print(a)  # {'name': 'Alice', 'age': 25}
b['name'] = 'Bella'
print(a)  # {'name': 'Alice', 'age': 25}
print(b)  # {'name': 'Bella', 'age': 25}
```

### 세트 메서드

고유한 항목들의 정렬되지 않은 컬렉션 `{` , `}` 로 나타내고, 빈 세트는 `set()` 로 나타냄.

`add(x)` , `clear()` , `remove(x)` , `pop()` , `discard(x)` , `update(iterable)`

```python
# add : 세트에 항목을 추가. 이미 있다면 변화 없음.
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.add(4)
print(my_set)  # {'a', 1, 2, 3, 'b', 4, 'c'}

my_set.add(4)
print(my_set)  # {'a', 1, 2, 3, 'b', 4, 'c'}

# clear : 세트의 모든 항목을 제거
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.clear()
print(my_set)  # set()

# remove : 세트에서 항목을 제거. 항목이 없을 경우 Key error
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2)
print(my_set)  # {'a', 1, 3, 'b', 'c'}
# my_set.remove(10)  # KeyError: 10

# pop : 세트에서 임의의 항목을 반환하고, 해당 항목을 제거함.
my_set = {'a', 'b', 'c', 1, 2, 3}
element = my_set.pop()
print(element)  # a

# discard : 세트에서 항목을 제거
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.discard(2)
print(my_set)  # {1, 3, 'a', 'b', 'c'}
my_set.discard(10)  # 아무런 일도 일어나지 않는다.

# update : 세트에 다른 iterable 요소를 추가함
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.update([1, 4, 5])
print(my_set)  # {'c', 2, 3, 1, 'b', 4, 5, 'a'}
```

### 세트의 집합 메서드

`difference()` , `intersection()` , `issubset()` , `issuperset()` , `union()`

```python
# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2))  # {0, 2, 4}, 차집합 : set1 - set2
print(set1.intersection(set2))  # {1, 3}, 교집합 : set1 & set2
print(set1.issubset(set2))  # False, 부분집합 여부 : set1 <= set2
print(set3.issubset(set1))  # True, 부분집합 여부 : set3 <= set1
print(set1.issuperset(set2))  # False, 부분집합 여부 : set1 >= set2
print(set1.union(set2))  # {0, 1, 2, 3, 4, 5, 7, 9}, 합집합 : set1 | set2
```

## 복사

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

### 해시 테이블

해시 함수를 사용하여 변환한 값을 인덱스로 삼아 키(Key)와 데이터(value)를 저장하는 자료구조

→ 데이터를 빠르게 저장하고 검색하기 위해 사용된다.

<aside>

**해시 (Hash)**

임의의 크기를 가진 데이터를 고정된 크기의 고유한 값으로 변환하는 것

생성된 **해시 값(고유한 정수)**은 해당 데이터를 식별하는 ‘지문’ 역할을 한다.

파이썬에서는 이 해시 값을 이용해 해시 테이블에 데이터를 저장한다.

**해시 함수 (Hash function)** = 해시 알고리즘

임의의 길이 데이터를 입력 받아 고정 길이로 변환해 주는 함수이다.

주로 해시 테이블을 구현할 , 매우 빠른 검색을 위해 활용한다.

</aside>

해시 테이블의 원리는 아래와 같다.

<aside>

1. 키를 해시 함수를 통해 해시 값으로 변환한다. (이름 등을 숫자로 나타낸다고 이해하면 됨.)
2. 변환된 해시 값을 인덱스로 삼아 데이터를 저장하거나 찾는다.
3. 이로 인해 검색, 삽입, 삭제 가 매우 빠르게 수행된다.
</aside>

```python
# 정수 : 정수값은 해시 값이 숫자 자기 자신과 동일하거나 단순 계산으로 고정됨.
my_set = {3, 2, 1, 9, 100, 4, 87, 39, 10, 52}
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set)

# 문자열 : 난수 시드 값이 실행 때마다 달라지므로, 결과가 다르게 나올 수 있다.
my_str_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())
```

해시 값이 적용되는 `set` 과 `dict` 의 차이를 알아보자.

`set`은 각 요소를 해시 함수로 변환해 나온 해시 값에 맞춰 해시 테이블 내부 버킷에 위치시킨다.

그래서 순서라기보다 버킷 위치가 요소의 위치를 결정한다. 따라서 `set`은 순서를 보장하지 않는 것이다.

`dict` 은 키 → 해시 함수 → 해시 값 → 해시 테이블 순으로 저장된다.

`set` 과 달리, 삽입 순서는 유지한다는 것이 특징이다. *(python 3.7 이상부터 적용됨)*

즉, 키를 추가한 순서대로 반복문 순회할 때 나오게 되고, 사용자에게 보여지는 키 순서는 삽입 순서가 유지되도록 설계된 것이다.

해시 함수가 적용되는 정수와 문자열을 확인해보자.

```python
print(hash(1))  # 1
print(hash(1))  # 1
print(hash('a'))  # 실행시마다 다르다.
print(hash('a'))  # 실행시마다 다르다.
```

정수는 항상 같은 해시 값을 가지지만,

문자열은 파이썬 인터프리터 시작 때 설정되는 **난수**가 달라지기에, 실행 때 마다 해시 값이 달라진다.

→ 해시 함수가 매번 바뀌는 것이 아니라, 해시 계산에 쓰이는 **시드 값**이 실행마다 달라지는 것이다.

결과적으로, 버킷 배치가 달라진다.

→ `set` 에서 `pop()` 을 할 때 결과가 달라지는 이유

### hashable

<aside>

**hashable**

hash() 함수에 넣어 해시 값을 구할 수 있는 객체를 의미

대부분의 불변 타입은 해시 가능 ex) `int` , `float` , `str` , `tuple` (내부의 불변만 있을 경우)

가변형 객체 ex) `list` , `dict` , `set` 는 기본적으로 해시 불가능

</aside>

hashable 객체가 필요한 이유는,

1. 해시 테이블 기반 자료 구조 사용 → set의 요소, dict의 키, 중복 방지 & 빠른 검색 및 조회 가능
2. 불변성을 통한 일관된 해시 값 → 한 번 해시 값이 정해지면 바뀌지 않아야 해시 테이블 무결성이 유진된다.
3. 안정성과 예측 가능성 유지

```python
print(hash(1))
print(hash(1.0))
print(hash('1'))
print(hash((1, 2, 3)))

# TypeError: unhashable type: 'list'
# print(hash((1, 2, [3, 4])))
# TypeError: unhashable type: 'list'
# print(hash([1, 2, 3]))
# TypeError: unhashable type: 'list'
# my_set = {[1, 2, 3], 1, 2, 3, 4, 5}
# TypeError: unhashable type: 'set'
# my_dict = {{3, 2}: 'a'}
```