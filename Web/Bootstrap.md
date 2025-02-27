## Bootstrap

[Get started with Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

**자세한 사용방법은 꼭 공식문서를 읽어보자!**

**CSS 프론트엔드 프레임워크** (Toolkit)

미리 만들어진 다양한 디자인 요소들을 제공하여 웹 사이트를 빠르고 쉽게 개발할 수 있도록 함

### CDN (Content Delivery Network)

지리적 제약 없이 빠르고 안전하게 콘텐츠를 전송할 수 있는 전송 기술

서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화 (웹 페이지 로드 속도를 높인다.)

지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 전달함.

*즉, 부트스트랩을 이용하는 방법은,*

*실제 css파일과 자바스크립트 파일을 다운 받아 사용하는 것이 아니라, CDN을 이용하여 부트스트랩을 이용하는 것이다.*

### Bootstrap 사용 가이드

부트스트랩은 클래스 선언으로 사용하면 된다.

**{property}{sides}-{size}** 형태로 클래스가 나타난다.

*ex)* mt-5 → margin, top, 3 rem

여기서, ‘rem’ 은 무슨 뜻인가?

> rem은 "root em"의 약자로, HTML 문서의 **루트 요소(`html`)의 폰트 크기를 기준**으로 하는 상대적 단위
> 

*em 이라는 단위도 있는데,*

*rem은 전체적인 크기, em은 부분적인 크기를 조정하는 단위라고 알아두면 될 것 같다.*

**즉,**

**Bootstrap에는 특정한 규칙이 있는 클래스 이름으로 스타일 및 레이아웃이 미리 작성되어 있다!**

## Reset CSS

모든 HTML 요소 스타일을 일관된 기준으로 재설정하는 간결하고 압축된 규칙 세트

→ HTML Element, Table, List 등의 요소들에 일관성 있게 스타일을 적용 시키는 기본 단계

모든 브라우저는 각자의 user agent stylesheet를 가지고 있다.

문제는 이 설정이 브라우저마다 상이하나는 것이다.

모든 브라우저에서 웹사이트를 동일하게 보이게 만들어야 하는 개발자에겐 매우 골치 아픈 일이다.

그러므로 모두 똑같은 스타일 상태로 만들고 스타일 개발을 시작하는 것이 중요하다.

→ **Reset CSS**

### Normalize CSS

Reset CSS 방법 중 대표적인 방법

웹 표준 기준으로 브라우저 중 하나가 불일치 한다면 차이가 있는 브라우저를 수정하는 방법

부트스트랩은 `bootstrap-reboot.css` 라는 파일명으로 `normalize.css` 를 자체적으로 커스텀해서 사용하고 있다.

## Bootstrap 활용

### Typography

제목, 본문 텍스트, 목록 등

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <!-- Bootstrap 선언 -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>
  <!-- Headings -->
  <h1>h1. Bootstrap heading</h1>
  <h2>h2. Bootstrap heading</h2>
  <h3>h3. Bootstrap heading</h3>
  <h4>h4. Bootstrap heading</h4>
  <h5>h5. Bootstrap heading</h5>
  <h6>h6. Bootstrap heading</h6>

  <!-- Display Headings -->
  <h1 class="display-1">Display 1</h1> 
  <h1 class="display-2">Display 2</h1>
  <h1 class="display-3">Display 3</h1>
  <h1 class="display-4">Display 4</h1>
  <h1 class="display-5">Display 5</h1>
  <h1 class="display-6">Display 6</h1>
  
  <!-- Inline elements -->
  <p>You can use the mark tag to <mark>highlight</mark> text.</p>
  <p><del>This line of text is meant to be treated as deleted text.</del></p>
  <p><s>This line of text is meant to be treated as no longer accurate.</s></p>
  <p><ins>This line of text is meant to be treated as an addition to the document.</ins></p>
  <p><u>This line of text will render as underlined.</u></p>
  <p><small>This line of text is meant to be treated as fine print.</small></p>
  <p><strong>This line rendered as bold text.</strong></p>
  <p><em>This line rendered as italicized text.</em></p>

  <!-- list -->
  <ul class="list-unstyled">
    <li>This is a list.</li>
    <li>It appears completely unstyled.</li>
    <li>Structurally, it's still a list.</li>
    <li>However, this style only applies to immediate child elements.</li>
    <li>Nested lists:
      <ul>
        <li>are unaffected by this style</li>
        <li>will still show a bullet</li>
        <li>and have appropriate left margin</li>
      </ul>
    </li>
    <li>This may still come in handy in some situations.</li>
  </ul>
  
  <!-- Bootstrap 선언 -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>

