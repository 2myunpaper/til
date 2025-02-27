## Bootstrap Grid system

웹 페이지의 레이아웃을 조정하는 데 사용되는 **12개의 컬럼**으로 구성된 시스템

→ 왜 12개의 컬럼일까?

→ 약수가 많아서 칸 수를 적절하게 조절할 수 있기 때문

### Grid system 목적

반응형 디자인을 지원해 웹 페이지를 모바일, 테블릿, 데스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도움.

디바이스 종류나 화면 크기에 상관없이, 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술을 **반응형 웹 디자인(Responsive Web)**이라고 한다.

### Grid system 구조

- **기본 요소**
    
    **Container** : Column들을 담고 있는 공간
    
    **Column** : 실제 컨텐츠를 포함하는 부분
    
    **Gutter** : 컬럼과 컬럼 사이의 여백 영역 (상하좌우). **x축은 padding**, **y축은 margin**으로 여백 생성
    
    1개의 row안에 12개의 column 영역이 구성
    

**Basic**

```html
<h2 class="text-center">Basic</h2>
  <!-- bootstrap에서 container는 양 옆에 여백을 둔다. -->
  <div class="container">
    <div class="row">
      <div class="col">
        <div class="box">col</div>
      </div>
      <div class="col">
        <div class="box">col</div>
      </div>
      <div class="col">
        <div class="box">col</div>
      </div>
    </div>
    <!-- 위와 같은 "col" 방법은 추천하지 않음. 정확하게 명시해놓는 것이 좋다. -->

    <div class="row">
      <div class="col-4">
        <div class="box">col-4</div>
      </div>
      <div class="col-4">
        <div class="box">col-4</div>
      </div>
      <div class="col-4">
        <div class="box">col-4</div>
      </div>
    </div>
    
    <div class="row">
      <div class="col-2">
        <div class="box">col-2</div>
      </div>
      <div class="col-8">
        <div class="box">col-8</div>
      </div>
      <div class="col-2">
        <div class="box">col-2</div>
      </div>
    </div>
    <!-- 칼럼의 개수는 12개로 일정함. 넘어가면 다음 줄로 넘어가 버린다. -->
  </div>
```

**Nesting**

```
<h2 class="text-center">Nesting</h2>
  <div class="container">
    <div class="row">
      <div class="col-4 box">
        <div>col-4</div>
      </div>
      <div class="col-8 box">
        <div class="row">
          <div class="col-6">
            <div class="box">col-6</div>
          </div>
          <div class="col-6">
            <div class="box">col-6</div>
          </div>
          <div class="col-6">
            <div class="box">col-6</div>
          </div>
          <div class="col-6">
            <div class="box">col-6</div>
          </div>
        </div>
      </div>
    </div>
  </div>
```

**Offset**

```html
<h2 class="text-center">Offset</h2>
  <div class="container">
    <div class="row">
      <div class="col-4">
        <div class="box">col-4</div>
      </div>
      <div class="col-4 offset-4">
        <div class="box">col-4 offset-4</div>
      </div>
    </div>
    <div class="row">
      <div class="col-3 offset-3">
        <div class="box">col-3 offset-3</div>
      </div>
      <div class="col-3 offset-3">
        <div class="box">col-3 offset-3</div>
      </div>
    </div>
    <div class="row">
      <div class="col-6 offset-3">
        <div class="box">col-6 offset-3</div>
      </div>
    </div>
    <!-- 한 row에서는 col개수와 offset을 합하여 12가 넘지 않는다. -->
  </div>
```

**Gutters**

```html
<h2 class="text-center">Gutters(gx-0)</h2>
  <div class="container">
    <div class="row gx-0">
      <div class="col">
        <div class="box">col</div>
      </div>
      <div class="col">
        <div class="box">col</div>
      </div>
    </div>
  </div>

<h2 class="text-center">Gutters(gy-5)</h2>
  <div class="container">
    <div class="row gy-5">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <!-- margin은 column으로 설정 시 위쪽 margin으로 설정된다. -->
    </div>
  </div>

<h2 class="text-center">Gutters(g-5)</h2>
  <div class="container">
    <div class="row g-5">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
    <!-- g다음 x,y 둘 다 입력하지 않을 시엔 padding, margin 둘 다 적용된다. -->
  </div>
```

### 참고

`container-fluid` 라는 것도 있으니, 참고해보자!

## Grid system for responsive web

