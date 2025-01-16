일반 텍스트로 문서를 작성하는 간단한 방법. 

주로 개발자들이 텍스트와 코드를 작성해 문서화하기 위해 사용

[Markdown 문법 참고 링크](https://www.markdownguide.org/basic-syntax/)

## **실습 코드**

### **Markdown 연습**

```markdown
# Markdown Practice

We are practicing markdown!!!

- Alex
- Brad
- Chad

라면 끓이는 법

- 물을 끓인다
- 스프를 넣는다
- 면을 넣는다

# Heading1 (제목)
## Heading2
### Heading3
#### Heading4
##### Heading5
###### Heading6

샵(우물 정)의 개수에 따라 더 작은 단위의 제목이 된다.

# 라면

## 준비물

## 과정

### 선택사항

그냥 쓰면 Paragraph (문단)

# 목록 (List)

## 순서가 없는 List

대시(-)로 쓴다

- 대파
- 양파
- 마늘
- 청양고추
  - 들여쓰기 할 수 있다
  - 페페론치노
- 다시 원래대로

## 순서가 있는 List

1, 2, 3... 등으로 쓴다

1. 물을 끓인다.
2. 스프를 넣는다.
   1. 물을 끓이기 전에 넣어도 좋다.
3. 면을 끓인다.

# Code Block

마크다운을 이용해 (소스)코드를 표현하는 방법들

**inline code block** : 문단 등의 내용 안에 일부분만 코드로 표현하는 방법: `git`, `python`, `vscode`
```

**code block** : 큰 영역에 코드를 작성하여 코드로 표현하는 방법
```
print("Hello World")
```

한 줄 이상 코드로 표현이 가능하다.
```
print("Hello World")

print("Hi World")
```

작성될 코드의 언어를 설정해 줄 수 있다.

Python의 경우 :
```python
print("Hello World")
```

Markdown의 경우:
```md
# Heading 1

Paragraph
```

### 링크(link)와 이미지(image)

[Google](https://www.google.com)

[Naver](https://www.naver.com)

[ ] 안에 있는 것이 표시되는 모습, ( ) 안에 있는 것이 링크 내용이다.

Python 트랙 공유 문서 [링크](https://abit.ly/pb-document)

이미지를 하고 싶을 땐 [ ] 앞에 ! 를 붙여준다.

![이미지](https://picsum.photos/200/300)

![들판](103-200x300.jpg)

같은 폴더 안에 있는 이미지이면, 파일 이름만 ( ) 안에 입력하면 된다.

---

구분선, 수평선, horizontal rule

---

---

---



### **자기소개 Markdown**

```markdown
# INTRODUCE

## 인적 사항

**이름** : 김동현

**MBTI** : 4항목 모두 50 : 50, 때마다 다름.

**출생연도** : 1998년

**전공** : 기계공학과

**사는 지역** : 경기도 화성시

**SSAFY Track** : Coding Track ; Python

**기술 스택**
- **Coding** : C, Java, Python
- **etc** : Photoshop, Illustrator, Premiere Pro, After Effects

## 특이 사항

### 1년간 목표

- SW역량테스트 A형 이상 합격
- 프로젝트 기획 및 구현 최소 3번
- 구체적 희망 직종 결정하기
- SQLD 등 데이터 관련 자격증 따기
- 어학 시험 최소 2번 응시하기

### 취미

- 악기 연주 (플룻) 및 오케스트라 활동
- 작곡, 영상 편집 및 크루 활동

### SNS
- **Youtube**

  [ELBs](https://www.youtube.com/@elbskim_pltt) 
  
  [PLTT_Crew](https://www.youtube.com/@plttcrew)

- **Instagram**

## VISION 문구
**"필요한 팀을 찾지 말고, 필요한 사람이 되자"**
```
