## Template System

### Django Template System

데이터 표현을 제어하면서, 표현과 관련된 부분을 담당함.

### Django Template Language (DTL)

Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템

1. **Variable**
    
    `render` 함수의 세번째 인자로 딕셔너리 데이터를 사용
    
    딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
    
    dot(’.’)을 사용하여 변수 속성에 접근할 수 있음.
    
    *ex)* `{{ variable }}` `{{ variable.attribute }}` 
    
2. **Filters**
    
    표시할 변수를 수정할 때 사용 (변수 + | + 필터)
    
    chained(연결)이 가능하며 일부 필터는 인자를 받기도 함
    
    약 60개의 built-in template filters를 제공
    
    *ex)* `{{ name|truncatewords:30 }}` 
    
3. **Tags**
    
    반복 또는 논리를 수행하여 제어 흐름을 만듦
    
    일부 태그는 시작과 종료 태그가 필요
    
    약 24개의 built-in template tags를 제공
    
    *화면에 출력은 되지 않음*
    
    *ex)* `{% if %} {% endif %}` 
    
4. **Comments**
    
    DTL에서의 주석
    
    ex) `{# #}` `{% comment %} {% endcomment %}`
    

*필터와 테그에 대한 자세한 정보는 공식 문서를 참고한다.*

*검색할 때는 공식 문서 검색 엔진을 사용하지 말고 구글링을 통해 자세히 알아본다.*

그럼 이것들을 활용한 예시를 작성해보자.

*ex) 메뉴판 예시*

```python
# urls.py
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('dinner/', views.dinner),
]
```

```python
# views.py
import random
from django.shortcuts import render

def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육', '']
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        'picked' : picked,
    }
    return render(request, 'articles/dinner.html', context)
```

```html
<!-- articles/dinner.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <p>{{ picked }} 메뉴는 {{ picked|length }} 글자 입니다.</p>
  <h2>메뉴판</h2>
  <ul>
    {% for food in foods %}
    <li>{{ food }}</li>
    {% endfor %}
  </ul>
  {% if picked|length == 0 %}
  <p>메뉴가 소진 되었습니다.</p>
  {% else %}
  <p>아직 메뉴가 남았습니다.</p>
  {% endif %}
</body>
</html>
```

![image.png](attachment:41b3f8e4-d8f9-4e95-a8f4-2a7e3c83d464:image.png)

## 템플릿 상속

**페이지의 공통요소를 포함**하고, **하위 템플릿이 재정의 할 수 있는 공간**을 정의하는 기본 ‘skeleton’ 템플릿을 작성하여 상속 구조를 구축

```html
<!-- articles/base.html -->
<!doctype html>
<html lang="en">
  <head>
    bootstrap CDN 생략
  </head>
  <body>
    {% block content %}
    {% endblock content %}
    bootstrap CDN 생략
  </body>
</html>
```

```html
<!-- articles/index.html -->
{% extends "articles/base.html" %}

{% block style %}
<style>
  h1 {
    color: red !important
  }
</style>
{% endblock style %}

{% block content %}
  <h1>Hello, {{ name }}</h1>
{% endblock content %}
```

- `extends` tag
    
    자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림.
    
    반드시 자식 템플릿 최상단에 작성되어야 함.
    
- `block` tag
    
    하위 템플릿에서 재정의 할 수 있는 블록을 정의
    
    상위 템플릿에 작성하며 하위 템플릿이 작성할 수 있는 공간을 지정하는 것
    

## 요청과 응답

- **HTML form**
    
    HTTP 요청을 서버에 보내는 가장 편리한 방법
    
    실제 웹 서비스에서도 많이 사용되고 있다.
    
- `form` element
    
    사용자로부터 할당된 데이터를 서버로 전송
    
    웹에서 사용자 정보를 입력하는 여러 방식 (`text`, `password`, `checkbox` 등)을 제공
    

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <form action="https://search.naver.com/search.naver" method="GET">
    <label for="message">검색어</label>
    <input type="text" name="query" id="message">
    <input type="submit" value="submit">
  </form>
  {% comment %} 물음표는 form이 알아서 붙여준다. {% endcomment %}
</body>
</html>
```

- **form의 핵심 속성**
    - `action`
        
        입력 데이터가 전송될 URL을 지정 (목적지)
        
        만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
        
    - `method`
        
        데이터를 어떤 방식으로 보낼 것인지 정의
        
        데이터의 HTTP request methods (GET, POST)를 지정
        
        *당분간 GET만 쓸 예정, 작성하지 않을 경우 기본 값으로 지정된다.*
        
- `input` element
    
    사용자의 데이터를 입력 받을 수 있는 요소
    
    - `name` 속성
        
        input의 핵심 속성
        
        사용자가 입력한 데이터에 붙이는 이름 (key)
        
        데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근할 수 있음
        
- **Query String Parameters**
    
    사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버로 보내는 방법
    

### HTML form 활용 (throw - catch)

```python
# urls.py

from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('throw/', views.throw),
    path('catch/', views.catch),
]
```

```python
# views.py

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    print(request)  # <WSGIRequest: GET '/catch/?message=%EB%B0%A9%EA%B0%80%EB%B0%A9%EA%B0%80'>
    print(type(request))  # <class 'django.core.handlers.wsgi.WSGIRequest'>
    print(request.GET)  # <QueryDict: {'message': ['방가방가']}>
    print(request.GET.get('message'))  # 방가방가
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'articles/catch.html', context)
```

```html
<!-- articles/throw.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Throw</h1>
  <form action="/catch/" method="GET">
    <input type="text" name="message">
    <input type="submit"></input>