Bootstrap grid system에서는 12개 column과 6개 breakpoints를 사용하여 반응형 웹 디자인을 구현한다.

### Grid system breakpoints

웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점

화면 너비에 따라 6개의 분기점 제공 ( `xs`, `sm`, `md`, `lg`, `xl`, `xxl` )

각 breakpoints 마다 설정된 최대 너비 값 이상으로 화면이 커지면 grid system 동작이 변경됨

*ex)* `col-sm-4` → 창의 크기가 sm을 넘어가면, 4개의 column을 차지한다.

```html
<h2 class="text-center">Breakpoints</h2>
  <div class="container">
    <div class="row">
      <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-6 col-md-8 col-lg-3 col-xl-4">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-6 col-md-12 col-lg-3 d-xl-none">
      <!-- d-xl-none: xl가 넘어갈 때 표시하지 않는다. -->
        <div class="box">col</div>
      </div>
    </div>
  </div>
```

```html
<h2 class="text-center">Breakpoints + offset</h2>
  <div class="container">
    <div class="row g-4">
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 col-md-6 offset-sm-4 offset-md-0">
      <!-- offset sm만 설정하게 해주면, 그 크기 이상일 때 그 상태가 계속 유지하므로,
      breakpoints 마다의 설정을 해주어야 한다. -->
        <div class="box">col</div>
      </div>
    </div>
  </div>
```

*breakpoints는 전자 기기에 따라 정해졌다고 생각할 수도 있다!*

*bootstrap 파일을 보면, 주석으로 장치 크기에 따라 정해진 것을 확인해볼 수 있다.*

다시 정리하면,

**Grid System은 화면 크기에 따라 12개의 칸을 각 요소에 나누어 주는 것**

이라고 할 수 있다.

## CSS Layout 종합 정리

Grid System, Flexbox, Position …

CSS 레이아웃 기술들은 각각 고유한 특성과 장단점을 가지고 있다.

이들은 상호보완적이며, 특정 상황에 따라 적합한 도구가 달라진다.

최적의 기술을 선택하고 효과적으로 활용하기 위해서는 다양한 실제 개발 경험이 필수적일 것이다.

## UX & UI

### UX (User Experience)

제품이나 서비스를 사용하는 사람들이 느끼는 전체적인 경험과 만족도를 개선하고 최적화하기 위한 디자인과 개발 분야

*ex)* 백화점 1층에서 느껴지는 좋은 향수 향기, 러쉬 매장 근처만 가도 맡을 수 있는 러쉬 향기 등

사람들의 마음과 생각을 이해하고 정리해서 제품에 녹여내는 과정이며,

유저 리서치, 데이터 설계 및 정제, 유저 시나리오, 프로토타입 설계 등으로 구현해볼 수 있다.

### UI (User Interface)

서비스와 사용자 간의 상호작용을 가능하게 하는 디자인 요소들을 개발하고 구현하는 분야

*ex)* 리모컨, ATM, 웹 사이트 등

예쁜 디자인보다는 사용자가 더 쉽고 편리하게 사용할 수 있도록 고려하며,

이를 위해서는 디자인 시스템, 중간 산출물, 프로토타입 등이 필요하다.

### 직무 관련

UX - UX Researcher, User Researcher

UI - Product Designer, Interaction Designer

기업에서는 UX/UI 둘 다 통합해서 채용하는 경우가 많다.

UX와 UI를 둘 다 고려하는 것이 좋다!

## 참고

### The Grid System

CSS가 아닌 편집 디자인에서 나온 개념으로 구성 요소를 잘 배치해서 시각적으로 좋은 결과물을 만들기 위한 시스템.

기본적으로 안쪽에 있는 요소들의 오와 열을 맞추는 것에서 기인했으며,

정보 구조와 배열을 체계적으로 작성하여 정보의 질서를 부여한다.

### Grid cards

`rol-cols` 클래스를 사용하여 행당 표시할 열(카드) 수를 손쉽게 제어할 수 있다.

*카드 전용 Grid System이라고 이해하면 된다.*

```html
<body>
  <h2 class="text-center">Grid Cards</h2>
  <div class="container">
    <div class="row row-cols-1 row-cols-sm-3 row-cols-md-2 g-4">
    <!-- row-cols-(카드개수) -->
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content.</p>
          </div>
        </div>
      </div>
      <div class="col offset-sm-4 col offset-md-0">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
```

## 실습

### `img-fluid`

Bootstrap에서 이미지가 크기에 맞춰지는 클래스