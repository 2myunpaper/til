최신 기술인 CSS Flexbox를 주의깊게 보자.

웹페이지는 박스로 구성되어 있다고 말할 수 있다.

원으로 보이는 것들은 모두 박스를 깎은 것이다.

박스 타입은 **Block box, Inline box** 가 있다.

박스 타입에 따라 페이지에서의 배치 흐름 및 다른 박스와 관련하여 박스가 동작하는 방식이 달라진다.

박스 표시 (Display) 타입은 **Outer display type, Inner display type** 이 있다.

<aside>

### **Outer display type**

박스가 문서 흐름에서 어떻게 동작할지를 결정

- **block 특징**
    
    항상 새로운 행으로 나뉨
    
    `width` 와 `height` 속성 사용 가능
    
    `padding` , `margin` , `border` 로 인해 다른 요소를 상자로부터 밀어냄
    
    `width` 속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 차지함
    
    대표적인 block 타입 태그 → `h1~6` , `p` , `div` 
    
- **inline 특징**
    
    새로운 행으로 넘어가지 않음
    
    `width` 와 `height` 속성을 사용할 수가 없음
    
    수직 방향 : `padding` , `margin` , `border` 가 적용되지만 다른 요소를 밀어낼 수는 없음
    
    수평 방향 : `padding` , `magins` , `borders` 가 적용되어 다른 요소를 밀어낼 수 있음
    
    대표적인 inline 타입 태그 → `a` , `img` , `span` , `strong` , `em` 
    
</aside>

### Normal flow

일반적인 흐름 또는 레이아웃을 변경하지 않은 경우 웹 페이지 요소가 배치되는 방식

가로는 Inline Direction, 세로는 Block Direction 이라고 함.

이번에 배울 것은, **Inner display type**에 관한 것이다.

<aside>

### Inner display type

박스 내부의 요소들이 어떻게 배치될 지를 결정

속성 : `flex` 

</aside>

## CSS Box Model

웹 페이지의 모든 HTML 요소를 감싸는 사각형 상자 모델

내용(content), 안쪽 여백(padding), 테두리(border), 외부 간격(margin)으로 구성되어 요소의 크기과 배치를 결정한다.

바깥부터 Margin - Border - Padding - Content 순으로 감싸져 있다.

<aside>

**Content box**

실제 콘텐츠가 표시되는 영역 크기

`width` 및 `height` 속성을 사용하여 크기 조정

</aside>

<aside>

**Padding box**

콘텐츠 주위에 공백

`padding` 관련 속성을 사용하여 크기 조정

</aside>

<aside>

**Border box**

콘텐츠와 패딩을 래핑

`border` 관련 속성을 사용하여 크기 조정

</aside>

<aside>

**Margin box**

콘텐츠, 패팅 및 테두리를 래핑

박스와 다른 요소 사이의 공백

`margin` 관련 속성을 사용하여 크기 조정

### shorthand 속성

- `border`
    
    `border-width` , `border-style` , `border-color` 를 한번에 설정하기 위한 속성
    
- `margin` , `padding`
    
    4방향의 속성을 각각 지정하지 않고 한번에 지정할 수 있는 속성
    
    4개 - 상우하좌
    
    3개 - 상/좌우/하
    
    2개 - 상하/좌우
    
    1개 - 공통
    
</aside>

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .box1 {
      width: 200px;
      padding-left: 25px;
      padding-bottom: 25px;
      margin-left: 25px;
      margin-top: 50px;
      border-width: 3px;
      border-style: solid;
      border-color: black;
    }

    .box2 {
      width: 200px;
      border: 1px dashed black;
      margin: 25px auto;
      padding: 25px 50px;

    }
  </style>
</head>

<body>
  <div class="box1">box1</div>
  <div class="box2">box2</div>
</body>

