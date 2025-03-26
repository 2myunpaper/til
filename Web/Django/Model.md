## Model

Djano는 Model을 통해 DB를 관리한다.

### Django Model

DB의 테이블을 정의하고 데이터를 조작(생성, 조회, 수정, 삭제 - **CRUD**) 할 수 있는 기능들을 제공.

테이블 구조를 설계하는 청사진.

```python
# articles/models.py

class Article(models.Model):
	title = models.CharField(max_length=10)
	content = models.TextField()
```

위와 같이 작성한 모델 클래스는 최종적으로 DB에 아래와 같은 테이블 구조를 만든다.

→ id 필드는 Django가 자동으로 생성한다.

→ 모델 클래스 == 테이블 설계도

| id | title | content |
| --- | --- | --- |
| .. | .. | .. |
| .. | .. | .. |

정리하자면,

`Article`이라는 클래스는 `Model`이라는 클래스를 상속받고,

클래스의 변수는 DB 테이블의 필드(Column)을 나타낸다는 것을 알 수 있다.

→ **Model Field**라 하고, **데이터의 유형과 제약 조건**을 정의한다.

## Model Field

DB 테이블의 필드(열)을 정의하며, 해당 필드에 저장되는 데이터 타입과 제약 조건을 정의한다.

*데이터가 날라가지 않도록 DB에 저장해줘야 하는데, DB는 Python 언어를 사용하지 않으므로,*

*Model.py을 이용해서 DB와 소통한다고 보면 되겠다.*

### Filed types (필드 유형)

데이터베이스에 저장될 데이터의 종류를 정의

`CharField()` : 제한된 길이의 문자열을 저장. 필드의 최대 길이를 결정하는 `max_length` 는 필수 옵션.

`TextField()` : 길이 제한이 없는 대용량 텍스트를 저장. (무한대는 아니며 사용하는 시스템에 따라 다름.)

<aside>

- **그 외 주요 필드**
    - 문자열 필드 : `CharField` , `TextField`
    - 숫자 필드 : `IntegerField` , `FloatField`
    - 날짜/시간 필드 : `DateField` , `TimeField` , `DateTimeField`
    - 파일 관련 필드 : `FileField` , `ImageField`
</aside>

### Filed options

필드의 동작과 제약 조건을 정의

- **제약 조건**
    
    특정 규칙을 강제하기 위해 테이블의 열이나 행에 적용되는 규칙이나 제한 사항
    
    *ex) 숫자만 저장되도록, 문자가 100자 까지만 저장되도록 하는 등*
    

<aside>

- **주요 필드 옵션**
    
    `null` : 데이터베이스에서 NULL 값을 허용할지 여부를 결정 (기본값 : False)
    
    `blank` : form에서 빈 값을 허용할지 여부를 결정 (기본값 : False)
    
    `default` : 필드의 기본값을 설정
    
    *※ 참고로 DB에서 True/False는 존재하지 않고, 1 또는 0으로 표현한다.*
    
</aside>

제약 조건은 Validator로 설정해줄 수도 있는데, 아래와 같이 코드로 표현할 수 있겠다.

```python
# SSAFY 과제 중 일부
# apis/models.py

from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

class APIInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.URLField(max_length=60, validators=[MinLengthValidator(20), MaxLengthValidator(60)])
    # 최소 길이, 최대 길이 판별
    documentation_url = models.URLField()
    auth_required = models.BooleanField()
    additional_info = models.JSONField(null=True, blank=True, default=None)
    # 빈 값으로 놓을 수 있게 설정.
    # null=True, blank=True, default=None
    created_at = models.DateTimeField(auto_now_add=True)
```

*그러나, 위의 과정까지는 DB에 아직 어떻게 하라고 요청한 것은 아니다.*

*DB에 요청하고 이동시키는 작업이 **Migrations**이라고 한다.*

## Migrations

model 클래스의 변경사항(필드 생성, 수정 삭제 등)을 DB에 최종 반영하는 방법

- **Migrations 과정**
    
    model class (설계도 초안) `makemigrations`→ migration 파일 (최종 설계도) `migrate`→ db.sqlite3 (DB)
    
    *설계도 초안에서 DB로 절대로 점프할 수 없다!*
    

`python [manage.py](http://manage.py) makemigrations` : model class를 기반으로 최종 설계도(migration) 작성

`python [manage.py](http://manage.py) migrate` : 최종 설계도를 DB에 전달하여 반영

*위의 과정을 통해 DB에 저장되는 테이블은, (appname)_(classname)으로 저장된다.*

### 추가 Migrations

| id | title | content | created_at | updated_at |
| --- | --- | --- | --- | --- |
| .. | .. | .. | .. | .. |
| .. | .. | .. | .. | .. |

위와 같이 이미 생성된 테이블에 필드를 추가해야 한다면?

```python
# articles/models.py

class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
```

`auto_now` : 데이터가 저장될 때마다 자동으로 현재 날짜 시간을 저장

`auto_now_add` : 데이터가 처음 생성될 때만 자동으로 현재 날짜 시간을 저장

models.py를 수정한 뒤 `makemigrations` 를 하면, warnning이 발생한다.

DB는 무결성 원칙으로 인해, 빈칸의 열을 추가할 수 없기 때문이다.

그러나, 옵션 선택으로 이를 해결할 수 있다.

(옵션 1. django에서 자동으로 값을 넣어줌. 옵션 2. 현재 명령어를 종료하고 default value를 개발자가 직접 넣을 수 있게 유도함.)

위와 같이 `makemigrations`를 하게 되면, migration 파일이 하나 더 생성된다.

이 파일은 전에 했던 `makemigrations` 파일을 `dependencies`로 설정한다.

이후 `migrate` 을 입력하면, DB가 업데이트된다.

정리하자면,

**model class에 변경 사항이 생겼다면, 반드시 새로운 설계도를 생성하고, DB에 반영해야 한다.**

## Admin Site

### Automatic admin interface

Django가 추가 설치 및 설정 없이 자동으로 제공하는 관리자 인터페이스.

데이터 확인 및 테스트 등을 진행하는데 매우 유용하다.

1. **admin 계정 생성**
    
    `python [manage.py](http://manage.py) createsuperuser` 
    
    email은 선택 사항이기 때문에 입력하지 않고 진행 가능
    
    비밀번호 입력 시 보안상 터미널에 출력되지 않으니 무시하고 입력 이어가기.
    
2. **DB에 생성된 admin 계정 확인**
3. **admin에 모델 클래스 등록**
    
    ```python
    # articles/admin.py
    
    from django.contrib import admin
    # 명시적 상대경로
    from .models import Article
    
    # Register your models here.
    admin.site.register(Article)
    ```
    
4. **admin site 로그인 후 등록된 모델 클래스 확인**
5. **데이터 생성, 수정, 삭제 테스트**
6. **테이블 확인**

## 참고

### 데이터베이스 초기화

- migration 파일 삭제
- db.sqlite3 파일 삭제
- [init.py](http://init.py) 및 migration 폴더를 지우지 않도록 주의하기!

### Migrations 기타 명령어

`python [manage.py](http://manage.py) showmigrations` : migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 명령어. [X] 표시가 있으면 migrate가 완료되었음을 의미

`python [manage.py](http://manage.py) sqlmigrate articles 0001` : 해당 migrations 파일이 SQL 언어(DB에서 사용하는 언어)로 어떻게 번역 되어 DB에 전달되는지 확인하는 명령어

### SQLite

데이터베이스 관리 시스템 중 하나이며 Django의 기본 데이터베이스로 사용됨.

파일로 존재하며 가볍고 호환성이 좋다.