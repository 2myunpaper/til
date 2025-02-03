## 프로그래밍 패러다임

<aside>

**절차 지향 프로그래밍**

프로그램을 함수와 로직(절차) 중심으로 작성, 데이터를 함수에 전달하며 순차적으로 처리

**객체 지향 프로그래밍**

데이터와 함수를 하나의 단위로 묶어서 관리, 객체들을 조합하고 재활용하는 방식으로 프로그램 구성

</aside>

### 절차 지향 프로그래밍

```python
# 절차 지향 사고
# 예: 변수와 함수를 별개로 다룸
name = 'Alice'
age = 25

def introduce(name, age):
    print(f'안녕하세요, {name}입니다. 나이는 {age}살입니다.')

introduce(name, age)
```

변수와 함수를 별개로 다룸

입력을 받고, 처리하고, 결과를 내는 과정이 위에서 아래로 순차적으로 흐르는 형태

함수 호출의 흐름이 중요하다!

그러나 한계가 발생한다.

프로그램 규모가 커질수록 데이터와 함수의 관리가 어렵고, 전역 변수의 증가로 인한 관리의 어려움이 있다. 유지보수에 문제도 있는게, 코드 수정 시 영향 범위 파악이 어렵다!

그래서 생긴 것이 **객체 지향 프로그래밍**이다.

### 객체 지향 프로그래밍

```python
# 객체 지향 사고
# 예: 사람(객체) 안에 name, age와 이와 관련된 기능(메서드) 포함
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'안녕하세요, {self.name}입니다. 나이는 {self.age}살입니다.')

alice = Person('Alice', 25)
alice.introduce()  # 객체가 자신의 정보를 출력
```

데이터와 해당 데이터를 처리하는 메서드를 하나의 객체로 묶는다.

객체 간 상호작용과 메시지 전달이 더 중요해졌다.

그러나,

**두 개의 방식은 대조적인 방안이 아니다!**

객체 지향은 기존 절차 지향을 기반으로 두고 보완하기 위해 객체라는 개념을 도입한 것이다.

어떤 순서로 처리할까? → 절차 지향 프로그래밍

어떤 객체가 이 문제를 해결할까? → 객체 지향 프로그래밍

*※ 객체 지향은 “데이터가 살아난다”라고 해석해볼 수 있을 것이다.*

### 객체와 클래스

<aside>

**객체 (Object)**

실제 존재하는 사물을 추상화한 것, “속성(변수)”과 “동작(메서드)”을 가짐.

*ex.* “강아지”라는 객체는 이름, 종, 나이(특징)와 짖기, 뛰기(행동) 등으로 표현할 수 있음.

**클래스 (Class)**

객체를 만들기 위한 설계도, 데이터와 기능을 함께 묶는 방법을 제공, 파이썬에서 타입을 표현하는 방법.

</aside>

```python
a = 'abc'
print(type(a))  # <class 'str'>
# 'abc'는 'str' 객체로 만들어진 것이다.
```

예를 들어, 가수를 생각해보자.

여러 가수가 있을 것이다. 아이유, BTS 등등…

이런 가수들이 모두 각각의 객체이며, 가수라는 클래스에 속해 있다고 말할 수 있다.

각 객체는 고유한 특성을 가지고 있으며,

속성(Attribute), 메서드(Method)를 가지고 있다.

## 클래스

데이터와 기능을 하나의 틀로 묶어 관리하는 방법.

사용자 정의 객체를 만드는 수단이자 속성과 메서드를 정의한다.

클래스 이름은 파스칼 케이스 방식으로 작성하게 된다. (필수는 아님.)

*ex.* MyClass, Person, Singer…

```python
class Person:
    def __init__(self, name, age):  # 생성자 메서드, 초기값 설정
        self.name = name  # 인스턴스 속성
        self.age = age  # 인스턴스 속성

    def introduce(self):
        print(f'안녕하세요. 저는 {self.name}, 나이는 {self.age}살입니다.')

```

`__init__` 메서드는 ‘생성자 메서드’ 로 불린다.

새로운 객체를 만들 때 필요한 초기 값을 설정한다.

이 메서드는 개발자가 직접 호출하지 않는다.

### 인스턴스

클래스를 통해 생성된 객체

클래스가 설계도라면, 인스턴스는 그 설계도로부터 실제로 만든 ‘개별 물건’

*ex.*

아이유는 객체이다. (O)

아이유는 인스턴스이다. (X)

아이유는 가수라는 클래스의 인스턴스이다. (O)

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # 인스턴스 속성
        self.age = age  # 인스턴스 속성

    def introduce(self):
        print(f'안녕하세요. 저는 {self.name}, 나이는 {self.age}살입니다.')

# 인스턴스 생성
p1 = Person('Alice', 25)
p2 = Person('Bella', 30)

# 인스턴스 메서드 호출
p1.introduce()
p2.introduce()
```

### 클래스와 인스턴스

클래스를 만든다는 것은 타입을 만든다는 말과 같다.

```python
name = 'Alice'

