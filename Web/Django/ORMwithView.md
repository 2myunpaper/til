이번 회차에서는 단일 게시글을 조회를 주로 본다.

## Read

```python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
		...
    path('<int:pk>/', views.detail, name='detail'),
]
```

```python
# articles/views.py

# 특정 단일 게시글의 상세 페이지를 응답 (* 단일 게시물 조회)
def detail(request, pk):  # pk -> URL에서 사용한 Variable Routing과 변수명이 동일해야 한다.
    # pk로 들어온 정수 값을 활용 해 DB에 id가 pk인 게시글을 조회 요청
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)
```

```html
<!-- templates/articles/detail.html -->

<h1>DETAIL</h1>
<hr>
{% comment %} 단일 게시글 출력 {% endcomment %}
<p>제목: {{ article.title }}</p>
<p>내용: {{ article.content }}</p>
<p>작성일: {{ article.created_at }}</p>
<p>수정일: {{ article.updated_at }}</p>
<hr>
<a href="{% url "articles:index" %}">[BACK]</a>
```

단일 게시글 페이지 링크 작성은 아래와 같이 html을 작성할 수 있겠다.

```html
<!-- templates/articles/index.html -->

<h1>Articles</h1>
<hr>
{% comment %} 전체 게시글 출력 {% endcomment %}
{% for article in articles %}
  <p>글 번호: {{ article.pk }}</p>
  <a href="{% url "articles:detail" pk=article.pk %}">
  <!-- argument를 url 태그에 입력해주어야 한다! -->
    <p>글 제목: {{ article.title }}</p>
  </a>
  <p>글 내용: {{ article.content }}</p>
  <hr>
{% endfor %}
```

`NoReverseMatch` *에러가 떴을 때는 url문제일 가능이 매우매우 크다!* 

## Create

Create 로직을 구현하기 위해 필요한 view 함수의 개수는?

→ 사용자 입력 데이터를 받을 페이지를 렌더링 `new`

→ 사용자가 입력한 요청 데이터를 받아 DB에 저장 `create`

→ **총 2가지가 필요한 것으로 볼 수 있겠다.**

```python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    ...
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
```

```python
# articles/views.py

# 게시글을 작성하기 위한 페이지를 제공하는 함수
def new(request):
    return render(request, 'articles/new.html')

# 사용자로부터 데이터를 받아 저장하고 저장이 완료되었다는 페이지를 제공하는 함수
def create(request):
    # 사용자로부터 받은 데이터를 추출
    # request.GET은 쿼리, dict 형태로 되어 있다.
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    # DB에 저장 요청
    # 1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2.
    # 유효성 검사할 타이밍이 생길 수 있으니, 이 방법을 추천한다.
    article = Article(title=title, content=content)
    article.save()

    # 3.
    # Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')
```

```html
<!-- templates/articles/new.html -->

<h1>NEW</h1>
<form action="{% url "articles:create" %}" method="GET">
  <div>
    <label for="title">Title: </label>
    <input type="text" name="title" id="title">
  </div>
  <div>
    <label for="content">Content: </label>
    <textarea name="content" id="content"></textarea>
  </div>
  <input type="submit">
</form>
<hr>
<a href="{% url "articles:index" %}">[BACK]</a>
```

```html
<!-- templates/articles/create.html -->

<h1>게시글이 문제 없이 작성되었습니다.</h1>
<a href="{% url "articles:index" %}">[BACK]</a>
```

## HTTP request methods

<aside>

**HTTP**

네트워크 상에서 데이터(리소스)를 주고 받기 위한 약속

</aside>

**HTTP request methods**란,

- 데이터에 대해 수행을 원하는 작업(행동)을 나타내는 것
    
    → 서버에게 원하는 작업의 종류를 알려주는 역할
    
- 클라이언트가 웹 서버에 특정 동작을 요청하기 위해 사용하는 표준 명령어
- 대표 메서드는 `GET` `POST` 가 있다.

### `GET` Method

