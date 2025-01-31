## 실습

**파이썬을 이용하여 날씨 정보를 받아올 것이다.**

<aside>

**서버** - 부탁을 받으면 처리해주거나, 부탁대로 원하는 값을 돌려주는 역할을 한다.

**클라이언트** - 부탁하는 역할

</aside>

*ex)* 네이버 주소를 입력하면 네이버 메인 화면을 달라고 요청한다. → 서버는 클라이언트가 요청한 네이버 메인 화면을 돌려준다.

위와 같은 서버, 클라이언트 원리로 날씨 정보를 받아오겠다.

그러면 클라이언트는 어떤 방법으로 서버에 요청을 보낼 수 있을까?

1. 웹 브라우저를 켜서 주소창에 주소를 입력한다.
2. 서버에 정보를 요청하는 파이썬 코드를 작성한다.

Google에 ‘python’을 검색하면 URL이 어떻게 되는지 살펴보자.

<aside>

https://www.google.com/search?q=python&oq=python&gs_lcrp=EgZjaHJvbWUyDAgAEEUYORixAxiABDIHCAEQABiABDIKCAIQABixAxiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIKCAcQABixAxiABDIHCAgQABiABDIHCAkQABiABNIBCDI0MTRqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8&sei=OxucZ5_sNN-l2roPtp-HaQ

</aside>

‘?’ 뒤에 있는 것들은 모두 변수인 것을 확인할 수 있다.

그러면 웹브라우저처럼 python으로 요청을 보낼 수 있을까?

*~~직접 요청을 보내는 로직을 구현할 수 있다면 싸피에 없었겠지 ㅎㅎ~~*

라이브러리를 설치하면 쉽게 정보를 가져올 수 있다.

```bash
$ pip install requests
$ pip list | grep requests  ## requests에 해당되는 패키지만 list로 보여줌.
```

```python
import requests
from pprint import pprint as print

# 하드코딩(문자열을 강제로 적는 행위)하는 변수
URL = 'https://fakestoreapi.com/carts'  ## 요청 주소

data = requests.get(URL)
# .get(URL) : URL 주소에 요청을 보내는 메서드

print(data)
# 출력결과 : <Response [200]>
# [200] : 웹의 응답 코드 -> 정상적으로 응답하였습니다.
# [404] : 웹의 응답 코드 -> 알 수 없는 주소로 요청했습니다.

json_data = data.json()
# .json() : 데이터를 JSON 형태로 변환해주는 매서드
print(type(json_data))
# 출력결과 : <class 'list'>
print(json_data)
```

클라이언트들은 각자 다른 방식으로 요청을 보낼 것이다.

그러면, 서버는 어떻게 요청을 이해하고 데이터를 반환할 수 있을까?

### API

클라이언트가 원하는 기능을 수행하기 위해서 서버 측에 만들어 놓은 프로그램

서버 측에 특정 주소로 요청이 오면 정해진 기능을 수행하는 API를 미리 만들어 둔다.

<aside>

**내 코드 ↔ 서버[ API ↔ DATA ]**

</aside>

오늘 실습 할 날씨 정보 수집에서는 두 가지를 찾아야 한다.

날씨 정보를 가지고 있는 서버, 해당 서버가 제공하는 API + 무료 ( = 오픈 API )

https://openweathermap.org/api

### 오픈 API

오픈 API의 사용법은 공식 문서*~~(대부분 영어)~~*에 명시되어 있다.

그런데 만약, 악성 사용자가 만은 계정을 생성해 API에 요청을 보내는 상황을 생각해보자.

서버가 못 버틸 것이다!

이런 문제점을 해결하기 위해 오픈 API는 **API KEY**를 활용하여 사용자를 확인한다.

사용자 인증 혹은 회원 가입을 하면 서버에서 API KEY를 발급해 준다.

서버에 요청할 때 마다 해당 API KEY를 함께 보내 정상적인 사용자인 것을 확인 받는다.

**그리고, 일부 오픈 API는 사용량이 제한되어 있다.**

### JSON

API가 반환하는 데이터는 어떻게 생겼을까?

JavaScript Object Notation (자바스크립트 객체 표기법)으로 나타난다.

데이터를 저장하거나 전송할 때 많이 사용되는 **경량의 텍스트 기반의 데이터 형식**이다.

파이썬은 JSON을 활용하는 기능을 가지고 있다.

<aside>

**파싱(Parsing)** : 데이터를 의미 있는 구조로 분석하고 해석하는 과정

`json.loads()` : JSON 형식의 문자열을 파싱하여 python Dictionary로 변환

</aside>

```python
json_data = '''
~
'''  # 서버로 부터 받은 문자열

# JSON 데이터 파싱하기
data = json.loads(json_data)
# JSON 형식의 문자열을 파싱하여 python Dictionary로 변환

# JSON 데이터에서 정보 읽기
name = data["name"]
age = data["age"]
# ...
```

*외부 API를 사용할 때 안 좋은 점은, 안정성에 문제가 있다.. 서버 터지면 서비스가 아무리 좋아도 말짱 도루묵…*

## 데이터 사이언스

개발자에게 데이터는 더 이상 선택이 아닌 필수이다.

다양한 데이터로부터 새로운 지식과 정보를 추출하기 위해 과학적 방법론, 프로세스, 알고리즘, 시스템을 동원하는 융합 분야가 데이터 사이언스이다.

<aside>

**데이터 사이언스 프로세스**

1. 문제 정의
2. 데이터 수집
3. 데이터 전처리(정제) : 수집한 데이터의 오류 제거(결측치, 이상치), 데이터 형식 변환 등
4. 데이터 분석 : 통계 지식, AI기법 등 *(제일 어려움!)*
5. 결과 해석 및 공유
</aside>

### 자주 활용되는 파이썬 패키지

<aside>

**Numpy** : 수학 계산용 패키지. **Pandas**와 **Matplotlib**를 사용하기 위해 활용되는 패키지

다차원 행결 자료 구조를 제공하여 개발하기 편하다.

**Pandas** : 원하는 데이터만 추출하거나 데이터를 분석할 때 활용되는 패키지

프로그래밍 버전의 엑셀을 다루듯 고성능의 데이터 구조를 만들 수 있다.

**Matplotlib** : 그래프를 그려주는 패키지

다양한 종류의 그래프와 도표를 생성하고 데이터를 시각적으로 표현할 수 있다.

</aside>