</body>
</html>
```

```html
<!-- articles/catch.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Catch</h1>
  <h2>{{ message }}를 받았다!</h2>
</body>
</html>
```

## Django URLs

모든 요청은 urls에서 받고 있다.

app은 늘어나게 될 것이다. (많아질 것이다.) 그럼 어떻게 관리를 해주어야 할까?

→ 한 곳에서 모든 것을 관리하는 게 문제라 분배해줄 필요가 있다.

→ **각 앱 마다의 통로를 따로 만들어주는 방법도 있다.**

→ **URL의 일부분을 변수로 바꿔준다!**

### **Variable Routing**

변수 경로, URL 일부에 변수를 포함시키는 것

변수는 view 함수의 인자로 전달 할 수 있음.

`<path_converter:variable_name>` 

- **Path converters**
    
    URL 변수의 타입을 지정 (str, int 등 5가지 타입 지원)
    

```python
# urls.py

from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('articles/<int:num>/', views.detail),
]
```

```python
# views.py

def detail(request, num):
    context = {
        'num' : num,
    }
    return render(request, 'articles/detail.html', context)
```

```html
<!-- articles/detail.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Detail</h1>
  <h2>{{ num }}번 게시글입니다.</h2>
</body>
</html>
```

detail 페이지 및 번호가 매겨서 URL 주소가 만들어진다.

### App URL mapping

각 앱에 URL을 정의하는 것

**프로젝트와 각 앱이 URL을 나누어 관리를 편하게 하기 위함**

`include` 를 사용한다.

```python
# firstpjt/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
```

```python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index),
    path('dinner/', views.dinner),
    path('search/', views.search),
    path('throw/', views.throw),
    path('catch/', views.catch, name='catch'),
    path('<int:num>/', views.detail),
    path('hello/<str:name>/', views.greeting),
]
```

```python
# pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
]
```

- `include()`
    
    프로젝트 내부 앱들의 URL을 참조할 수 있도록 매핑하는 함수
    
    URL의 일치하는 부분까지 잘라내고, 남은 문자열 부분은 후속 처리를 위해 include된 URL로 전달
    

## URL 이름 지정

### Naming URL patterns

URL에 이름을 지정하는 것 (path 함수의 name 인자를 정의해서 사용)

```python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('<int:num>/', views.detail, name='detail'),
    path('hello/<str:name>/', views.greeting, name='greeting'),
]
```

```python
# pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
]
```

### URL 표기 변화

url을 작성하는 모든 곳에서 변경

- `url` tag
    
    주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 반환
    
    ```html
    <!-- articles/index.html -->
    
    {% extends "base.html" %}
    
    {% block content %}
      <h1>Hello, {{ name }}</h1>
      <a href="{% url 'dinner' %}">dinner</a>
      <a href="{% url 'search' %}">search</a>
      <a href="{% url 'throw' %}">throw</a>
    {% endblock content %}
    ```
    

단순히 이름만으로는 완벽하게 분리할 수 없다.

→ **이름에 성(key)을 붙인다!**

- `app_name` 변수 값 설정
    
    ```python
    # articles/urls.py
    
    ...
    app_name = 'articles'
    ...
    ```
    
    ```html
    <!-- articles/index.html -->
    
    {% extends 'articles/base.html' %}
    
    {% block style %}
    <style>
      h1 {
        color: red
      }
    </style>
    {% endblock style %}
    
    {% block content %}
      <h1>Hello, {{ name }}</h1>
      <a href="{% url 'articles:dinner' %}">dinner</a>
      <a href="{% url 'articles:search' %}">search</a>
      <a href="{% url 'articles:throw' %}">throw</a>
    {% endblock content %}
    ```
    

## 참고

### 추가 템플릿 경로 지정

템플릿 기본 경로 외 커스텀 경로 추가하기

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # 이 부분을 수정한다.
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

각 하위 템플릿에서 `extends` 경로가 수정된다.

```html
<!-- articles/index.html -->

{% extends 'base.html' %}

{% block style %}
<style>
  h1 {
    color: red
  }
</style>
{% endblock style %}

{% block content %}
  <h1>Hello, {{ name }}</h1>
  <a href="{% url 'articles:dinner' %}">dinner</a>
  <a href="{% url 'articles:search' %}">search</a>
  <a href="{% url 'articles:throw' %}">throw</a>
{% endblock content %}
```

- `BASE_DIR`
    
    [`settings.py`](http://settings.py) 에서 경로지정을 편하게 하기 위해 최상단 지점을 지정해 둔 변수
    

### DTL 주의사항

Python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 명칭을 그렇게 설계했을 뿐, Python 코드로 실행되는 것이 아니며 Python과는 관련이 없다.

프로그래밍적 로직이 아니라 표현을 위한 것임을 명심하자.

프로그래밍적 로직은 되도록 view 함수에서 작성 및 처리를 하자.

### URL의 Trailing Slashes

Django는 URL 끝에 ‘/’가 없다면 자동으로 붙인다.

Django는 검색 엔진이 혼동하지 않게 하기 위해 무조건 붙이는 것을 선택한다.

그러나 모든 프레임워크가 이렇게 동작하는 것은 아니니 주의하자