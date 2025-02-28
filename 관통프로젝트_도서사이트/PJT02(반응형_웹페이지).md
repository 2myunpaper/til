## 프로젝트 목표

나만의 사이트 구현하기, 반응형으로 만들기

웹은 알고리즘 학습과 다르게 정답이 없고, 암기가 힘들다.

→ 다양한 방법으로 구현해볼 수 있도록 노력해야 한다!

프로젝트를 들어가기 전에, 개발자 포트폴리오 사이트를 만들면서 사이트를 어떻게 만들어야 할지 파악해가자.

## 페이지 구조 만들기

### 전체 구조 만들기

포트폴리오 사이트에는 여러가지 내용이 포함되어 있다고 가정하자.

→ *메뉴, 메인 콘텐츠, 자기소개, 나의 기술 스택 소개, 진행한 프로젝트, 연락처 남기기, 꼬리말 등…*

그럼 아래와 같이 작성해볼 수 있겠다. → 생각했던 공간을 만든다.

- **참고 : Emmet, 들여쓰기 자동 완성**
    
    Visual Code는 자동완성을 지원한다.
    
     `div * 7` 을 입력하면 `div` 태그 7개 자동 생성된다.
    
    `div > (div + p)` 을 입력하면 `div`안에 `div`, `p`가 있는 태그들이 자동 생성된다.
    
    `alt + shift + F` 는 띄어쓰기, 들여쓰기 등을 자동 설정해준다.
    

그런데 `div` 태그들만 사용해서 구성하면 안될까? → 가독성이 떨어지고, 중요도 구분이 되지 않는다.

의미 있는 태그(시맨틱 태그)를 적절히 활용하여 영역을 구분해보자.

| **태그** | **설명** |
| --- | --- |
| `<header>` | 문서의 머리말. 제목이나 로고 등의 정보를 포함. |
| `<nav>`  | 페이지 메뉴를 만들 때 사용 |
| `<main>` | 주요 콘텐츠를 나타냄 |
| `<section>` | 주제 별로 문서의 콘텐츠 영역을 구성하는 요소 |
| `<article>` | 개별 콘텐츠를 나타내는 요소. 뉴스 기사, 포스트 등의 내용을 포함. |
| `<footer>`  | 문서의 꼬리말. 저작권 정보, 연락처 등을 포함함 |

```html
  <!-- [참고] Emmet 자동 완성 기능 찾아보기 -->
  <!-- 네비게이션 -->
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">포트폴리오</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
          <!-- me-auto : 오른쪽에 남는 공간 다 주자! -->
          <!-- ms-auto : 왼쪽에 남는 공간 다 주자! -->
          <li class="nav-item">
            <a class="nav-link" href="#">헤더</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">자기소개</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">기술스택</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">프로젝트</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">연락처</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <!-- 헤더 -->
  <header>헤더</header>
  <!-- 자기소개 -->
  <section>자기소개</section>
  <!-- 기술 스택 -->
  <section>기술 스택</section>
  <!-- 프로젝트 -->
  <section>프로젝트</section>
  <!-- 연락처 -->
  <section>연락처</section>
  <!-- 꼬리말 -->
  <footer>꼬리말</footer>
```

※ **SEO (Search Engine Optimization)** : 자신들이 만든 정보를 사람들이 쉽게 찾을 수 있게 하는 것

*SEO 점수를 매기는 사이트도 존재한다. 쇼핑몰 같은 경우, 유료 버전을 이용해서 SEO를 검사하기도 한단다.*

그 외에 디자인 요소는 Bootstrap을 이용한다. Bootstrap은 CSS 프레임워크이다.

*프레임워크라 하면, 쉽게 말해 남의 코드를 가져온다고 생각하면 된다.*

이것을 사용할 방법은 1. 직접 다운로드 2. CDN 이 있다.

CDN을 이용해서 구현해보자.

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>
```

각 구간들을 모두 높이 300px로 맞추고 싶다. 어떻게 할까?

`<style>` 태그에 높이를 설정해주면 될 것이다.

```html
<style>
    .header,
    .intro,
    .skills,
    .projects,
    .contact {
      height: 300px;
    }
</style>
```

참고로 `<style>` 설정할 때, 이미 존재하는 태그를 선언하는 것은 권장하지 않는다.

새로 클래스를 만들어 선언하는 것이 좋다!

### 구글 폰트 추가하기

사이트의 폰트를 적용하고 싶다면, embedded를 통해 가져올 수 있다.

아래는 “Dongle”이라는 폰트를 가져와 코드로 사용한 예이다.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Dongle&display=swap" rel="stylesheet">
  <style>
    * {
      font-family: "Dongle", sans-serif;
			/* "Dongle" 이라는 폰트가 없을 경우, sans-serif로 대체함. */
      font-weight: 400;
      font-style: normal;
    }
  </style>
```

### 반응형 레이아웃 구성하기

반응형 레이아웃을 구성하는 방법은 아래와 같다.

1. **`flex` 정렬**
    
    가장 기본적인 반응형 레이아웃 구현
    
    그러나, 내 마음대로 비율을 조정하기 힘듦.
    
2. **`grid` (내부적으로 `flex` 로 구현되어 있음.)**
    
    가로 한 줄을 12칸으로 나눔. → `row`
    
    각 요소들이 원하는 만큼 가져가자 → `col-N` 
    
    정해진 픽셀에서 원하는 크기를 재설정 → `breakpoint (xs, sm, md, lg, xl, xxl)` 
    
    `col-{breakpoint}-{N}` 
    
    `grid` 를 이용하여 Intro, skills, projects, contact 부분을 조건에 맞게 배치해보자.
    
    ```html
    <main class="row">
        <!-- 자기소개 -->
        <section class="intro col-12 col-sm-6 col-md-4 col-lg-3">자기소개</section>
        <!-- 기술 스택 -->
        <section class="skills col-12 col-sm-6 col-md-4 col-lg-3">기술 스택</section>
        <!-- 프로젝트 -->
        <section class="projects col-12 col-sm-6 col-md-4 col-lg-3">프로젝트</section>
        <!-- 연락처 -->
        <section class="contact col-12 col-sm-6 col-md-4 col-lg-3">연락처</section>
      </main>
    ```
    
3. **추가적인 반응형 CSS**
    
    breakpoint 외의 작업은 어떻게 할까? → 미디어 쿼리 ( `@media` ) 를 이용한다.
    
    ```html
    <style>
      /* @media 미디어타입 and (조건) */
      /* 가로가 500px 이상일 때 헤더의 배경색을 빨간색으로 */
      /* min-width: 조건 이상일 때 적용 */
      /* max-width: 조건 이하일 때 적용 */
      /* orientation: 화면의 가로 세로 여부 (핸드폰에서 주로 이용될 수 있음.) */
    								  /* portrait(세로), landscape(가로) */
      @media screen and (min-width: 500px) {
        .header {
          background-color: crimson;
          /* transition: 변할 때 부드럽게 전환 */
          transition: background-color 2s ease;
        }
      }
    </style>
    ```
    

### 이미지 반응형으로 만들기

이미지는 본인이 사이즈를 가지고 있으므로 기본적으로 반응형이 되지 않는다. 

`img-fluid` : 이미지를 반응형에 맞게 바꿔주는 class

```html
<img src="assets/ai_recommendation/img1.jpeg" class="img-fluid">
```