</html>
```

### box-sizing 속성

**표준 상자 모델(The standard CSS box model) - 기본값**에서 `width` 와 `height` 속성 값을 설정하면 이 값은 content box의 크기를 조정하게 된다.

실제 박스 크기는 content box의 `width` 와 `height` 가 아닌 테두리, 패딩 값을 모두 더해야 한다.

**대체 상자 모델(The alternative CSS box model)**에서 모든 `width` 와 `height` 는 실제 상자의 너비이다.

실제 박스 크기를 정하기 위해 테두리와 패딩을 조정할 필요가 없다.

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .box {
      width: 100px;
      border: 2px solid black;
      padding: 10px;
      margin: 20px;
      background-color: yellow;
    }

    .content-box {
      box-sizing: content-box;
      /* box-sizing을 content-box 기준으로, */
    }

    .border-box {
      box-sizing: border-box;
      /* box-sizing을 border-box 기준으로, */
    }
  </style>
</head>

<body>
  <div class="box content-box">content-box</div>
  <div class="box border-box">border-box</div>
</body>

</html>
```

### 기타 display 속성

<aside>

`inline-block`

`inline` 과 `block` 요소 사이의 중간 지점을 제공하는 display 값

`width` 및 `height` 속성 사용 가능

`padding` , `margin` 및 `border` 로 인해 다른 요소가 상자에서 밀려남

새로운 행으로 넘어가지 않음

→ 요소가 줄 바꿈 되는 것을 원하지 않으면서 너비와 높이를 적용하고 싶은 경우에 사용

</aside>

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">

  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    span {
      margin: 20px;
      padding: 20px;
      width: 80px;
      height: 50px;
      background-color: lightblue;
      border: 2px solid blue;
      display: inline-block;
    }

    ul>li {
      background-color: crimson;
      padding: 10px 20px;
      display: inline-block;
    }

    .container {
      text-align: center;
    }

    .box {
      width: 100px;
      height: 100px;
      background-color: #4CAF50;
      margin: 10px;
      display: inline-block;
    }
  </style>
</head>

<body>
  <!-- 1. 이제 다른 요소를 밀어낼 수 있는 span -->
  <p>Lorem ipsum dolor sit amet <span>consectetur</span> adipisicing elit. Animi iusto enim officia exercitationem
    dolorque, quasi velit, dolores, tempora illum odio necessitatibus. Fugit,
    cumque eligendi!</p>

  <!-- 2. 리스트 요소를 가로로 정렬 -->
  <ul>
    <li><a href="#">link</a></li>
    <li><a href="#">link</a></li>
    <li><a href="#">link</a></li>
  </ul>

  <!-- 3. div 요소를 가로로 정렬 -->
  <div class="container">
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
  </div>
</body>

</html>

```

<aside>

`none`

요소를 화면에 표시하지 않고, 공간조차 부여되지 않음

→ 나중에 javascript를 이용해서 애니메이션 등을 적용해볼 수 있겠다!

</aside>

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .box {
      width: 100px;
      height: 100px;
      background-color: red;
      border: 2px solid black;
    }

    .none {
      display: none;
    }
  </style>
</head>

<body>
  <div class="box"></div>
  <div class="box"></div>
  <div class="box"></div>
</body>

</html>
```

## CSS Position

각 요소의 위치와 크기를 조정하여 웹 페이지의 디자인을 결정하는 것

`Position` , `Flexbox` 등

요소를 Normal Flow에서 제거하여 다른 위치로 배치하는 것

웹 페이지는 가로(Inline)과 세로(Block) 순으로 읽는다.

이번에 배우는 것을 이것을 무시하고, 다른 요소 위에 올리기, 화면의 특정 위치에 고정시키기 등을 적용해볼 것이다.

Position의 이동 방향은 Z축 방향을 조정한다고 보면 된다.

### Position 유형

`static` , `relative` , `absolute` , `fixed` , `sticky` 

<aside>

`static`

요소를 Normal Flow에 따라 배치

top, right, bottom, left  속성이 적용되지 않음

기본 값

</aside>

<aside>

`relative`

요소를 Normal Flow에 따라 배치

자신의 원래 위치(static) 기준으로 이동

top, right, bottom, left 속성으로 위치를 조정

다른 요소의 레이아웃에 영향을 주지 않음 (요소가 차지하는 공간은 static일 때와 같음)

</aside>

<aside>

`absolute`

요소를 Normal Flow에서 제거

가장 가까운 `relative` 부모 요소를 기준으로 이동

→ 만족하는 부모 요소가 없다면 body 태그를 기준으로 함

top, right, bottom, left 속성으로 위치를 조정

문서에서 요소가 차지하는 공간이 없어짐.

</aside>

<aside>

`fixed`

요소를 Normal Flow에서 제거

