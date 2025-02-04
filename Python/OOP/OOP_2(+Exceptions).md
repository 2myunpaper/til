## 상속


한 클래스(부모)의 속성과 메서드를 다른 클래스(자식)가 물려받는 것

상속이 필요한 이유는, **코드 재사용, 계층 구조, 유지 보수의 용이성**를 위해서이다.

<aside>

**코드 재사용**

상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있음

기존 클래스를 수정하지 않고도 기능을 확장할 수 있음

**계층 구조**

상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음

부모 클래스와 자식 클래스 간의 관계를 표현하고, 더 구체적인 클래스를 만들 수 있음

**유지 보수의 용이성**

상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 되므로 유지 보수가 용이해진다.

코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화할 수 있음

</aside>

*ex1)* 아래로 내려갈 수록 자식 클래스임

Motor Vehicle

Bus, Truck, Car

….

*ex2)* 게임을 만든다고 생각해보자.

캐릭터 ← 돈, 레벨, 공격, 수비, 이동…

전사 ← 힘, 명예, 베기, 찌르기  |  마법사 ← 마력, 회복, 순간이동

Python에 상속 개념을 적용하면 아래의 예시와 같다.

```python
class Animal:
    def eat(self):
        print('먹는 중')

class Dog(Animal):
    def bark(self):
        print('멍멍')

# 인스턴스 생성
my_dog = Dog()

my_dog.bark()  # 멍멍

# 부모 클래스(Animal) 메서드 사용 가능
my_dog.eat()  # 먹는 중
```

만약 상속 개념 없이 구현을 했다고 치자.

```python
# 상속 없는 경우 - 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

s1 = Person('김학생', 23)
s1.talk()  # 반갑습니다. 김학생입니다.

p1 = Person('박교수', 59)
p1.talk()  # 반갑습니다. 박교수입니다.
# 하나의 클래스로는 교수의 특징, 학생의 특징을 세부적으로 표현하지 못한다.

# 상속 없는 경우 - 2
class Professor:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def talk(self):  # 중복
        print(f'반갑습니다. {self.name}입니다.')

class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def talk(self):  # 중복
        print(f'반갑습니다. {self.name}입니다.')
# 중복되는 instance 선언이 많아진다.
```

그래서 상속 개념을 적용하면, 세부적인 특징을 담을 뿐더러, 중복적 코딩을 할 필요가 없어진다.

```python
# 상속을 사용한 계층구조 변경
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):  # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')

class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
```

### 메서드 오버라이딩

부모 클래스의 메서드를 같은 이름, 같은 파라미터 구조로 재정의하는 것

```python
class Animal:
    def eat(self):
        print('Animal이 먹는 중')

class Dog(Animal):
    # 오버라이딩 (부모 클래스 Animal의 eat 메서드를 재정의)
    def eat(self):
        print('Dog가 먹는 중')

my_dog = Dog()

my_dog.eat()  # Dog가 먹는 중, method overriding
```

**참고 : 오버로딩**

같은 이름, 다른 파라미터를 가진 여러 메서드를 정의하는 것 → 파이썬은 미지원한다. Java는 가능함.

파이선은 실제로 하나의 메서드만 인식하며, 인자의 형태가 다르다는 이유로 메서드를 여러 개 구분하여 불러주지 않는다.

### 다중 상속

**둘 이상의 상위 클래스로부터** 여러 행동이나 특징을 상속받을 수 있는 것을 뜻함.

상속받은 모든 클래스의 요소를 활용 가능함

**중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정된다.**

```python
# 다중 상속 예시
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'

class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'

class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'

class FirstChild(Dad, Mom):  # Dad를 먼저 상속받음
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'

baby1 = FirstChild('아가')
print(baby1.cry())  # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
print(baby1.gene)  # XY, FirstChild가 Dad를 먼저 상속받으므로 gene은 Dad를 따름.
```

이 원리는 **다이아몬드 문제**를 해결하기 위한 것이다.

부모 클래스로부터 상속된 송성들의 검색을 깊이 우선으로(왼쪽에서 오른족으로), **계층 구조에서 겹치는 같은 클래스를 두 번 검색하지 않는다!**

다이아몬드 문제를 단편적으로 보면 간단하지만,

실제 프로그램은 엄청 복잡한 구조를 가지고 있다.

그러므로, **Python에는 MRO을 쉽게 적용할 수 있는 메서드가 존재한다!**

<aside>

**MRO** : 파이썬이 메서드를 찾는 순서에 대한 규칙, 메서드 결정 순서

</aside>

### `super()` 메서드

부모 클래스의 메서드를 호출하기 위해 사용하는 내장 함수

다중 상속 상황에서 특히 유용하며, MRO를 따르기 때문에 여러 부모 클래스를 가진 자식 클래스에서 다음에 호출해야 할 부모 메서드를 순서대로 호출할 수 있게 한다.

아래는 단일 상속일 경우를 보여준다.

