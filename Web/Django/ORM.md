## ORM

---

**Object-Relational-Mapping**

객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술.

*파이썬을 알아듣지 못하는 시스템과 소통하는 것을 예로 들 수 있겠다.*

### ORM의 역할

Django와 DB간에 사용하는 언어가 다르기 때문에 소통이 불가 하다.

Django는 Python Object를 사용하고, DB는 SQL을 사용한다.

그래서 Django에 내장된 ORM이 중간에서 이를 해석해준다.

*Django를 사용할 시 Python을 그대로 사용하되, **ORM을 위한 문법을 알 필요**가 있다.*

## QuerySet API

---

ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는 데 사용하는 도구

→ **API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리**한다.

*→ ORM에 맞춘 QuerySet을 맞추면 된다.*

<aside>

*ex)* `Article.objects.all()` 

**Model class - Manager - Queryset API**

으로 이루어져 있다.

</aside>

- **Query**
    
    데이터베이스에 특정한 데이터를 보여 달라는 요청
    
    **“쿼리문을 작성한다.”** → “원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다.”
    
    파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달한다.
    
- **Queryset**
    
    데이터베이스에게서 전달 받은 객체 목록(데이터 모음)
    
    → 순회 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있다.
    
    **Django ORM을 통해 만들어진 자료형**
    
    단, 데이터베이스가 **단일한 객체를 반환 할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환**된다.
    
- **QuerySet API**
    
    python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장, 조회, 수정, 삭제(CRUD)하는 것.
    
    ※ **CRUD** : 소프트웨어가 가지는 기본적인 데이터 처리 기능 (**Create, Read, Update, Delete**)
    

## QuerySet API 실습

---

### 사전 준비

실습을 하기 전, 두 개의 pip를 설치한다.

```bash
$ pip install ipython
$ pip install django-extensions
```

두 pip는 가독성을 위한 설치 파일이다.

그리고 `django-extensions` 같은 경우는 django 프로젝트 앱에 등록 (settings.py 에 등록) 해야 하니 참고해야 한다.

*→ pip 마다 다르므로, 공식 문서를 꼭 끝까지 읽는 습관을 가져야 한다.*

