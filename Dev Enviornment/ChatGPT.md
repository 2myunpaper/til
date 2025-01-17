## 들어가기 전

들어가기 전, AI의 역사 몇 가지를 알아보자.

**ML(Machine Learning)**은 **알고리즘**을 토대로 **모델을 만드는 것**이다.

모델을 테스트 할 데이터도 많이 필요해진다.

데이터로 모델을 검증하면서, 정확도를 높이게 하는 것이  ML 과정이다.

ML 알고리즘이 발전해서 나온 것들은

SVM (Support Vector Machine), **뉴럴 네트워크** 등이 있다.

**뉴럴 네트워크**란, 각 노드들이 존재하는 layer가 있고,

여러개의 layer을 통해 result를 만드는 과정이다.

이렇게 **뉴럴 네트워크**가 발전해서 나온 것이 **Deep Learning**이다.

**Deep Learning**은 데이터를 입력 받아 모델을 스스로 만드는 기술이다.

ChatGPT가 나오기 전에는, AI는 **판별 모델**이 주였다.

판별 모델이란, 입력 값을 받아 무엇인지 판별하는 모델이라고 생각하면 된다.

시간이 지나 **생성형 모델**이 생겼고, 현재 우리가 많이 쓰는 AI 모델이 되었다.

## 생성형 AI

<aside>

**Generative AI**

오디오, 비디오, 이미지, 텍스트, 코드, 시뮬레이션 등의 새로운 콘텐츠를 생성하는 인공지능 모델

</aside>

<aside>

**Chat GPT ; Generative Pre-trained Transformer**

생성 모델 / 사전 훈련 / 트랜스포머 AI 모델

→ GPT 모델을 기반으로 한 대화형 AI

</aside>

Gernerative는 알겠는데, **Pre-trained** 의미는 무엇일까?

LLM (Large Language Model)을 토대로 추가 강화 학습을 한 모델이라는 뜻으로 사용된다.

※ 전문적 기술을 가르쳐 주는 것을 **fine tune**이라고 한다.

*진짜진짜 많은 데이터를 사용해서 훈련시킨다는 의미로 Pre-trained 인것임!*

**Transformer**는 원래 Encoder, Decoder, Architecture 구조로 되어 있다.

GPT 모델은 Decoder 부분만을 사용한다.

문장 속의 단어 간 관계를 추적해 맥락과 의미를 학습하며,

인간처럼 일관되고 연관성이 높은 언어를 구사하여 **대화형 작업에 강점**이다.

Attention 메커니즘이 적용, RNN과 달리 순차 처리가 아닌 병렬 처리가 가능하며, 대규모 데이터 및 파라미터를 활용할 수 있다.

<aside>

**Attention 메커니즘**

AI가 데이터의 맥락과 중요도를 이해하도록 돕는 필수 기술

입력 데이터의 각 요소가 출력에 얼마나 중요한지 중요도를 계산하는 기법

</aside>

**그러므로 Chat GPT는 세가지 방법으로 AI를 운용한다고 말할 수 있다!**

## Interface, Server, Client

### Interface

서로 다른 두 개의 시스템이 정보를 교환할 때, 그 사이에 존재하는 접점

사용자가 기기를 쉽게 동작 시키거나, 기계와 기계가 통신할 때 필요한 ‘약속된 방식’

→ 실제로 기계와 기계, 시스템과 시스템 사이에서도 수많은 인터페이스를 통해 정보를 주고받고 있음.

<aside>

**UI (User Interface)**

사람이 소프트웨어에 접근하는 그래픽적, 화면적 요소

</aside>

### Client & Server

<aside>

**Client** - 서비스를 요청하는 쪽

**Server** - 요청을 받아서 처리하고, 결과를 응답해주는 쪽

Client → Server : **Requests**

Server → Client : **Responses**

</aside>

우리가 Google에 접속하면 어떤 과정이 이루어질까?

Client가 Server에 사이트를 요청,

Server가 검토 후 사이트 페이지 전송

Client 페이지 받음.

이러한 과정으로 이루어지고 있는 것이다.

## API (Application Programming Interface)