print(type(name))  # <class 'str'>

# 변수 name의 타입은 str 클래스다.
# 변수 name은 str 클래스의 인스턴스이다.
# 우리가 사용해왔던 데이터 타입은 사실 모두 클래스였다.
# int, float, list, tuple, str 등등...

"hello".upper()
# 문자열.대문자로()
# 객체.행동()
# 인스턴스(of 'str').메서드()
```

### 클래스 구조

<aside>

**생성자 메서드**

언더바가 두개 있는 메서드를 ‘매직 매서드’라고도 부름.

인스턴스 생성 시 자동 호출되는 특별한 메서드 → `__init__` 

**인스턴스 변수 (속성)**

각 인스턴스 별 고유한 속성

`self.변수명` 형태로 정의한다. 인스턴스마다 독립적인 값이 유지된다.

**클래스 변수 (속성)**

모든 인스턴스가 공유하는 속성이며 클래스 내부에서 직접 정의한다.

</aside>

```python
class Circle:
    # 생성자 메서드
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius  #self.radius의 radius와 뒤에 radius는 다른 것임.

# 인스턴스 생성
# c1 = Circle()  # TypeError: __init__() missing 1 required positional argument: 'radius'
c1 = Circle(1)
c2 = Circle(5)

# 인스턴스 변수(속성)
print(c1.radius)  # 1
print(c2.radius)  # 5

# 클래스 변수(속성)
print(c1.pi)
print(c2.pi)
```

### 클래스 변수와 인스턴스 변수

클래스 변수와 동일한 이름으로 인스턴스 변수 생성 시, 클래스 변수가 아닌 인스턴스 변수에 먼저 참조하게 된다.

```python
class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

c1 = Circle(5)
c2 = Circle(10)

print(c1.radius)  # 5
print(c2.radius)  # 10

# c1의 인스턴스 변수 pi를 생성
c1.pi = 100

print(c1.pi)  # 100
print(Circle.pi)  # 3.14

# c2는 인스턴스 변수 pi가 없으므로 클래스 변수 pi를 참조
print(c2.pi)  # 3.14
```

## 메서드

클래스 내부에 정의된 함수로, 해당 객체가 어떻게 동작할지를 정의하는 것

### 인스턴스 메서드

**클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드**

인스턴스의 상태를 조작하거나 동작을 수행함.

반드시 첫 번째 인자로 인스턴스 자신(`self`)을 받음

인스턴스의 속성에 접근하거나 변경 가능하다.

`self` *는 매개변수 이름일 뿐이며 다른 이름으로 설정 가능하다.*

*하지만! 다른 이름을 사용하지 않을 것을 강력히! 권장한다.*

`self` 동작 원리는 다음과 같다.

```python
# 'hello'를 대문자로 변경하기
'hello'.upper()

# 실제 파이썬 내부 동작은 다음과 같이 진행된다.
str.upper('hello')

# 그래서 self는 단축형 호출이라고 말할 수 있다. 객체지향적인 표현
```

이를 이용하여 인스턴트 메서드를 생성할 수 있다.

```python
class Counter:
    def __init__(self):  # 인스턴스 메서드
        self.count = 0

    def increment(self):  # 인스턴스 메서드
        self.count += 1

c = Counter()  # Counter.__init__(인스턴스)
print(c.count)  # 0
c.increment()
print(c.count)  # 1

c2 = Counter()
c.increment()
print(c2.count)  # 0
print(c.count)  # 2
```

인스턴스 메서드는 생성자 메서드를 포함하고 있다.

생성자 메서드의 예시는 아래와 같다.

```python
class Person:
    def __init__(self, name):
        # 왼쪽 name : 인스턴스 변수 name
        # 오른쪽 name : 생성자 메서드의 매개변수 이름
        self.name = name
        print('인스턴스가 생성되었습니다.')

    def greeting(self):
        print(f'안녕하세요 {self.name}입니다.')
        # 그냥 name이라고 하면 인스턴스로 인식되지 않는다.

person1 = Person('지민')  # 인스턴스가 생성되었습니다.
person1.greeting()  # 안녕하세요. 지민입니다.
# Person.greeting(person1)  # 결과는 위와 같지만, 이런 식으로 코딩하지 않는다!
```

### 클래스 메서드

**클래스가 호출하는 메서드**

클래스 변수를 조작하거나 클래스 레벨의 동작을 수행한다.

`@classmethod` 데코레이터를 사용하여 정의한다!

`cls` *는 매개변수 이름일 뿐이며 다른 이름으로 설정 가능하다.*

*하지만! 다른 이름을 사용하지 않을 것을 강력히! 권장한다.*

```python
class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.increase_population()

    @classmethod
    def increase_population(cls):
        cls.population += 1