[Installation instructions — django-extensions 3.2.3 documentation](https://django-extensions.readthedocs.io/en/latest/installation_instructions.html)

```python
# settings.py

INSTALLED_APPS = [
    # 1. 직접 생성한 app
    'articles',
    # 2. 설치한 앱(3rd party library)
    'django_extensions',
    # 3. 내장 앱
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

그리고 나서, Django shell을 실행한다.

```bash
$ python manage.py shell_plus
```

그러면 창에 엄청나게 import를 해오는데,

그 중 model에서 만든 클래스도 import한 것을 확인할 수 있다.

그래서 위와 같이 설정해 놓으면, 편리한 개발 환경을 만들 수 있겠다!

- **Django shell**
    
    Django 환경 안에서 실행되는 python shell
    
    입력하는 QuerySet API 구문이 Django 프로젝트에 영향을 미침.
    

그럼 위에서 잠깐 배운 `Articles.objects.all()` 명령어를 사용해보자.

에러가 뜬다…? 왜? → .gitignore 파일 때문이다. git에 올릴 때는 DB 파일을 무시하고 올려야 한다.

그러므로, `migrate` 명령을 먼저 한 다음, 조회를 해보아야 할 것이다.

### Create

본격적으로 데이터 객체를 만들어보자.

- **첫 번째 방법**
    
    DB에 저장하려면, `save()` 인스턴스 메서드를 사용
    
    ```bash
    # 특정 테이블에 새로운 행을 추가하여 데이터 추가
    >>> article = Article()
    >>> article
    <Article: Article object (None)>
    
    >>> article.title = 'first'  # 인스턴스 변수(title)에 값을 할당
    >>> article.content = 'django!'  # 인스턴스 변수(content)에 값을 할당
    
    # save를 하지 않으면 아직 DB에 값이 저장되지 않음
    >>> article
    <Article: Article object (None)>
    
    >>> Article.objects.all()
    <QuerySet []>
    
    # save를 호출하고 확인하면 저장된 것을 확인
    >>> article.save()
    >>> article
    <Article: Article object (1)>
    >>> article.id
    1
    >>> article.pk
    1
    >>> Article.objects.all()
    <QuerySet [Article: Article object (1)]>
    
    # 인스턴스 article을 활용하여 인스턴스 변수 활용하기
    >>> article.title
    'first'
    
    >>> article.content
    'django!'
    
    >>> article.created_at
    datetime.datetime(2023, 6, 30 ...)
    ```
    
- **두 번째 방법**
    
    테이블에 한 행(레코드)이 쓰여진 것
    
    ```bash
    >>> article = Article(title='second', content='django!')
    
    # 아직 저장 되어있지 않음
    >>> article
    <Article: Article object (None)>
    
    # save를 호출해야 저장됨
    >>> article.save()
    >>> article
    <Article: Article object (2)>
    >>> Article.objects.all()
    <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>
    
    # 값 확인
    >>> article.pk
    2
    >>> article.title
    'second'
    >>> article.content
    'django!'
    ```
    
- **세 번째 방법**
    
    QuerySet API 중 `create()` 메서드 활용
    
    ```bash
    # 위 2가지 방법과 달리 바로 저장 이후 바로 생성된 데이터가 반환된다.
    
    >>> Article.objects.create(title='third', content='django!')
    <Article: Article object (3)>
    ```
    

### Read

Return new QuerySets : `all()` , `filter()` 

Do not return QuerySets : `get()` 

- `all()`
    
    전체 데이터 조회
    
    ```bash
    >>> Article.objects.all()
    ```
    
- `filter()`
    
    주어진 매개변수와 일치하는 객체를 포함하는 QuerySet 반환
    
    *하나 건, 여러 개이건, 0개 이건 다 QuerySet으로 결과를 출력한다.*
    
    ```bash
    >>> Article.objects.filter(content='django!')
    <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
    
    >>> Article.objects.filter(title='abc')
    <QuerySet []>
    
    >>> Article.objects.filter(title='first')
    <QuerySet [<Article: Article object (1)>]>
    ```
    
- `get()`
    
    주어진 매개변수와 일치하는 객체를 반환
    
    primary key와 같이 고유성(uniqueness)을 보장하는 조회에서 사용해야 함.
    
    ```bash
    >>> Article.objects.get(pk=1)
    <Article: Article object (1)>
    
    >>> Article.objects.get(pk=100)
    DoesNotExist ...  # 객체를 찾을 수 없음.
    
    >>> Article.objects.get(content='django!')
    MultipleObjectsReturned ...  # 둘 이상의 객체를 찾음.
    ```
    

### Update

인스턴스 변수를 변경 후 `save` 메서드 호출

```bash
# 수정할 인스턴스 조회
>>> article = Article.objects.get(pk=1)

# 인스턴스 변수를 변경
>>> article.title = 'byebye'

# 저장
>>> article.save()

# 정상적으로 변경된 것을 확인
>>> article.title
'byebye'
```

### Delete

삭제하려는 데이터 조회 후 `delete` 메서드 호출

```bash
# 삭제할 인스턴스 조회
>>> article = Article.objects.get(pk=1)

# delete 메서드 호출 (삭제 된 객체가 반환)
>>> article.delete()
(1, {'articles.Article' : 1})

# 삭제한 데이터는 더이상 조회할 수 없음
>>> Article.objects.get(pk=1)
DoesNotExist ...
```

## ORM with view

---

Django shell에서 연습했던 Queryset API를 직접 view 함수에서 사용해보자.

이번 시간에는 전체 게시글 조회 부분만 본다.

### 전체 게시글 조회

```python
# views.py

from .models import Article

def index(request):
  articles = Article.objects.all()
  context = {
    'articles': articles
  }
  return render(request, 'articles/index.html', context)
```

```html
<!-- articles/index.html -->

{% block content %}
<h1>Articles</h1>
<hr>
{% for article in articles %}
  <p>글 번호: {{ article.pk }}</p>
  <p>글 제목: {{ article.title }}</p>
  <p>글 내용: {{ article.content }}</p>
  <hr>
{% endfor %}
{% endblock content %}
```

## 참고

---

### Field lookups

Query에서 조건을 구성하는 방법

```bash
# Field lookups 예시

# 내용에 'dja'가 포함된 모든 모든 게시글 조회
Article.objects.filter(content__contains='dja')

# 제목이 he로 시작하는 모든 게시글 조회
Article.objects.filter(title__startswith='he')
```

*이 외에는 공식 문서를 또 참고해보자. (Field lookups 참고)*

[QuerySet API reference | Django documentation](https://docs.djangoproject.com/en/5.1/ref/models/querysets/)

### ORM, QuerySet API를 사용하는 이유

1. **데이터베이스 추상화**
    
    개발자는 특정 데이터베이스 시스템에 종속되지 않고 일관된 방식으로 데이터를 다룰 수 있음
    
2. **생산성 향상**
    
    복잡한 SQL 쿼리를 직접 작성하는 대신 Python 코드로 데이터베이스 작업을 수행할 수 있음
    
3. **객체 지향적 접근**
    
    데이터베이스 테이블을 Python 객체로 다룰 수 있어 객체 지향 프로그래밍의 이점을 활용할 수 있음.