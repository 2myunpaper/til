Django는 **프레임워크 학습**임.

이미 만들어진 기능을 **어떻게 활용하고 조합할지 학습하는 것이 중요**하다.

## Web Application

인터넷을 통해 사용자에게 제공되는 소프트웨어 프로그램을 구축하는 과정

다양한 디바이스에서 웹 브라우저를 통해 접근 및 사용

### 웹의 동작 방식

클라이언트 (Cline) - 서버 (Server) 구조

클라이언트가 서버에 요청 (request)

서버가 클라이언트에게 응답 (response)

- **Client**
    
    서비스를 요청하는 주체 (사용자 웹 브라우저, 모바일 앱)
    
- **Server**
    
    클라이언트의 요청에 응답하는 주체 (웹 서버, 데이터베이스 서버)
    

<aside>

*ex) 우리가 웹 페이지를 보게 되는 과정*

1. 웹 브라우저(클라이언트)에서 [google.com](http://google.com) 을 입력 후 엔터
2. 웹 브라우저는 인터넷에 연결된 구글 컴퓨터(서버)에게 ‘메인 홈페이지.html’ 파일을 **요청**
3. 요청 받은 구글 컴퓨터는 데이터 베이스에서 ‘메인 홈페이지.html’ 파일을 찾아 **응답**
4. 웹 브라우저는 전달 받은 파일을 사람이 볼 수 있도록 해석, 사용자는 메인 페이지 확인.
</aside>

### Frontend & Backend

- **Frontend**
    
    사용자 인터페이스를 구성하고, 사용자가 애플리케이션과 상호작용할 수 있도록 함
    
    *ex) HTML, CSS, Javascript*
    
- **Backend**
    
    서버 측에서 동작하며, 클라이언트의 요청에 대한 처리와 데이터베이스와의 상호작용 등을 담당
    
    *ex) django, Python, Java, 보안*
    

## Framework

모든 기능을 직접 개발하기에는 현실적인 어려움이 존재한다.

현대 웹 개발의 핵심은 잘 만들어진 도구를 효과적으로 활용하는 능력을 기르는 것이다.

- **Web Framework**
    
    웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구
    
    (개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공)
    

### Django

Python 기반의 대표적인 웹 프레임워크

→ 다양성(광범위한 서비스 개발), 확장성(대량의 데이터에 빠르고 유연하게 처리 가능), 보안(보안 기능이 기본적으로 내장되어 있음), 커뮤니티 지원 등에 뛰어나다.

*ex) Spotify, Instagram, Dropbox, Delivery Hero 등에서도 검증된 프레임워크*

## 가상 환경

하나의 컴퓨터 안에서 또 다른 **‘독립된’ 파이썬 환경**

<aside>

*ex) 가상 환경이 필요한 시나리오*

1. 2개의 프로젝트(A와 B)를 진행해야 한다.
2. 프로젝트 A는 `requests` 패키지 버전 1을 사용해야 한다.
3. 프로젝트 B는 `requests` 패키지 버전 2를 사용해야 한다.
4. 파이썬 환경에서 패키지는 1개의 버전만 존재할 수 있다.
5. A와 B 프로젝트의 다른 패키지 버전 사용을 위한 독립적인 개발 환경이 필요하다.
</aside>

그러므로, 파이썬의 global 환경 안에 가상 환경을 만들어줄 필요가 있다.

### 가상 환경 생성 및 활성화

`python -m venv (가상환경 이름)` : 현재 디렉토리에 `venv` 라는 폴더가 생성되고, 폴더 안에는 파이썬 실행 파일, 라이브러리 등을 담을 공간이 마련된다. 되도록 가상환경 이름은 `venv` 라고 설정해주는 것이 좋다.

`source venv/Scripts/activate` : **가상 환경 활성화**, 활성화 후, 프롬프트 앞에 `(venv)` 와 같이 표시된다면 성공한 것이다.

`deactivate` : 활성화한 상태에서 입력하면, 다시 기본 Global 파이썬 환경으로 돌아옴.