현재 화면영역(viewport)을 기준으로 이동

스크롤해도 항상 같은 위치에 유지됨

top, right, bottom, left 속성으로 위치를 조정

문서에서 요소가 차지하는 공간이 없어짐

</aside>

<aside>

`sticky`

`relative` 와 `fixed` 의 특성을 결합한 속성

스크롤 위치가 임계점에 도달하기 전에는 `relative` 처럼 동작

스크롤이 특정 임계점에 도달하면 `fixed` 처럼 동작하여 화면에 고정됨

만약 다음 `sticky` 요소가 나오면 다음 `sticky` 요소가 이전 `sticky` 요소의 자리를 대체

→ 이전 `sticky` 요소가 고정되어 있던 위치와 다음 `sticky` 요소가 고정되어야 할 위치가 겹치게 되기 때문

</aside>

```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
	  /* static, relative, absolute, fixed 예제 */
    * {
      box-sizing: border-box;
    }

    body {
      height: 1500px;
    }

    .container {
      position: relative;
      height: 300px;
      width: 300px;
      border: 1px solid black;
      left: 100px;
    }

    .box {
      height: 100px;
      width: 100px;
      border: 1px solid black;
    }

    .static {
      position: static;
      background-color: lightcoral;
    }

    .absolute {
      position: absolute;
      /* 본인의 영역을 버린다. 집 나간 아이 */
      background-color: lightgreen;
      top: 100px;
      left: 100px;
    }

    .relative {
      position: relative;
      /* 본인의 static 위치의 상대값 */
      background-color: lightblue;
      top: 100px;
      left: 100px;
    }

    .fixed {
      position: fixed;
      /* 사용자가 웹사이트 크기를 조정해도 고정됨 */
      background-color: gray;
      top: 0;
      right: 0;
    }
  </style>
</head>

<body>
  <div class="container">
    <div class="box static">Static</div>
    <div class="box absolute">Absolute</div>
    <div class="box relative">Relative</div>
    <div class="box fixed">Fixed</div>
  </div>
</body>

</html>
```

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
	  /* sticky 예제 */
    body {
      height: 1500px;
    }

    .sticky {
      position: sticky;
      top: 0;
      background-color: lightblue;
      padding: 20px;
      border: 2px solid black;
    }
  </style>
</head>

<body>
  <h1>Sticky positioning</h1>
  <div>
    <div class="sticky">첫 번째 Sticky</div>
    <div>
      <p>내용1</p>
      <p>내용2</p>
      <p>내용3</p>
    </div>
    <div class="sticky">두 번째 Sticky</div>
    <div>
      <p>내용4</p>
      <p>내용5</p>
      <p>내용6</p>
    </div>
    <div class="sticky">세 번째 Sticky</div>
    <div>
      <p>내용7</p>
      <p>내용8</p>
      <p>내용9</p>
    </div>
  </div>
</body>

</html>
```

### z-index

요소의 쌓임 순서(stack order)를 정의하는 속성. 정수 값을 사용해 Z축 순서를 지정

값이 클수록 요소가 위에 쌓이게 됨. `static`이 아닌 요소에만 적용됨

기본 값은 auto. 부모 요소의 z-index 값에 영향을 받는다.

같은 부모 내에서만 z-index 값을 비교함. 부모의 z-index가 낮으면 자식의 z-index가 아무리 높아도 부모보다 위로 올라갈 수 없음

z-index 값이 같으면 HTML 문서 순서대로 쌓임.

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .container {
      position: relative;
    }

    .box {
      position: absolute;
      width: 100px;
      height: 100px;
    }

    .red {
      background-color: red;
      top: 50px;
      left: 50px;
      z-index: 3;
    }

    .green {
      background-color: green;
      top: 100px;
      left: 100px;
      z-index: 2;
    }

    .blue {
      background-color: blue;
      top: 150px;
      left: 150px;
      z-index: 1;
    }
  </style>
</head>

<body>
  <div class="container">
    <div class="box red">z-index: 3</div>
    <div class="box green">z-index: 2</div>
    <div class="box blue">z-index: 1</div>
  </div>
</body>

</html>
```

### Position의 목적

전체 페이지에 대한 레이아웃을 구성하는 것보다는 **페이지 특정 항목의 위치를 조정**하는 것

## CSS Flexbox