서버로부터 데이터를 요청하고 받아오는데(조회) 사용.

1. 데이터 전송
    
    URL의 **쿼리 문자열(Query String)**을 통해 데이터를 전송한다.
    
2. 데이터 제한
    
    **URL 길이에 제한**이 있어 **대량의 데이터 전송에는 적합하지 않다.**
    
3. 브라우저 히스토리
    
    요청 URL이 브라우저 **히스토리에 남는다.**
    
4. 캐싱
    
    브라우저는 GET 요청의 응답을 로컬에 저장할 수 있다.
    
    동일한 URL로 다시 요청할 때, **서버에 접속하지 않고 저장된 결과를 사용**한다.
    
    **페이지 로딩 시간을 크게 단축시킨다.**
    

ex) 검색 쿼리 전송, 웹 페이지 요청, API에서 데이터 조회

### `POST` Method

서버에 데이터를 제출하여 리소스를 변경(생성, 수정, 삭제) 하는 데 사용.

1. 데이터 전송
    
    **HTTP Body**를 통해 데이터를 전송
    
2. 데이터 제한
    
    `GET` 에 비해 **더 많은 양의 데이터를 전송**할 수 있다.
    
3. 브라우저 히스토리
    
    `POST` 요청은 브라우저 **히스토리에 남지 않는다.**
    
4. 캐싱
    
    `POST` 요청은 기본적으로 **캐시 할 수 없다.**
    
    `POST` 요청이 일반적으로 **서버의 상태를 변경하는 작업을 수행**하기 때문이다.
    

ex) 로그인 정보 제출, 파일 업로드, 새 데이터 생성 (새 게시글 작성), API에서 데이터 변경 요청

`GET` 과 `POST` 의 기술적인 특징을 비교해서 사용해야 한다. (보안 측면에서 바라보는 것은 아님.)

→ `GET` 은 **데이터 조회** 목적

→ `POST` 는 **데이터 생성이나 수정**에 주로 사용

그럼 위에서 했던 Create 기능 구현 중 new.html에서 `GET` 을 `POST`로 바꿔보자.

→ 에러가 뜬다! `Error 403`

→ “**CSRF** **token**이 누락되었다”라는 응답이 뜬다.

→ 이 에러를 **HTTP response status code**라고 한다.

## HTTP response status code

서버가 클라이언트의 요청에 대한 처리 결과를 나타내는 3자리 숫자.

→ 클라이언트에게 **요청 처리 결과를 명확히 전달**한다.

→ 문제 발생 시 **디버깅에 도움.**

→ 웹 애플리케이션의 동작을 제어하는 데 사용한다.

<aside>

**403 Forbidden**

서버에 요청이 전달되었지만, **권한 때문에 거절**되었다는 것을 의미한다.

</aside>

### CSRF

Cross-Site-Request-Forgery. 사이트 간 요청 위조

→ 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹 페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법

→ **CSRF 토큰**을 심어주면 해킹이 방지된다.

**요청 시 CSRF Token을 함께 보내야 하는 이유**

→ DJango가 직접 제공한 페이지에서 데이터를 작성하고 있는 것인지 확인 수단이 필요하기 때문.

**왜 `POST` 일 때만 Token을 확인할까?**

→ 단순 조회를 위한 `GET` 과 달리 특정 리소스에 변경(생성, 수정, 삭제)을 요구하는 의미와 기술적인 부분을 가지고 있기 때문이다.

→ DB에 조작을 가하는 요청은 반드시 인증 수단이 필요하다.

→ 데이터베이스에 대한 변경 사항을 만드는 요청이기 때문에 토큰을 사용해 최소한의 신원 확인을 하는 것이다.

정리하자면,

Django에서는 `POST` 를 사용할 경우 **CSRF token을 확인한다**는 것!

## Redirect

그런데, 게시글 작성 후 완료를 알리는 페이지가 흔히 있는가? → 그렇지 않다.

**서버는 데이터 저장 후 페이지를 응답하는 것이 아닌 사용자를 적절한 기존 페이지로 보내야 한다.**