person1 = Person('Alice')
person2 = Person('Bob')
print(Person.population)  # 2
```

### 스태틱 메서드

**클래스, 인스턴스와 상관없이 독립적으로 동작하는 메서드** → *그냥 일반 함수라고 생각하면 됨.*

`@staticmethod` 데코레이터를 사용하여 정의

호출 시 자동으로 전달 받는 인자가 없음. 인스턴스나 클래스 속성에 직접 접근하지 않는 도우미 함수와 비슷한 역할!

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(3, 5))  # 8
```

### 메서드 활용

```python
# 입출금이 가능한 은행 계좌 클래스 만들기
# 은행 계좌를 모델링하는 클래스를 만들고, 입출금 기능(메서드)를 구현

class BankAccount:
    interest_rate = 0.02  # 이자율

    def __init__(self, owner, balance=0):
        self.owner = owner  # 계좌 소유자
        self.balance = balance  # 초기 잔액

    # 입금
    def deposit(self, amount):
        self.balance += amount

    # 출금
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('잔액이 부족합니다!')

    # 이자율 설정
    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

    # 금액이 양수인지 검증
    @staticmethod
    def is_positive(amount):
        if amount > 0:
            return True
        else:
            return False

# 계좌 개설 (인스턴스 생성)
alice_acc = BankAccount('Alice', 1000)
print(alice_acc.owner)  # Alice
print(alice_acc.balance)  # 1000

# 입금 및 출금 (인스턴스 메서드 호출)
alice_acc.deposit(500)
alice_acc.withdraw(300)
alice_acc.withdraw(3000)  # 잔액이 부족합니다!

# 잔액 확인 (인스턴스 변수 참조)
print(alice_acc.balance)  # 1200

# 이자율 변경 (클래스 메서드 호출)
BankAccount.set_interest_rate(0.03)
print(BankAccount.interest_rate)  # 0.03

# 잔액이 양수인지 확인 (정적 메서드 호출)
print(BankAccount.is_positive(alice_acc.balance))  # True
```

### 메서드 정리

<aside>

**클래스가 사용해야 할것**

- **클래스 메서드**
    
    인스턴스의 상태에 의존하지 않는 기능을 정의
    
    클래스 변수를 조작하거나 클래스 레벨의 동작을 수행
    
- **스태틱 메서드**
    
    클래스 및 인스턴스와 관련이 없는 일반적인 기능을 수행
    

**인스턴스가 사용해야 할 것**

- **인스턴스 메서드**
    
    인스턴스 상태를 변경하거나, 해당 인스턴스의 특정 동작을 수행
    
</aside>

```python
class MyClass:
    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'

instance = MyClass()
# 클래스가 할 수 있는 것
print(MyClass.instance_method(instance))  # 될 수 있다고 이렇게 쓰면 안된다.
print(MyClass.class_method())
print(MyClass.static_method())

# 인스턴스가 할 수 있는 것
print(instance.instance_method())  # 될 수 있다고 이렇게 쓰면 안된다.
print(instance.class_method())  # 될 수 있다고 이렇게 쓰면 안된다.
print(instance.static_method())  # 인스턴스는 인스턴스 메서드만 사용하도록 한다.
```

*할수 있다와 써도 된다라는 것은 다르다!*

**패러다임은 규칙이 아니다.**

명확한 목적에 따라 설계된 것이기 때문에 클래스와 인스턴스 각각 올바른 메서드만 사용한다!

## 참고

### 클래스와 인스턴스 간 이름 공간

클래스를 정의하면, 클래스와 해당하는 이름 공간이 생성된다.

인스턴스를 만들면, 인스턴스 객체가 생성되고 독림적인 이름 공간이 생성된다.

인스턴스에서 특정 속성에 접근하면, 인스턴스 → 클래스 순으로 탐색한다.

```python
class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)

p1 = Person()
p1.talk()  # unknown

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk()  # unknown
p2.name = 'Kim'
p2.talk()  # Kim

print(Person.name)  # unknown
print(p1.name)  # unknown
print(p2.name)  # Kim
```

이와 같은 원리는 충동이나 영향을 주지 않으면서, 독립적으로 동작할 수 있게 해준다!

→ **코드의 가독성, 유지보수성, 재사용성을 높이는데 도움을 준다.**

### 매직 메서드 (magic method)

Double underscore(’__’)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드이다.

특정 상황에 자동으로 호출된다!

`__str__(self)` , `__len__(self)` 등등…

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'원의 반지름: {self.radius}'

c1 = Circle(10)
c2 = Circle(1)

print(c1)  # 원의 반지름: 10
print(c2)  # 원의 반지름: 1
```

### 데코레이터

다른 함수의 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 함수

*데코레이터도 함수이다!*

```python
# 데코레이터 정의
def my_decorator(func):
    def wrapper():
        # 함수 실행 전에 수행할 작업
        print('함수 실행 전')
        # 원본 함수 호출
        result = func()
        # 함수 실행 후에 수행할 작업
        print('함수 실행 후')
        return result
    return wrapper

# 데코레이터 사용
@my_decorator
def my_function():
    print('원본 함수 실행')
my_function()

"""
함수 실행 전
원본 함수 실행
함수 실행 후
"""
```