### 의존성 패키지

프로젝트가 의존하는 “개별 라이브러리들”을 가리키는 말

→ 프로젝트가 실행되기 위해 꼭 필요한 패키지 하나하나

- **의존성**
    
    하나의 소프트웨어가 동작하기 위해 필요로 하는 다른 소프트웨어나 라이브러리
    

*ex)* `requests` 패키지는 다른 몇 패키지에 의존하는 부분이 있어 다른 패키지와 같이 설치된다. 

`pip list`  : **현재 가상환경에 설치된 라이브러리 목록을 확인**, 갓 생성된 가상 환경은 별도의 패키지가 없어, 주로 `pip` , `setuptools` 정도만 표시된다.

`pip freeze > requirements.txt` : **가상환경에 설치된 모든 패키지를 버전과 함께 출력하여 텍스트 파일에 저장**한다. 나중에 동일한 환경을 재현할 때 유용하다. 협업 시에도 팀원들이 똑같은 버전의 라이브러리를 설치하도록 공유가 가능하다.

`pip install -r requirements.txt` : **기록된 의존성 리스트대로 pip 설치**

### 가상환경이 필요한 이유

패키지마다 버전이 다르고, 버전이 다른 경우 함수명이나 동작이 달라질 수 있다.

프로젝트가 커질수록 사용하는 패키지의 개수도 늘어나므로, 어떤 버전을 쓰고 있는지 기록 및 공유가 필수적이다.

다른 PC나 팀원들이 같은 환경을 구성할 때 **의존성 리스트**가 반드시 필요하다.

### 가상환경 주의사항

1. 가상 환경에 들어가고 나오는 것이 아니라 사용할 Python 환경을 On/Off로 전환하는 개념
    
    가상환경 활성화는 현재 터미널 환경에만 영향을 끼친다.
    
2. 프로젝트마다 별도의 가상 환경을 사용한다.
3. 일반적으로 가상환경 폴더 `venv` 는 관련된 프로젝트와 동일한 경로에 위치시킨다.
4. 폴더 `venv` 는 `.gitignore` 파일에 작성되어 원격 저장소에 공유되지 않음.
    
    저장소 크기를 줄여 효율적인 협업과 배포를 가능하게 하기 위함.
    
    대신 `requirements.txt` 를 공유한다.
    

## Django 프로젝트

### 프로젝트 생성 및 서버 실행

`pip install django` : 현재 환경에 Django 패키지를 설치함.

※ 설치 후 requirements.txt 는 자동으로 업데이트 되지 않으므로, `pip freeze`를 꼭 할 것!

`django-admin startproject firstpjt .` : `firstpjt` 라는 이름의 django 프로젝트를 생성

`.` 은 현재 디렉토리를 의미함. (점이 없을 땐 어떻게 될까?)

`python [manage.py](http://manage.py) runserver` : **서버 실행**, `manage.py`와 동일한 위치에서 명령어 진행

※ 서버 종료는 `Ctrl + C` 를 입력하면 됨.

## Django Design Pattern

- **디자인 패턴**
    
    소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책 (공통적인 문제를 해결하는 데 쓰이는 형식화된 관행)
    
    → 애플리케이션의 구조는 이렇게 구성하자라는 관행이다.
    
    - **MVC 디자인 패턴**
        
        **Model, View, Controller**
        
        데이터, 사용자 인터페이스, 비지니스 로직을 분리.
        
        **애플리케이션을 구조화하는 대표적인 패턴**이다.
        
        시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이, 독립적이고 쉽게 유지 보수할 수 있는 애플리케이션을 만들기 위한 것.
        
    - **MTV 디자인 패턴**
        
        **Model, Template, View**
        
        Django에서 애플리케이션을 구조화는 패턴.
        
        기존 MVC 패턴과 동일하나 **단순히 명칭을 다르게 정의**한 것!
        
        [MTV 디자인 패턴 정리](https://www.notion.so/MTV-1c07900d53b680f8824ff28b0c0b7b87?pvs=21) 
        

### 프로젝트와 앱

프로젝트는 여러 애플리케이션(기능)을 관리하는 것이다.

- **Django project**
    
    애플리케이션의 집합이다. (DB설정, URL 연결, 전체 앱 설정 등을 처리함.)
    
- **Django application**
    
    독립적으로 작동하는 기능 단위 모듈
    
    각자 특정한 기능을 담당하며 다른 앱들과 함께 하나의 프로젝트를 구성한다.
    

<aside>

*ex) 온라인 커뮤니티 카페*