```python
# super를 사용하지 않았을 때
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id

# 단일 상속, super() 사용
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        # super()를 통해 Person의 __init__ 메서드 호출
        super().__init__(name, age, number, email)
        # Person.__init__(name, age, number, email) 도 위와 동일하게 적용됨.
        # 그러나, 부모 클래스의 이름이 바뀐다면? 일일이 다 수정해야 한다.
        # 그래서 super()을 쓰는 것이 합당함.
        self.student_id = student_id
```

단일 상속은 하나의 부모 객체에서만 가져오는 것이기 때문에 충돌이란 것이 없다.

하지만, 다중 상속을 받을 때 `super()` 을 사용한다면 어떻게 될까?

```python
# 다중 상속
class ParentA:
    def __init__(self):
        # super().__init__()
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')

class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')

class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()  # ParentA 클래스의 __init__ 메서드 호출
        self.value_c = 'Child'

    def show_value(self):
        super().show_value()  # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')

child = Child()
child.show_value()
"""
Value from ParentA: ParentA
Value from Child: Child
"""

print(child.value_c)  # Child
print(child.value_a)  # ParentA
print(
    child.value_b
)  # AttributeError: 'Child' object has no attribute 'value_b'
```

그러면 `child` 객체는 `value_b`를 가져올 수 없는 걸까?

답은 가져올 수 있는 방법이 존재한다!

현재 상황에서는,

`ParentA` 클래스 `__init__()` 메소드에 `super()` 을 붙이면, `ParentB`로 탐색하게 된다.

```python
class ParentA:
    def __init__(self):
        super().__init__()  # Child 입장에서는 ParentA 탐색 후 ParentB로 탐색하게 됨.
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')
```

따라서, `super()` 은 **무조건 부모 클래스를 가리키는 것이 아니다!**

MRO 순서를 기반으로 **현재 클래스의 다음 순서를 탐색하는 함수**인 것이다.

그럼 결과적으로 `value_b` 도 출력할 수 있게 된다.

그러므로, `super()` 을 사용할 때는 MRO를 잘 이해하고 있어야 한다.

순서를 아는 방법은, `__mro__` 또는 `mro()` 함수를 사용하여 알 수 있다.

```python
class A:
    def __init__(self):
        print('A Constructor')

class B(A):
    def __init__(self):
        super().__init__()
        print('B Constructor')

class C(A):
    def __init__(self):
        super().__init__()
        print('C Constructor')

class D(B, C):
    def __init__(self):
        super().__init__()
        print('D Constructor')

# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
print(D.mro())

# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(D.__mro__)
```

MRO가 필요한 이유는,

1. 부모 클래스들이 여러 번 액세스 되지 않도록,
2. 각 클래스에서 지정된 왼쪽에서 오른쪽으로 가는 순서를 보존하고,
3. 각 부모를 오직 한 번만 호출하고,
4. 부모들의 우선순위에 영향을 주지 않으면서 서브 클래스를 만드는 단조적인 구조를 형성한다.

프로그래밍 언어의 신뢰성 있고 확장성 있는 클래스를 설계할 수 있고,

클래스 간의 메서드 호출 순서가 예측 가능하게 유지되며, 코드의 재사용성과 유지보수성이 향상된다.

## 에러와 예외

### 디버깅

버그를 해결하는 것. 프로그램의 오작동 원인을 식별하여 수정하는 작업을 뜻한다.

버그란, 소프트웨어에서 발생하는 오류 또는 결함을 뜻한다.

프로그램의 예상된 동작과 실제 동작 사이의 불일치를 뜻하기도 한다.

<aside>

**디버깅 방법**

1. print 함수 활용
2. 개발 환경(text editor, IDE) 등에서 제공하는 기능을 활용한다.
3. Python tutor 활용
4. *~~뇌 컴파일, 눈 디버깅 ㅋㅋ~~*

…

</aside>

### 에러

프로그램 실행 중에 발생하는 예외 상황

<aside>

**문법 에러 (Syntax Error)**

프로그램의 구문이 올바르지 않은 경우 발생 (오타, 괄호 및 콜론 누락 등)

애초에 실행되지 않음.

*ex)* Invalid syntax, assign to literal, EOL(End of Line), EOF(End of File)

**예외 (Exception)**

프로그램 실행 중에 감지되는 에러

</aside>

### 예외 (Exception)

python에는 예외 상황을 나타내는 **예외 클래스**들이 존재한다. → 내장 예외 (Built-in Exceptions)

`ZeroDivisionError` `NameError` `TypeError` (타입 불일치, 인자 누락, 인자 초과, 인자 타입 불일치)

`ValueError` `IndexError` `KeyboardInterrupt` (사용자가 Ctrl+C 또는 Delete를 연타하면 발생)

`IndentationError` (잘못된 들여쓰기) 등등…

## 예외 처리 (Exception Handling)

예외가 발생했을 때 프로그램이 비정상적으로 종료되지 않고, 적절하게 처리할 수 있도록 하는 방법

<aside>

`try` : 예외가 발생할 수 있는 코드 작성

`except` : 예외가 발생했을 때 실행할 코드 작성