</html>

```

### Bootstrap Color System

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>
  <!-- text colors -->
  <p class="text-primary">.text-primary</p>
  <p class="text-primary-emphasis">.text-primary-emphasis</p>
  <p class="text-secondary">.text-secondary</p>
  <p class="text-secondary-emphasis">.text-secondary-emphasis</p>
  <p class="text-success">.text-success</p>
  <p class="text-success-emphasis">.text-success-emphasis</p>
  <p class="text-danger">.text-danger</p>
  <p class="text-danger-emphasis">.text-danger-emphasis</p>
  <p class="text-warning bg-dark">.text-warning</p>
  <p class="text-warning-emphasis">.text-warning-emphasis</p>
  <p class="text-info bg-dark">.text-info</p>
  <p class="text-info-emphasis">.text-info-emphasis</p>
  <p class="text-light bg-dark">.text-light</p>
  <p class="text-light-emphasis">.text-light-emphasis</p>
  <p class="text-dark bg-white">.text-dark</p>
  <p class="text-dark-emphasis">.text-dark-emphasis</p>

  <p class="text-body">.text-body</p>
  <p class="text-body-emphasis">.text-body-emphasis</p>
  <p class="text-body-secondary">.text-body-secondary</p>
  <p class="text-body-tertiary">.text-body-tertiary</p>

  <p class="text-black bg-white">.text-black</p>
  <p class="text-white bg-dark">.text-white</p>
  <p class="text-black-50 bg-white">.text-black-50</p>
  <p class="text-white-50 bg-dark">.text-white-50</p>

  <!-- background colors -->
  <div class="p-3 mb-2 bg-primary text-white">.bg-primary</div>
  <div class="p-3 mb-2 bg-primary-subtle text-primary-emphasis">.bg-primary-subtle</div>
  <div class="p-3 mb-2 bg-secondary text-white">.bg-secondary</div>
  <div class="p-3 mb-2 bg-secondary-subtle text-secondary-emphasis">.bg-secondary-subtle</div>
  <div class="p-3 mb-2 bg-success text-white">.bg-success</div>
  <div class="p-3 mb-2 bg-success-subtle text-success-emphasis">.bg-success-subtle</div>
  <div class="p-3 mb-2 bg-danger text-white">.bg-danger</div>
  <div class="p-3 mb-2 bg-danger-subtle text-danger-emphasis">.bg-danger-subtle</div>
  <div class="p-3 mb-2 bg-warning text-dark">.bg-warning</div>
  <div class="p-3 mb-2 bg-warning-subtle text-warning-emphasis">.bg-warning-subtle</div>
  <div class="p-3 mb-2 bg-info text-dark">.bg-info</div>
  <div class="p-3 mb-2 bg-info-subtle text-info-emphasis">.bg-info-subtle</div>
  <div class="p-3 mb-2 bg-light text-dark">.bg-light</div>
  <div class="p-3 mb-2 bg-light-subtle text-light-emphasis">.bg-light-subtle</div>
  <div class="p-3 mb-2 bg-dark text-white">.bg-dark</div>
  <div class="p-3 mb-2 bg-dark-subtle text-dark-emphasis">.bg-dark-subtle</div>
  <div class="p-3 mb-2 bg-body-secondary">.bg-body-secondary</div>
  <div class="p-3 mb-2 bg-body-tertiary">.bg-body-tertiary</div>
  <div class="p-3 mb-2 bg-body text-body">.bg-body</div>
  <div class="p-3 mb-2 bg-black text-white">.bg-black</div>
  <div class="p-3 mb-2 bg-white text-dark">.bg-white</div>
  <div class="p-3 mb-2 bg-transparent text-body">.bg-transparent</div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
    crossorigin="anonymous"></script>
</body>

</html>

```

**실습 : 파란색 정사각형 만들기**

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <style>
    .box {
      width: 200px;
      height: 200px;
    }
  </style>
</head>

