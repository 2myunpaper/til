## 문자의 표현

글자 A를 메모리에 저장하는 방법에 대해서 생각해보자

메모리는 숫자만을 저장할 수 있기 때문에 A라는 글자의 모양 그대로 비트맵으로 저장하는 방법을 사용하지 않는 한 각 문자에 대해서 대응되는 숫자를 정해 놓고 이것을 메모리에 저장하는 방법이 사용될 것이다.

영어가 대소문자 합쳐서 52자 이므로 6(64가지)비트면 모두 표현할 수 있다.

이를 **코드 체계**라고 한다.

*ex)* 000000 → ‘a’,  000001 → ‘b’

```python
print(f'{ord("대"):x}')  # x는 16진수를 표현하기 위해 존재
print(chr(0xb300))  # 0x : 16진수 표현 방법
```

네트워크가 발전되기 전 미국의 각 지역 별로 코드 체계를 정해 놓고 사용했지만,

네트워크가 발전하면서 서로 간에 정보를 주고 받을 때 정보를 달리 해석한다는 문제가 생겼다.

그래서 혼동을 피하기 위해 표준안을 만들었으며,

1967년 미국에서 **ASCII**라는 문자 인코딩 표준이 제정되었다.

### ASCII **(American Standard Code for Information Interchange)**

7-bit 인코딩으로 128문자를 표현하며 33개의 출력 불가능한 제어 문자들과 공백을 비롯한 95개의 출력 가능한 문자들로 이루어져 있다.

*ex)* 65 → A, 97 → a …

**확장 아스키**는 표준 문자 이외의 악센트 문자, 도형 문자, 특수 문자, 특수 기호 등 부가적인 문자를 128개 추가할 수 있게 하는 부호이다.

**확장 아스키**는 1Byte 내의 8-bit를 모두 사용한다.

확장 아스키는 세계적으로 통용되는 표준 아스키에 비해, 프로그램이나 컴퓨터 또는 프린터가 그것을 해독할 수 있도록 설계되어 있어야만 올바로 해독될 수 있다.

오늘 날 대부분의 컴퓨터는 문자를 읽고 쓰는데 ASCII 형식을 사용한다.

하지만, 각 나라에서도 컴퓨터가 발전했으며 각 국가들의 문자를 표현하기 위하여 코드체계를 만들어서 사용하게 되었다.

다국어 처리를 위해 표준을 마련한 것이 **유니코드**이다.

유니코드도 다시 **Character Set**으로 분류된다.

UCS-2, UCS-4 → 유니코드를 저장하는 변수의 크기를 정의한다.

그러나 바이트 순서에 대해서 표준화하지 못했다. → 파일을 인식 시 파일이 UCS-2, UCS-4인지 인식하고 각 경우를 구분해서 모두 다르게 구현해야 하는 문제가 발생한다.

유니코드의 적당한 외부 인코딩이 필요하게 되었다.

### 유니코드 인코딩 (UTF : Unicode Transformation Format)

<aside>

**UTF-8** (in web) - min : 8bit, max : 32bit (1Byte * 4)

*ex)* (실제로 정보가 들어가 있는 부분은 x 부분임.)

0xxxxxxx

110xxxxx  10xxxxxx

1110xxxx  10xxxxxx  10xxxxxx

11110xxx  10xxxxxx  10xxxxxx  10xxxxxx

**UTF-16** (in Windows, Java) - min : 16bit, max : 32bit

**UTF-32** (in Unix) - min : 32bit, max : 32bit

</aside>

ex)

```python
# [test.txt]
ABC
한글
```

위의 파일을 인코딩해본다고 생각해보자.

UTF-8 → 41 42 43 0D 0A ED ….

UTF-16BE (Big Endian) → FE FF 00 41 00 42 00 43 00 …

인코딩 별로 기록하는 바이트 크기가 다름을 알 수 있다.

*처음에 Python 프로그래밍도 ASCII 코드로 되어 있으므로,* `coding: utf-8` *이라고 첫 줄에 명시했어야 했다. 지금은 생략 가능하다.*

*다른 인코딩 방식으로 프로그래밍 하고 싶다면 위 항목에 원하는 인코딩 방식을 지정해주면 된다.*

## 문자열

### 문자열 처리

**C언어**에서는,