**Inner display type,** 박스 내부의 요소들이 어떻게 배치될 지를 결정한다.

요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식 → **공간 배열, 정렬**

### Flexbox 구성 요소

Flex Container, Flex Item, main axis(가로 - main start, end로 나뉨.), cross axis(세로 - cross start, end로 나뉨.)

<aside>

**main axis (주 축)**

flex item들이 배치되는 기본 축

main start에서 시작하여 main end 방향으로 배치 (기본 값)

</aside>

<aside>

**cross axis (교차 축)**

main axis에 수직인 축

cross start에서 시작하여 cross end 방향으로 배치 (기본 값)

</aside>

<aside>

**Flex Container**

`display: flex;` 혹은 `display: inline-flex;` 가 설정된 부모 요소

이 컨테이너의 1차 자식 요소들이 Flex Item이 됨

flexbox 속성 값들을 사용하여 자식 요소 Flex Item들을 배치하는 주체

**Flex Item**

Flex Container 내부에 레이아웃 되는 항목

</aside>

### Flexbox 속성

- **Flex Container 관련 속성**
    
    `display` , `flex-direction` , `flex-wrap` , `justify-content` , `align-items` , `align-content` 
    
- **Flex Item 관련 속성**
    
    `align-self` , `flex-grow` , `flex-basis` , `order` 
    
    ---
    
1. **Flex Container 지정 :** `display`
    
    flex item은 기본적으로 행(주 축의 기본값인 가로 방향)으로 나열
    
    flex item은 주 축의 시작 선에서 시작
    
    flex item은 교차 축의 크기를 채우기 위해 늘어남
    
    ---
    
2. `flex-direction` 
    
    flex item이 나열되는 방향을 지정
    
    `column` 으로 지정할 경우 주 축이 변경됨
    
    `-reverse` 로 지정하면 flex item 배치의 시작 선과 끝 선이 서로 바뀜
    
    ---
    
3. `flex-wrap`
    
    flex item 목록이 flex container의 한 행에 들어가지 않을 경우 다른 행에 배치할지 여부 설정
    
    ---
    
4. `justify-content`
    
    주 축을 따라 flex item과 주위에 공간을 분배
    
    `start` , `end` , `center` 로 설정할 수 있음.
    
    ---
    
5. `align-content`
    
    교차 축을 따라 flex item과 주위에 공간을 분배
    
    `flex-wrap` 이 `wrap` 또는 `wrap-reverse` 로 설정된 여러 행에만 적용됨.
    
    한 줄 짜리 행에는 효과 없음 (`flex-wrap` 이 `nowrap` 으로 설정된 경우)
    
    ---
    
6. `align-items` 
    
    교차 축을 따라 flex item 행을 정렬
    
    ---
    
7. `align-self` 
    
    교차 축을 따라 개별 flex item을 정렬
    
    ---
    
8. `flex-grow` 
    
    남는 행 여백을 비율에 따라 각 flex item에 분배
    
    아이템이 컨테이너 내에서 확장하는 비율을 지정함.
    
    `flex-grow` 의 반대는 `flex-shrink` 이다.
    
    `flex-grow` 의 숫자는 배율로 보면 안된다. → 남는 영역을 나누어, 개수를 준다고 생각하면 된다.
    
    *ex)* `flex-grow` 가 1 1 0 2 라면, 남는 영역을 4개로 나누어, 1칸 1칸 0칸 2칸으로 나누어 준다.
    
    아예 크기를 부여하는 방식도 존재한다.
    
    ---
    
9. `flex-basis` 
    
    flex item의 초기 크기 값을 지정
    
    `flex-basis` 와 `width` 값을 동시에 적용한 경우 `flex-basis` 가 우선이다.
    
    ---
    

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .container {
      height: 500px;
      border: 1px solid black;
      display: flex;
      /* flex-direction: row; */
      /* flex-direction: column; */
      /* flex-direction: row-reverse; */
      /* flex-direction: column-reverse; */

      /* flex-wrap: nowrap; */
      /* flex-wrap: wrap; */

      /* justify-content: flex-start; */
      /* justify-content: center; */
      /* justify-content: flex-end; */

      /* align-content: flex-start; */
      /* align-content: center; */
      /* align-content: flex-end; */

      /* align-items: flex-start; */
      /* align-items: center; */
      /* align-items: flex-end; */
    }

    .post {
      background-color: grey;
      border: 1px solid black;
      margin: 0.5rem;
      padding: 0.5rem;
    }

    .item1 {
      align-self: center;
    }

    .item2 {
      align-self: flex-end;
    }
  </style>