→ 서버가 클라이언트를 직접 다른 페이지로 보내는 것이 아니라, 클라이언트가 `GET` **요청을 한번 더 보내도록 응답하는 것을 의미**한다.

- `redirect()`
    
    클라이언트가 인자에 작성된 주소로 다시 요청을 보내도록 하는 함수
    
    ```python
    # articles/views.py
    
    from django.shortcuts import render, redirect
    
    def create(request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
    
        # return redirect('article:index')
        return redirect('articles:detail', article.pk)
    ```
    

## Delete

```python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
		...
    path('<int:pk>/delete/', views.delete, name='delete'),
]

```

```python
# articles/views.py

def delete(request, pk):
    # 어떤 게시글을 지우는지 먼저 조회
    article = Article.objects.get(pk=pk)
    # DB에 삭제 요청
    article.delete()
    return redirect('articles:index')
```

## Update

Update 로직을 구현하기 위해 필요한 view 함수의 개수는?

→ 사용자 입력 데이터를 받을 페이지를 렌더링 `edit`

→ 사용자가 입력한 데이터를 받아 DB에 저장 `update` 

```python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
		...
    path('<int:pk>/edit', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
```

```python
# articles/views.py

def edit(request, pk):
    # 몇 번 게시글 정보를 보여줄지 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk)
```

```html
<!-- templates/articles/edit.html -->

<h1>EDIT</h1>
<form action="{% url "articles:update" article.pk %}" method="POST">
  {% csrf_token %}
  <div>
    <label for="title">Title: </label>
    <input type="text" name="title" id="title" value="{{ article.title }}">
  </div>
  <div>
    <label for="content">Content: </label>
    <textarea name="content" id="content">{{ article.content }}</textarea>
  </div>
  <input type="submit">
</form>
<hr>
<a href="{% url 'articles:index' %}">[BACK]</a>
```

### `Delete` 와 `Update` 가 반영된 `detail.html`

```html
<h1>DETAIL</h1>
<hr>
{% comment %} 단일 게시글 출력 {% endcomment %}
<p>제목: {{ article.title }}</p>
<p>내용: {{ article.content }}</p>
<p>작성일: {{ article.created_at }}</p>
<p>수정일: {{ article.updated_at }}</p>
<hr>
<form action="{% url "articles:edit" pk=article.pk%}">
  <input type="submit" value="EDIT">
</form>
<form action="{% url "articles:delete" pk=article.pk %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="DELETE">
</form>
<a href="{% url 'articles:index' %}">[BACK]</a>
```

## 참고

### `GET`과 `POST`

|  | GET | POST |
| --- | --- | --- |
| 데이터 전송 방식 | URL의 Query string parameter | HTTP body |
| 데이터 크기 제한 | 브라우저 제공 URL의 최대 길이 | 제한 없음 |
| 사용 목적 | 데이터 검색 및 조회 | 데이터 제출 및 변경 |
- `GET` 요청이 필요한 경우
    1. **캐싱 및 성능**
        
        `GET` 요청은 캐시될 수 있고, 이전에 요청한 정보를 새로 요청하지 않고 사용할 수 있다.
        
        특히, 동일한 검색 결과를 여러 번 요청하는 경우, `GET` 요청은 캐시를 활용하여 더 빠르게 응답할 수 있다.
        
    2. **가시성 및 공유**
        
        `GET` 요청은 URL에 데이터가 노출되어 있기 때문에 사용자가 해당 URL을 북마크하거나 다른 사람이 공유하기 용이하다.
        
    3. **RESTful API 설계**
        
        HTTP 메서드의 의미에 따라 동작하도록 디자인된 API의 일관성을 유지할 수 있다.
        

<aside>

*ex) HTTP request methods를 활용한 효율적인 URL 구성*

(GET) `articles/1/` → 1번 게시글 조회 요청!

(POST) `articles/1/` → 1번 게시글 조작 요청!

</aside>