프로젝트 → 카페 (전체 설정 담당)

앱 → 게시글, 댓글, 회원 관리 등 (DB, 인증, 화면)

</aside>

앱을 사용하기 위한 순서는, **1. 앱 생성, 2. 앱 등록이며, 순서가 바뀌면 안 된다.**

1. **앱 생성**
    
    `python [manage.py](http://manage.py) startapp (앱 이름)` 
    
    앱의 이름은 ‘복수형’으로 지정하는 것을 권장
    
2. **앱 등록**
    
    [`settings.py`](http://settings.py) 파일 내에 `INSTALLED_APPS` 앱 이름을 추가한다.
    
    ※ 왜 문자열로 사용하지?
    
    → 이런 고민은 프레임워크 사용 중에선 금지. 이렇게 이용해야 되는구나 하고 넘어가야 함!
    

### 프로젝트 구조

[`settings.py`](http://settings.py) : 프로젝트의 모든 설정을 관리

`urls.py` : 요청 들어오는 URL에 따라 이에 해당하는 적절한 views를 연결

`__init__.py` : 해당 폴더를 패키지로 인식하도록 설정하는 파일

`asgi.py` : 비동기식 웹 서버와의 연결 관련 설정

`wsgi.py` : 웹 서버와의 연결 관련 설정

`manage.py` : Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

### 앱 구조

[`admin.py`](http://admin.py) : 관리자용 페이지 설정

[`models.py`](http://models.py) : DB와 관련된 Model을 정의, MTV 패턴의 M

[`views.py`](http://views.py) : HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환 (url, model, template과 연계), MTV 패턴의 V, 80%는 여기에서 코드 수정이 이루어짐.

[`apps.py`](http://apps.py) : 앱의 정보가 작성된 곳

[`tests.py`](http://tests.py) : 프로젝트 테스트 코드를 작성하는 곳

## 요청과 응답

요청 → [`urls.py`](http://urls.py) → ( [`views.py`](http://views.py) → [`models.py`](http://models.py) , [`templates.py`](http://templates.py) ) → 응답

※ 괄호는 app을 의미함.

1. URLs
    
    request 객체를 views 모듈의 함수에게 전달하며 호출
    
    url 경로는 반드시 ‘/’ 로 끝나야 한다.
    
2. View
    
    view 함수가 정의되는 곳
    
    특정 경로에 있는 template과 request 객체를 결합해 응답 객체를 반환
    
    - 모든 view 함수는 첫번째 인자로 요청(request) 객체를 필수적으로 받음
    - 매개변수 이름이 request가 아니어도 되지만 그렇게 작성하지 않는다!
3. Template
    
    `articles` 앱 폴더 안에 `templates` 폴더 생성
    
    - 폴더 명은 반드시 `templates` 여야 하며 개발자가 직접 생성해야 한다.
    
    `templates` 폴더 안에 `articles` 폴더 생성
    
    `articles` 폴더 안에 템플릿 파일 생성
    
    - Django에서 template을 인식하는 경로 규칙
        
        <aside>
        
        *~~app폴더 / templates /~~* articles / index.html
        
        *~~app폴더 / templates/~~* example.html
        
        </aside>
        
        Django는 ‘app 폴더 / templates' 지점까지 기본 경로로 인식하기 때문에, view 함수에서 template 경로 작성 시 이 지점 이후의 경로를 작성해야 한다.
        

### 요청과 응답 과정 정리

1. 브라우저가 사이트 링크로 요청, urls.py가 요청을 받는다.
2. 주소와 일치하는 view 함수를 호출한다.
3. index view 함수가 응답 객체 생성 및 반환한다.
4. 브라우저는 index view 함수가 반환한 응답 객체를 해석해 페이지를 렌더링한다.

→ 데이터 흐름에 따른 코드를 작성하는 방법은, `URLs` → `View` → `Template` 순으로 작성한다.

## 참고

### Django 프로젝트 생성 전 루틴

1. 가상환경 생성
    
    `python -m venv venv`
    
2. 가상환경 활성화
    
    `source venv/Scripts/activate`
    
3. Django 설치
    
    `pip install django`
    
4. 패키지 목록 파일 생성
    
    `pip freeze > requirements.txt`
    
5. .gitignore 파일 생성 (첫 add전)
6. git 저장소 생성 (git init)
7. Django 프로젝트 생성

### LTS (Long-Term Support)

프레임워크나 라이브러리 등의 소프트웨어에서 장기간 지원되는 안정적인 버전을 의미할 때 사용.

기업이나 대규모 프로젝트에서는 소프트웨어 업그레이드에 많은 비용과 시간이 필요하기 때문에 안정적이고 장기간 지원되는 버전이 필요하다.

### Django는 Full stack framework

그러나, Django가 제공하는 Frontend 기능은 다른 전문적인 Frontend Framework들에 비해서는 매우 미흡하다.

엄밀히 하자면 Full Stack 영역에서 Backend에 속한다고 볼 수 있겠다.

### `render` 함수

`render(request, template_name, context)`

주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 렌더링 된 텍스트와 함께 HttpResponse 응답 객체를 반환하는 함수

`request` : 응답을 생성하는 데 사용되는 요청 객체

`template_name` : 템플릿 이름의 경로

`context` : 템플릿에서 사용할 데이터 (딕셔너리 타입으로 작성)

### MTV 디자인 패턴 정리

- **Model**
    
    **데이터와 관련된 로직을 관리**
    
    응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
    
- **Template**
    
    **레이아웃과 화면을 처리**
    
    화면 상의 사용자 인터페이스 구조와 레이아웃을 정의
    
- **View**
    
    Model & Template과 관련한 로직을 처리해서 응답을 반환
    
    클라이언트의 요청에 대해 **처리를 분기하는 역할**
    
    *ex) 데이터가 필요하다면 model에 접근해서 데이터를 가져오고, 가져온 데이터를 template로 보내 화면을 구성하고, 구성된 화면을 응답으로 만들어 클라이언트에게 반환*
    

### 프레임워크의 규칙

**프레임워크를 사용할 때는 일정한 규칙을 따라야 하며** 이는 저마다의 설계 철학이나 목표를 반영하고 있다. → 일관성 유지, 보안 강화, 유지보수성 향상, 최적화 등

프레임워크는 개발자에게 도움을 주는 도구와 환경을 제공하기 위해 규칙을 정해 놓은 것이며, 우리는 이를 잘 활용하여 **특정 기능을 구현하는 방법을 표준화하고 개발 프로세스를 단순화할 수 있도록 해야 한다.**

<aside>

*ex) Django의 규칙*

[`urls.py`](http://urls.py) 에서 각 url 문자열 경로는 반드시 ‘/’로 끝남

[`views.py`](http://views.py) 에서 모든 view 함수는 첫번째 인자로 요청 객체를 받음.

→ 매개변수 이름은 반드시 `request`로 지정하기

Django는 특정 경로에 있는 template 파일만 읽어올 수 있다.

→ 특정 경로 : `app폴더/templates/` 

</aside>

### `.gitignore` 입력 문구 참고 사이트

[gitignore.io](https://www.toptal.com/developers/gitignore/)

<aside>

*ex) Django .gitignore*

Django, VisualStudioCode로 검색하면 된다.

</aside>