</head>

<body>
  <div class="container">
    <div class="post item1">
      <h2>Post Title 1</h2>
      <p>Post Content 1</p>
    </div>
    <div class="post item2">
      <h2>Post Title 2</h2>
      <p>Post Content 2</p>
    </div>
    <div class="post item3">
      <h2>Post Title 3</h2>
      <p>Post Content 3</p>
    </div>
    <div class="post item4">
      <h2>Post Title 4</h2>
      <p>Post Content 4</p>
    </div>
  </div>

</body>

</html>
```

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .container {
      display: flex;
      width: 100%;
    }

    .item {
      height: 100px;
      color: white;
      font-size: 3rem;
    }

    .item-1 {
      background-color: red;
      flex-basis: 300px;
    }

    .item-2 {
      background-color: green;
      flex-basis: 600px;
    }

    .item-3 {
      background-color: blue;
      flex-basis: 300px;
    }
    /* 창이 줄어들면 설정해둔 크기의 배율로 적용된다. */
  </style>
</head>

<body>
  <div class="container">
    <div class="item item-1">1</div>
    <div class="item item-2">2</div>
    <div class="item item-3">3</div>
  </div>
</body>

</html>
```

표로 정리하면 아래와 같다.

| **배치** | **공간분배** | **정렬** |
| --- | --- | --- |
| `flex-direction`
`flex-wrap`  | `justify-content`
`align-content`  | `align-items`
`align-self` |

`justify` *는 **주축**이고,* `align` *는 **교차축**이라고 알면 된다!*

※ `justify-items` 및 `justify-self`  속성이 없는 이유는 필요 없기 때문이다. `margin auto` 를 통해 정렬 및 배치가 가능하다.

### `flex-wrap` 응용

다양한 디바이스와 화면 크기에 자동으로 적응하여 콘텐츠를 최적으로 표시하는 웹 레이아웃 방식을 **반응형 레이아웃**이라고 한다.

`flex-wrap` , `flex-grow` , `flex-basis` 등을 모두 이용하여 반응형 레이아웃을 만들어 볼 수 있겠다.

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .card {
      width: 80%;
      border: 1px solid black;
      /* 1 */
      display: flex;
      /* 2 */
      flex-wrap: wrap;
    }

    img {
      width: 100%;
    }

    .thumbnail {
      /* 3 */
      flex-basis: 700px;
      /* 4 */
      flex-grow: 1
    }

    .content {
      /* 3 */
      flex-basis: 350px;
      /* 4 */
      flex-grow: 1
    }
  </style>
</head>

<body>
  <div class="card">
    <img class="thumbnail" src="images/sample.jpg" alt="sample">
    <div class="content">
      <h2>Heading</h2>
      <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis minus sed expedita ut nihil tempora
        neque autem odio eos, repudiandae blanditiis, molestiae consequatur. Adipisci illo dolor repellat alias
        maiores.
        Aut?</p>
    </div>
  </div>
</body>

</html>
```

## 참고

### 마진 상쇄 (Margin collapsing)

두 block 타입 요소의 margin top과 bottom이 만나 더 큰 margin으로 결합되는 현상

일관된 레이아웃을 위해 적용되는 것이다.

복잡한 레이아웃에서 요소 간 간격을 일관 되게 유지하고, 요소 간의 간격을 더 예측 가능하고 관리하기 쉽게 만들기 위해서 적용된다. → 일관성, 단순화

### Flexbox 속성 정리

`flex-direction`  |  `row` , `row-reverse` , `column` , `column-reverse`

`flex-wrap`  |  `wrap` , `nowrap` 

`justify-content`  |  `flex-start` , `flex-end` , `center` , `space-between` , `space-around` , `space-evenly` 

`align-content`  |  `flex-start` , `flex-end` , `center` , `space-between` , `space-around` , `space-evenly` 

`align-items`  |  `stretch` , `flex-start` , `flex-end` , `center`

`align-self`  |  `stretch` , `flex-start` , `flex-end` , `center`