<body>
	<!-- class 내에서 설정함. 자세한 설정 방법은 공식 문서를 참고한다. -->
  <div class="box bg-info border border-black border-2"></div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
    crossorigin="anonymous"></script>
</body>

</html>

```

### Bootstrap Component

Bootstrap에서 제공하는 UI 요소

버튼, 네비게이션 바, 카드, 폼, 드롭다운 등 → `Alerts`, `Badges`, `Buttons`, `Cards`, `Navbar`…

일관된 디자인을 제공하여 웹 사이트의 구성 요소를 구축하는 데 유용하게 활용.

*Javascript가 웹페이지 동작을 결정짓는 코딩이다!*

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>
  <!-- alerts -->
  <div class="alert alert-primary" role="alert">
    A simple primary alert—check it out!
  </div>
  <div class="alert alert-secondary" role="alert">
    A simple secondary alert—check it out!
  </div>
  <div class="alert alert-success" role="alert">
    A simple success alert—check it out!
  </div>
  <div class="alert alert-danger" role="alert">
    A simple danger alert—check it out!
  </div>
  <div class="alert alert-warning" role="alert">
    A simple warning alert—check it out!
  </div>
  <div class="alert alert-info" role="alert">
    A simple info alert—check it out!
  </div>
  <div class="alert alert-light" role="alert">
    A simple light alert—check it out!
  </div>
  <div class="alert alert-dark" role="alert">
    A simple dark alert—check it out!
  </div>

  <!-- badges -->
  <h1>Example heading <span class="badge text-bg-secondary">New</span></h1>
  <button type="button" class="btn btn-primary">
    Notifications <span class="badge text-bg-secondary">4</span>
  </button>
  <button type="button" class="btn btn-primary position-relative">
    Inbox
    <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
      99+
      <span class="visually-hidden">unread messages</span>
    </span>
  </button>

  <!-- Buttons -->
  <button type="button" class="btn btn-primary">Primary</button>
  <button type="button" class="btn btn-secondary">Secondary</button>
  <button type="button" class="btn btn-success">Success</button>
  <button type="button" class="btn btn-danger">Danger</button>
  <button type="button" class="btn btn-warning">Warning</button>
  <button type="button" class="btn btn-info">Info</button>
  <button type="button" class="btn btn-light">Light</button>
  <button type="button" class="btn btn-dark">Dark</button>
  <button type="button" class="btn btn-link">Link</button>

  <!-- Cards(많이 쓰이는 요소!) -->
  <div class="card" style="width: 18rem;">
    <img src="..." class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">Card title</h5>
      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
      <a href="#" class="btn btn-primary">Go somewhere</a>
    </div>
  </div>

  <!-- navbar(제일 많이 쓰이는 요소! 크기에 따라 자동으로 모양 변화됨.) -->
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Dropdown
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" aria-disabled="true">Disabled</a>
          </li>
        </ul>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
    crossorigin="anonymous"></script>
</body>

</html>

```

그 외 `carousel`, `modal` 등의 요소도 있다.

`carousel`은 회전목마라는 뜻이며, 이미지를 보여줄 때 주로 사용된다.

`carousel`을 한 번에 2개를 쓸 때는 주의해야 된다.

Javascript 상으로 어떤 버튼으로 이미지를 넘길지 **정확히** 설정해 놓아야 한다.

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>
  <div class="container">
    <!-- 첫 번째 carousel -->
    <div id="carouselExample1" class="carousel slide">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="images/01.jpg" class="d-block w-100" alt="01.jpg">
        </div>
        <div class="carousel-item">
          <img src="images/02.jpg" class="d-block w-100" alt="02.jpg">
        </div>
        <div class="carousel-item">
          <img src="images/03.jpg" class="d-block w-100" alt="03.jpg">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample1" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExample1" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>

    <!-- 두 번재 carousel -->
    <div id="carouselExample2" class="carousel slide">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="images/04.jpg" class="d-block w-100" alt="01.jpg">
        </div>
        <div class="carousel-item">
          <img src="images/05.jpg" class="d-block w-100" alt="02.jpg">
        </div>
        <div class="carousel-item">
          <img src="images/06.jpg" class="d-block w-100" alt="03.jpg">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample2" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExample2" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>

  <!-- 첫 번째와 두 번째 carousel id값과 각 버튼의 data-bs-target 값을 따로 설정해야 개별로 작동한다 -->
  <!-- 다른 요소들도 마찬가지! -->

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
    crossorigin="anonymous"></script>