두 소프트웨어가 서로 통신할 수 있게 하는 메커니즘 → ‘약속된 방식의 인터페이스’

※ **Application** - 응용 소프트웨어

*ex1)* 소셜 로그인 - Google로 ChatGPT에 로그인하기

Google 로그인 계정으로 로그인을 성공했을 경우 Google API는 ChatGPT에게 로그인에 성공한 인증된 사용자 정보를 넘겨줌.

*ex2)* 날씨 앱

기상 데이터가 들어있는 기상청의 서버

스마트 폰의 날씨 앱, 웹 사이트의 날씨 정보 등 다양한 서비스들이 이 기상청 서버로부터 데이터를 요청해서 응답을 받는 것임.

**소프트웨어와 소프트웨어 간 지정된 정의(형식)으로 소통하는 수단이 API이다.**

### API Key

API에게 요청을 보내는 애플리케이션을 구별하기 위한 고유한 식별 문자열

Server가 API Key를 요청마다 함께 보냄. → **절대 노출되면 안됨!!!! 무단 사용 위험!!!**

무단 접근을 막고, 승인된 사용자만 요청할 수 있도록 하는 것임.

데이터 관리에도 효율적. (API 호출 횟수, 사용량 모니터링, 제한 및 과금 정책 이용 가능)

결론적으로,

**화면에 드러나지 않아도, 앱이 서버와 통신할 때는 API가 필요하다!**

**API를 안전하게 사용하려면 API Key 등을 고려해야 한다!**

### 챗봇 프로그램 with ChatGPT - API 이용 실습

ChatGPT에서 API key를 발급 받아 실습 해볼 수 있다.

코드는 Private. 개인 드라이브 참고하기.

**Drive**

[](ChatGPT_models.png)

*그러나 한정적으로 이용할 수 있고, 많이 이용하고 싶으면 ChatGPT에 돈 내야된다는 것은 안비밀.*

## ChatGPT API

[API 공식 문서](https://www.google.com/url?q=https%3A%2F%2Fplatform.openai.com%2Fdocs%2Fapi-reference%2Fchat)

[사용 가능한 모델](https://www.google.com/url?q=https%3A%2F%2Fplatform.openai.com%2Fdocs%2Fmodels%2Fgpt-4o)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/a178b89c-3f2f-4b30-8878-a10ce48c15a4/92e9a0f6-50b1-411a-97a9-eb619df812cd/image.png)

### **필수 파라미터**

**model** : 사용하고자 하는 gpt 모델

**messages** : 대화 메시지 목록 응답의 다양성 제어 파라미터

### 응답 다양성 제어

**temperature** : 다음 토큰 예측을 위한 확률 분포를 부드럽게 하는 역할 → **응답의 창의성과 다양성** 조정

0에서 2 사이의 값을 가지며, 1.0 이상일 경우 확률 분포가 평탄해지며 더 창의적이고 예측할 수 없는 결과를 생성

**top_p** : 누적 확률을 기준으로 선택할 토큰의 범위를 제한 → 누적 확률 기반으로 응답의 범위 제한

0에서 1 사이의 값을 가지며, 1에 가까울수록 모델은 더 다양한 토큰을 고려

> **낮은 temperature + 높은 top_p​**
> 
> - temperature가 낮아 확률 분포의 차이가 더 강조됨 → 높은 확률의 단어에 집중​
> - top_p가 높아 누적 확률 범위가 넓음 → 상위 확률 단어들을 다양하게 고려​
>     - 응답이 안정적이고 예측 가능​
> - 활용: 기술 문서 작성, 고객 지원​

> **높은 temperature + 낮은 top_p​**
> 
> - temperature가 높아 확률 분포가 평탄해짐 → 다양한 단어가 선택될 가능성 증가​
> - top_p가 낮아 누적 확률 범위가 좁음 → 선택 후보가 제한적​
>     - 창의적이고 독창적인 응답
> - 활용: 아이디어 도출, 소설 생성

*~~요즘은 많이 똑똑해져서 사실 이 파라미터들로 조절 안 해도 상관은 없음.. 그래도 과거엔 이랬구나 하고 알아가자.~~*