문자열은 문자들의 배열 형태로 구현된 응용 자료형이며, 문자배열에 문자열을 저장할 때는 항상 마지막에 끝을 표시하는 ‘\0’을 넣어줘야 한다.

```c
char arr[] = "abc";
char arr[] = {'a', 'b', 'c', '\0'};
```

문자열 처리에 필요한 연산을 함수 형태로 제공한다.

`strlen()` , `strcpy()` , `strcmp()` …

**java**에서는,

java.lang.String 클래스에는 기본적인 객체 메타 데이터 외에도 네가지 필드들이 포함되어 있는데, hash값, 문자열의 길이, 문자열 데이터의 시작점, 그리고 실제 문자열 배열에 대한 참조이다.

문자열 데이터를 저장, 처리해주는 클래스를 제공해주며, String 클래스를 사용한다.

```java
String str = "abc"
String str = new String("abc")
```

문자열 처리에 필요한 연산을 연산자, 메소드 형태로 제공한다. 보다 풍부한 연산을 제공한다.

`+`, `length()` , `replace()` , `split()` , `substring()` …

**Python**에서는,

char 타입이 없고, 텍스트 데이터의 취급 방법이 통일되어 있다.

`+`: 연결 (Concatenation), `*`: 반복 …

문자열은 시퀀스 자료형으로 분류되고, 시퀀스 자료형에서 사용할 수 있는 인덱싱, 슬라이싱 연산들을 사용할 수 있다.

`replace()` , `split()` , `isalpha()` , `find()`

문자열은 튜플과 같이 요소값을 변경할 수 없다.

기본적인 차이점은,

C는 아스키 코드로 저장한다.

java는 유니코드(UTF16, 2byte)로 저장한다.

Python은 유니코드(UTF8)로 저장한다.

```c
// C언어
char *name = "홍길동";
int count = strlen(name);
printf("%d", count);  // 6
```

```java
// Java
String name = "홍길동";
System.out.println(name.length());  // 3
```

```python
# Python
name = "홍길동"
print(len(name))  # 3

# 참고
txt = input()  # abcd
txt = list(input())  # ['a', 'b', 'c', 'd']
```

### 문자열 뒤집기

자기 문자열에서 뒤집는 방법이 있고 새로운 빈 문자열을 만들어 소스의 뒤에서부터 읽어서 타겟에 쓰는 방법이 있다.

자기 문자열을 이용할 경우는 swap을 위한 임시 변수가 필요하며 반복 수행을 문자열 길이의 반만을 수행해야 한다.

ex) algorithm → 문자열 길이 9, 4회 반복(9 // 2 = 4)

### 문자열 비교

C언어에서는 `strcmp()` 함수를 제공한다.

Java에서는 equals() 메소드를 제공한다. → 문자열 비교에서 `==` 연산은 메모리 참조가 같은지를 물어본다.

Python에서는 `==` 연산자와 `is` 연산자를 제공한다!

```python
# 문자열 비교
s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = 'ab'
s5 = s4 + 'c'

print(s1 is s3)  # False
print(s1 == 'abc')  # True
print(s1 is 'abc')  # True
print(s1 == s2)  # True, 같은 모양인가?
print(s1 is s2)  # True, 같은 메모리위치인가?
print(s1 == s5)  # True
print(s1 == s5)  # True
print(s5 == 'ab' + 'c')  # True
print(s5 is 'ab' + 'c')  # False

s1 = 'ab'
s2 = 'ab'
s3 = 'ac'
print(s1 == s2)  # True
print(s1 < s2)  # False
print(s1 < s3)  # True
```

### 문자열 숫자를 정수로 변환하기

C언어에서는 `atoi()` 함수를 제공한다. 역함수로는 `itoa()` 가 있다.

Java에서는 숫자 클래스의 parse 메소드를 제공한다.

*ex)* `Integer.parseInt(String)`, 역함수로는 `toString()` 메소드를 제공한다.

Python에서는 숫자와 문자변환 함수를 제공한다.

*ex)*  `int("123")` , `float(”3.14”)` , `int(’A’, 16)` → 16진수 정수로 변환

*※ 참고 : int()와 같은 atoi()함수 만들기*

```python
def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x) - ord('0')  # 문자열 코드를 정수코드로 변환하는 과정
    return i
```