`else` : 예외가 발생하지 않았을 대 실행할 코드 작성

`finally` : 예외 발생 여부와 상관없이 항상 실행할 코드 작성

</aside>

### try-except 구조

```python
try:
		# 예외가 발생할 수 있는 코드

except:
		# 예외 처리 코드
```

### 복수 예외 처리

```python
# 복수 예외처리
try:
    num = int(input('100을 나눌 값을 입력하시오 : '))
    print(100 / num)
except (ValueError, ZeroDivisionError):  # 복수 예외 처리
    print('제대로 좀 입력해')
```

```python
try:
    num = int(input('100을 나눌 값을 입력하시오 : '))
    print(100 / num)
except ValueError:
    print('숫자를 입력하라고')
except ZeroDivisionError:
    print('0으로 어떻게 나누겠니')
except:  # 위의 두 예외사항 말고 나머지 예외가 발생할 때
    print('나눌 수가 없다ㅏㅏㅏ')
```

### else & finally

```python
try:
    x = int(input('숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('유효한 숫자가 아닙니다.')
else:  # 위의 두 예외가 발생하지 않으면 실행되는 구간
    print(f'결과: {y}')
finally:  # 마지막에 무조건 실행되는 구간
    print('프로그램이 종료되었습니다.')
```

## 참고

### 예외 처리 주의사항

예외 클래스들도 상속처리가 된 클래스들이다.

그러므로 예외 처리를 할 때는 주의해야 한다.

내장 예외 클래스 상속관계는 공식 문서를 참고하면 된다.

```python
# 아래와 같이 예외를 작성하면 코드는 2번째 except 절에 이후로 도달하지 못함
# ZeroDivisionError 클래스는 BaseException 클래스의 하위 클래스 중 하나이므로
# ZeroDivisionError를 먼저 작성해야 함
# https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy
try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
except BaseException:
    print('숫자를 넣어주세요.')
# ZeroDivisionError는 BaseException의 하위 클래스이므로 BaseException보다 먼저 작성해야 함
# 아래쪽은 죽은 코드들이 되버린다.
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('에러가 발생하였습니다.')
```

그래서 올바르게 작성하려면 아래와 같이 해야한다.

```python
# 옳은 코드
# 가장 구체적인 예외부터 처리하고, 마지막에 범용 예외를 처리하도록 순서를 배치
try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
# 1) 구체적인 예외부터
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('숫자를 넣어주세요.')
# 2) 마지막에 광범위한 예외(Exception)
except Exception:
    print('에러가 발생하였습니다.')
```

*세부적인 것부터 예외를 작성해가야 한다!*

### 예외 객체 다루기

예외가 발생했을 때 예외에 대한 정보를 담고 있는 객체를 생성할 수 있다.

```python
my_list = []

try:
    number = my_list[1]
except IndexError as error:
    # list index out of range가 발생했습니다.
    print(f'{error}가 발생했습니다.')
```

그리고 try-except와 if-else는 같이 사용될 수 있다!

### EAFP & LBYL

try-except는 그럼 언제 쓰일까?

<aside>

**EAFP ; Easier to Ask for Forgiveness than Permission**

허락보다 용서가 더 쉽다.

예외처리를 중심으로 코드를 작성하는 접근 방식 → try-except

예외 상황을 예측하기 어려운 경우에 유용함.

**LBYL ; Look Before You Leap**

돌다리도 두들겨 보고 가라

값 검사를 중심으로 코드를 작성하는 접근 방식 → if-else

예외 상황을 미리 방지하고 싶을 때 유용함.

</aside>

```python
# EAFP (Easier to Ask for Forgiveness than Permission, 허락보다 용서 구하기)
try:
    result = my_dict['key']
    print(result)
except KeyError:
    print('Key가 존재하지 않습니다.')

# LBYL (Look Before You Leap, 돌다리도 두들겨보고 건너기)
if 'key' in my_dict:
    result = my_dict['key']
    print(result)
else:
    print('Key가 존재하지 않습니다.')
```

### 클래스의 의미와 활용

프로그램 규모가 커지면 서로 관련 있는 정보와 기능을 따로 관리하기가 어려워진다.

클래스를 사용하면 **관련된 데이터와 기능을 ‘한 덩어리’로 묶어 구조를 명확히 할 수 있다.**

이로서 작성한 코드가 훨씬 깔끔해지고, 나중에 수정하거나 기능을 추가할 때 더 쉽고 안전해진다.

ex) 도서 관리 프로그램

책을 나타내는 클래스를 만들고 (title, author, price 같은 속성과 print_info() 같은 기능 등…), 이 클래스를 이용해 여러 권의 책 객체를 다룰 수 있다.

알고리즘 문제는 클래스가 없어도 문제 해결이 가능하다.

하지만 현실의 문제는 훨씬 복잡하며, **나중에 여러 사람과 함께 작업하는 프로젝트를 한다면**, 클래스를 통해 구조를 잘 짜는 것이 필수가 된다. → 프로그램 이해도 상승, 오류 발견 용이함.