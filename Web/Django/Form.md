## 개요

지금까지 사용자로부터 데이터를 제출 받기 위해 활용한 방법을 사용했다.

그러나 비정상적 혹은 악의적인 요청을 필터링 할 수가 없다.

그러므로 **유효한 데이터**인지에 대한 확인이 필요하다!

<aside>

**유효성 검사**

수집한 데이터가 정확하고 유효한지 확인하는 과

</aside>

유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복, 범위, 보안 등 많은 것들을 고려해야 한다.

→ 지금은 그냥 **Django가 제공하는 Form을 사용**한다.

## Django Form

`forms.py`

사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구

**→ 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공한다.**

```html
<!-- articles/new.html -->

<body>
  <h1>NEW</h1>
  <form action="{% url "articles:create" %}" method="POST">
    {% csrf_token %}
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
  <a href="{% url "articles:index" %}">[back]</a>
</body>
```

*이렇게 길게 작성했던 것을, 이제는 Django의 form을 이용하면 된다는 것이다.*

[`forms.py`](http://form.py) 는 기존에 존재하지 않는다.

새로 만들어야 하는데, 꼭 이름이 [`forms.py`](http://forms.py) 일 필요는 없다. (import할 거기 때문에, [`models.py`](http://models.py) 에서  작성할 수도 있다고 한다.)

*~~그러나 관행상 이렇게 이름을 지어놓도록 하자…!~~*

작성하는 방법은 [`models.py`](http://models.py) 와 비슷하다.

(그러나, `forms` 객체에는 `TextFeild()` 라는 객체가 존재하지 않는다..!)

```python
# forms.py

from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```

```python
# views.py

# 게시글을 작성하기 위한 페이지를 제공하는 함수
def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

```html
<!-- articles/new.html -->

<form action="{% url "articles:create" %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}  <!-- form의 요소들을 p형태로 출력해줌. (Form rendering options) -->
  <input type="submit">
</form>
```

위와 같이 입력해서 서버에 접속하면, html로 자동적으로 변환이 된다.

*Form rendering options는 공식 문서를 참고하는데,*

[`forms.py`](http://forms.py) 에서 바로 변환할 수 있는 방법이 존재한다.

→ **Widget**을 이용한다.

### Widgets

HTML `input` element의 표현을 담당한다.

Widget은 단순히 input 요소의 속성 및 출력 되는 부분을 변경하는 것이다.

```python
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
    # widget을 사용하여, content를 Textarea로 보여주게 한다.
```

## Django ModelForm

*만약 사용자로부터 받아야 하는 필드 개수가 100개라면..?*

*→* [`forms.py`](http://forms.py) *도 동일하게 100개를 입력해야 되나..? 너무 비효율적이다!*

→ 이를 해결하기 위해 존재하는 것이 **Django ModelForm**이다.

| Form | ModelForm |
| --- | --- |
| 사용자 입력 데이터를 **DB에 저장하지 않을 때** 유용하다. | 사용자 입력 데이터를 **DB에 저장해야 할 때** 유용하다. |
| *ex) 검색, 로그인* | *ex) 게시글 작성, 회원가입* |

*Form을 이용해도 되지만, DB에 저장해야 할 경우 중복 사항 등 더 편리하게 적용할 수 있는 건 **ModelForm**이다.*

<aside>

**ModelForm**

Model과 연결된 Form을 자동으로 생성해주는 기능을 제공한다.

</aside>

```python
# forms.py
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'  # 모든 필드를 반영한다.
```

이렇게 하면, 위에 Form처럼 html 처리를 하지 않아도, **자동적으로 html 요소가 반영된다.**

(auto로 입력되는 요소들은 알아서 표시를 하지 않는다.) 

*~~이때까지 난 뭐한거야.~~*

### Meta class

*※ 정보의 정보를 Meta라고 표현한다. (Model에 대한 정보를 저장하는 클래스라는 뜻으로 생각.)*

`ModelForm`의 정보를 작성하는 곳

- `fields` 및 `exclude` 속성
    
    `fields` 속성을 사용하여 **모델에 포함할 필드를 지정**한다.
    
    `exclude` 속성을 사용하여 **모델에서 포함하지 않을 필드를 지정**할 수도 있다.
    
    둘 다 리스트 혹은 튜플로 부여하면 된다.
    

```python
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title',)
        exclude = ('contents',)
```

*문법적으로 너무 깊게 파고들려고 하지 말자.*

### ModelForm 적용

```python
# views.py

def create(request):
    form = ArticleForm(request.POST)

    # 데이터가 유효한지 검사 (유효성 검사)
    if form.is_valid():
        # 유효성 검사를 통과 했다면 (데이터 저장)
        article = form.save()
        return redirect('articles:detail', article.pk)
    # 유효성 검사를 통과하지 못했다면
    # 현재 사용자가 게시글을 작성하는 템플릿(new 페이지)을 다시 한 번 응답
    context = {
        # 왜 유효성 검사를 통과하지 못했는지에 대한 에러메시지를 담고 있음
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

- `is_valid()`
    
    여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 `Boolean` 으로 변환
    
    빈 값을 입력할 경우,
    
    `is_valid()` 에 의해 False로 평가되고 `form` 객체에는 그에 맞는 에러 메시지가 포함되어 다음 코드로 진행된다.
    

edit 및 update에도 적용해보면 아래와 같다.

```python
# views.py

def edit(request, pk):
    # 몇번 게시글 정보를 보여줄지 조회
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
    
def update(request, pk):
    # 어떤 글을 수정하는지 먼저 조회
    article = Article.objects.get(pk=pk)
		
		# 사용자가 새로 입력한 데이터를 받아서 form 인스턴스 생성
    form = ArticleForm(request.POST, instance=article)

    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```

```html
<!-- articles/edit.html -->

<form action="{% url "articles:update" article.pk %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
```

### `save` 메서드

데이터베이스 객체를 만들고 저장하는 `ModelForm` 의 인스턴스 메서드.

`save()` 메서드가 생성과 수정을 구분하는 방법은,

키워드 인자 `instance` 여부를 통해 생성할 지, 수정할 지를 결정한다.

```python
# CREATE
form = ArticleForm(request.POST)
form.save()

# UPDATE
form = ArticleForm(request.POST, instance=article)
form.save()
```

### Django Form 정리

**사용자로부터 데이터를 수집하고 처리하기 위한 강력하고 유연한 도구**

HTML `form` 생성, 데이터 유효성 검사 및 처리를 쉽게 할 수 있도록 도와준다.

## HTTP 요청 다루기

new와 create view 함수간 공통점과 차이점은?

→ 공통점은 데이터 생성을 구현하기 위한 것이다.

→ 차이점은 new는 `GET` method 요청만을, create는 `POST` method 요청만을 처리한다.

→ HTTP request method 차이점을 활용해 **동일한 목적을 가지는 2개의 view 함수를 하나로 구조화**한다.

### new & create 함수 결합

```python
# views.py

def create(request):
    # 1. 요청 메서드가 POST라면
    if request.method == 'POST':
        # 1.1 사용자로부터 받은 데이터를 인자로 통째로 넣어서 form 인스턴스 생성
        form = ArticleForm(request.POST)
        # 1.2 유효성 검사
        if form.is_valid():
            # 1.3 유효성 검사가 통과한다면 저장
            article = form.save()
            # 1.4 상세 페이지로 리다이렉트
            return redirect('articles:detail', article.pk)
    # 2. 요청 메서드가 POST가 아니라면 (GET, PUT, DELETE...)
    else:
        # 2.1 ArticleForm 인스턴스를 생성
        form = ArticleForm()

    # case 1 : 1.2에서 내려왔을 때 : 에러메시지를 담은 form
    # case 2 : 2.1이 끝나고 내려왔을 때 : 빈 form
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

두 함수의 유일한 차이점이었던 **request method에 따른 분기**

→ `POST` 일 때는 과거 create 함수 구조였던 객체 생성 및 저장 로직 처리

→ `POST` 가 아닐 때는 과거 new 함수에서 진행했던 `form` 인스턴스 생성

→ `context` 에 담기는 `form` 은

1. `is_valid()` 를 통과하지 못해 에러메시지를 담은 `form` 이거나
2. `else` 문을 통한 `form` 인스턴스

→ 그럼 new라는 파일은 필요 없다!

### edit & update 함수 결합

위와 같은 방법으로 통합할 수 있겠다.

```python
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

## 참고

### ModelForm의 키워드 인자 구성

```python
form = ArticleForm(request.POST, instance=article)
# 첫 번째 인자는 data, 두 번째 인자는 instance이다.
```

`data` 는 첫번째에 위치한 키워드 인자이기 때문에 생략 가능하지만,

`instance` 는 9번째에 위치한 키워드 인자이기 때문에 생략할 수 없다.

### Widgets 응용

```python
class ArticleForm(forms.ModelForm):
	title = forms.CharField(
		label='제목',
		widget=forms.Textinput(
			altrs={
				'class': 'my-title',
				'placeholder': 'Enter the title',
				'maxlength': 10,
			}
		),
		error_messages={'required': '제목을 입력해주세요.'}
	)
```

[Widgets | Django documentation](https://docs.djangoproject.com/en/5.1/ref/forms/widgets/)

공식 문서를 참고해서 사용해본다.

참고로, 필드를 template 파일에서 수동으로 렌더링 할 수도 있다.

```html
{{ form.non_field_errors }}
<form action="..." method="POST">
	{% csrf_token %}
	<div>
		{{ form.title.errors }}
		<label for="{{ form.title.id_for_label }}">Title:</label>
		{{ form.title }}
	</div>
...
```