</body>

</html>

```

`modal` 도 마찬가지로 각자의 `id` 와 `data-bs-target` 이 일치해야 한다.

`modal` 은 id값으로 동작하기 때문에, 코드 정리가 용이해진다.

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>
  <!-- Button trigger modal 1 -->
  <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
    One
  </button>

  <!-- Button trigger modal 2 -->
  <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal2">
    Two
  </button>

  <!-- Modal 1 -->
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          One
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal 2 -->
  <div class="modal fade" id="exampleModal2" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          Two
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>

  <!-- modal도 마찬가지로 여러 개를 사용할 경우 각 id와 data-bs-target을 일치시켜주어야 한다. (따로 설정!) -->

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
    crossorigin="anonymous"></script>
</body>

</html>

```

`aria-….` *설정은 지금 당장 사용되지는 않지만, 나중에 웹 동작을 위해 남겨두는 것이 좋다!*

## Semantic Web

웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식

이 요소가 시각적으로 어떻게 보여질까? → 이 요소가 가진 목적과 역할은 무엇일까?

예를 들어, HTML 요소에서 보면

단순히 크게 설정한 글씨체와, 헤더를 사용한 큰 글씨와는 모양은 같지만, 의미가 다르다는 것이다.

### HTML Semantic Element

기본적인 모양과 기능 이외에 의미를 가지는 HTML 요소

검색엔진 및 개발자가 웹 페이지 콘텐츠를 이해하기 쉽도록 한 것

*ex)* `header` `nav` `main` `article` `section` `aside` `footer` …

CSS에도 이러한 요소가 존재한다. (CSS 방법론)

CSS를 효율적이고 유지 보수가 용이하게 작성하기 위한 일련의 가이드라인인 셈이다.

### OOCSS (Object Oriented CSS)

객제 지향적 접근법을 적용하여 CSS를 구성하는 방법론

기본 원칙으로는,

1. 구조와 스킨을 분리
2. 컨테이너와 콘텐츠를 분리

가 있다.

<aside>

1. **구조와 스킨 분리**
    
    구조와 스킨을 분리함으로써 재사용 가능성을 높인다.
    
    *ex)* 모든 버튼의 공통 구조를 정의하고, 각각의 스킨(배경색과 폰트 색상)을 정의한다.
    
2. **컨테이너와 콘텐츠 분리**
    
    객체에 직접 적용하는 대신 객체를 둘러싸는 컨테이너에 스타일을 적용한다.
    
    스타일을 정의할 때 위치에 의존적인 스타일을 사용하지 않도록 한다.
    
    콘텐츠를 다른 컨테이너로 이동시키거나 재배치할 때 스타일이 깨지는 것을 방지한다.
    
    *ex)*
    
    `.container`과 `.title`은 폰트 크기 담당 (콘텐츠 스타일)
    
    `.header`와 `.footer`는 폰트 색 담당 (컨테이너 스타일)
    
</aside>

## 참고

### Bootstrap을 사용하는 이유

가장 많이 사용되는 CSS 프레임워크이다.

사전에 디자인된 다양한 컴포넌트 및 기능이 있으며, 손쉬운 반응형 웹 디자인 구현이 가능하다.

커스터마이징이 용이하며, 모든 주요 브라우저에서 작동하도록 설계되어 있다.

*Bootstrap은 CDN을 사용하지 않고, 파일을 다운 받아 사용도 가능하다!*

### HTML과 CSS의 역할

HTML은 콘텐츠의 구조와 의미를 담당하며,

CSS는 레이아웃과 디자인을 담당한다.

→ 의미론적인 마크업이 필요한 것이다! (검색엔진 최적화(SEO), 웹 접근성(Web Accessibility))

## 실습

### Breakpoints

창 크기를 조절하면 그에 따라 padding, margin 값을 조정할 수 있다.

`{properties}{sides}-{breakpoint}-{size}` 

| breakpoints | **범위** |
| --- | --- |
| `sm`  | ≥ 576px |
| `md` | ≥ 768px |
| `lg` | ≥ 992px |
| `xl` | ≥ 1200px |
| `xxl` | ≥ 1400px |