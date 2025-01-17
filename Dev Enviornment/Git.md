<aside>

**git** : 분산 버전 관리 시스템

</aside>

Google docs에서 버전 기록 하는 것과 같은 원리.

## 버전 관리가 무엇인가?

우리는 사실 버전 관리를 하고 있다.

*최종, 진짜_최종, 진짜진짜_최종 …*

그러나 이런 방법은 용량 등의 문제가 발생할 수 있다.

그러면 **변경 사항** 만을 저장할 수 있다면? → 효율적으로 버전을 관리할 수 있을 것이다.

Git은 개발 과정에서 발생하는 이와 같은 원리로 효율적으로 개발 과정을 이끌 수 있다. (용량 관리도 용이함.)

## 중앙 집중식 vs 분산식

위키피디아 페이지는 여러 개를 보여주는가? → 아니다.

위키피디아는 중앙 관리식으로, 모든 버전들은 서버에 저장이 되어, 사용자에게 하나의 버전만 보여준다.

<aside>

**중앙 집중식**

버전은 중앙 서버에 저장되고 중앙 서버에서 파일을 가져와 다시 중앙에 업로드

→ 중앙에서 받고 수정하고 다시 알려주는 구조

</aside>

<aside>

**분산식**

버전을 여러 개의 복제된 저장소에 저장 및 관리

→ 나도 가지고 있고 수정하면 중앙에 알려주는 구조

</aside>

분산 구조에서의 장점은,

**중앙 서버에 의존하지 않고 동시에 다양한 작업을 수행**할 수 있다는 것이다. **개발자들 간의 작업 충돌을 줄여주고 개발 생산성을 향상**시킨다.

중앙 서버의 장애나 손실에 대비하여 **백업과 복구가 용이**하다.

인터넷 연결이 없어도 작업을 계속할 수 있다.

그러므로, Git은 **코드 분산 관리 시스템**이며,

**코드의 변경 이력을 기록하고 협업을 원활하게 하는 도구**이다!

## git의 영역

<aside>

**Working Directory**

실제 작업 중인 파일들이 위치하는 영역

→ 그냥 파일들, 아직 기록되지 않은 파일들

</aside>

<aside>

**Staging Area**

Working Directory 에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역

→ 추가될 파일들

</aside>

<aside>

**Repository**

버전 이력과 파일들이 영구적으로 저장되는 영역 모든 버전과 변경 이력이 기록됨.

→ 버전에 추가된 파일들

</aside>

Working Directory는 우리가 폴더에서 그냥 파일을 생성하는 것과 같다. 물리적으로 존재하지만, project에는 포함이 되어있지 않은 상태.

Staging Area는 Working Directory의 일부분을 프로젝트에 포함할거야! 하는 추가될 파일들이다.

*ex) 1 ~ 10 Working Directory에서 6 ~ 10을 추가할거야! → 6 ~ 10은 Staging Area*

Repository에는 최종적으로 포함된 파일들을 의미함.

그럼 굴러가는 방향이 Working Directory → Staging Area → Respository → Working Directory…

<aside>

**Commit (= 기여하다)**

변경된 파일들을 저장하는 행위이며, 마치 사진을 찍듯이 기록한다 하여 ‘snapshot’ 이라고도 함.

</aside>

git은 로컬 저장소 내 **모든 파일의 ‘변경사항’**을 감시하고 있다.

git을 init한 폴더에서,

그 안에 폴더를 만들어 그 폴더를 다시 init을 하는 것은 권장하지 않는다.

## Remote Respository

---

<aside>

**원격 저장소**

코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간

*ex) GitLab, GitHub, Bitbucket*

</aside>

### GitHub

※ 2020년 이후로 GitHub의 주 Branch는 master가 아니라 main으로 바뀌었다. *노예를 연상시킨대나 뭐래나..*

<aside>

**Push** : 현재 위치에 있는 모든 파일을 GitHub Repository에 add 하는 것

</aside>

**commit 이력이 없다면 push 할 수 없다!**

**원격 저장소에는 commit이 올라가는 것**

remote 링크는 1개 이상 설정해줄 수 있다.

<aside>

**Pull** : GitHub Repository으로 부터 내용을 가져오는 것 (수정된 파일 등)

**Clone** : GitHub Repository으로 부터 전체 내용을 가져오는 것 (전체 다)

</aside>

### .gitignore

<aside>

**.gitignore** : git add, commit를 무시할 파일 목록들

</aside>

올리고 싶지 않은 파일이 있다? → add를 애초에 안하면 된다.

그러나 파일이 너무 많다면 어떡하지?

**.gitignore** 라는 파일을 생성한다. → git add를 하고 싶지 않은 파일명을 적어 놓는다.

하지만, **.gitignore** 도 파일이므로, push될 수 있음.

되도록 push를 하는 것을 권장함.

GitHub에서 새로 Repository를 만들 때도 **.gitignore**을 만드는 설정이 있음.

*ex) .gitignore을 python으로 설정하면, python에서 일반적으로 무시하는 파일명들을 입력해준다.*

관련 사이트도 있다.

[gitignore.io](https://www.toptal.com/developers/gitignore)

그리고,

**이미 git의 관리를 받은 이력이 있는 파일이나 디렉토리는 나중에 gitignore에 작성해도 적용되지 않음!** → 이 문제는 `git rm --cached` 로 해결 가능

그런데,

Dev1, Dev2가 있다고 생각해보자.

Dev1과 Dev2가 동시에 Clone을 해서 모든 파일을 받고,

각각 코드를 편집하여 각각 add, commit을 했다.

그리고 각자 push를 하려고 한다.

그러면 어떻게 될까?

만약 Dev1이 먼저 push를 했다면,

Dev2는 push를 못하고, Dev2가 어쩔 수 없이 pull을 한다면 파일 내용이 이상하게 바뀐다.

파일 내용에는 내가 고친 부분과, 이미 다른 사람이 push한 내용이 동시에 기록된다.

이게 바로 git에서의 **CONFLICT**이다.

이것을 보완하는 방법은, Dev2는 Dev1이 이미 Push한 내용을 합치고, 추가사항을 적어 내용을 합병시킨다. 그리고 add, commit, push를 하면 해결된다.

*그러므로! pull을 항상 하는 것이 좋을 것이다~*

참고로 **CONFLICT**는 push할 때만 발생하지 않고, 다른 경우도 있으니 경험으로 알아가보자!

### Revert

‘재설정’

**특정 commit을 없던 일로 처리하며 그 결과를 새로운 commit으로 추가**한다.

그러니 **단순히 지워버리는 개념은 아니다.**

여기에서도 **CONFLICT**가 발생할 수 있다.

예를 들어 한 파일을 1번째, 2번째, 3번째 과정을 통해 add, commit이 되었다.

만약 2번째 commit을 revert해버린다면, **CONFLICT가 발생**한다.

*그래서 강사님은 revert를 잘 사용안하신다고 한다 ㅎㅎ*

### Reset

‘없던 일로 하자’

**특정 commit으로 돌아가는 작업**, 과거로 돌리는 듯한 행위

<aside>

`--soft` : 삭제된 commit의 기록을 staging area에 남김

→ commit만 사라지고, add가 된 상태까지

`—-mixed` : 삭제된 commit의 기록을 working directory에 남김 (기본 옵션 값)

→ 파일은 그대로 유지, add가 되지 않은 상태까지

`--hard` : commit의 기록도 삭제, commit에 해당되는 수정사항도 다 reset.

→ 파일도 reset

</aside>

그런데, push가 된 commit을 reset하는 것은? → *비추!비추!*

## 명령어

git 명령어는 앞에 무조건 `git` 을 붙여줘야 함.

`git init` : 현재 경로를 git으로 인해 관리되고 있는 폴더로 초기화해줌. 로컬 저장소를 초기화한다.

`git status` : git에 관리되는 현재 저장소에 git 상황을 보여줌. (많이 사용될 예정)

`git add sample.txt` : ‘sample.txt’ 를 staging area에 추가함.

`git add sample.txt a.txt` : ‘sample.txt’, ‘a.txt’ 를 staging area에 추가함.

`git commit -m "First commit"` : “First commit” 이라는 메세지를 남기며 staging area에 있는 파일들을 commit 함. (repository로 이동) 

`git config **--global** [user.email](http://user.email) "dhk0420@naver.com"` , `git config **--global** [user.name](http://user.name) "2myunpaper"` : git global 사용자 설정

`git config **--local** [user.email](http://user.email) "dhk0420@naver.com"` , `git config **--local** [user.name](http://user.name) "2myunpaper"` : 각 repository마다 다른 config 설정

`git config --global -l` : git global 설정 정보 보기

`git log` : 지금까지 commit한 파일들의 log를 최근 순으로 나열한다.

`git log --oneline` : commit 목록 한 줄로 보기

※ 모든 파일을 `commit`했는데, 만약 수정해줘야 하는 파일이 생겼다. 혹은 새로 생긴 파일이 생겼다.

→ 이런 파일들도 다시 1. `add`  2. `commit`해주면 repository에 저장되는 것임.

`git commit --amend` : 바로 직전 생성한 commit 메시지 수정, commit 전체 수정

`git remote **add** origin *링크*` : 현재 디렉토리를 *링크*  디렉토리에 원격 연결할 수 있게 해줌. *링크는* origin(단지 명칭)으로 설정

`git remote **seturl** origin *링크*` : origin 로컬 저장소와 연결되는 링크를 재설정 함.

`git push origin master` : origin 링크에 master branch로 push 한다.

`git push -u origin master` : origin 링크와 master branch를 기본 경로 (`-u`)로 설정하여 push한다.

`git pull origin master` : origin 링크에 master branch에 있는 내용을 끌어온다.

`git clone *링크*` : 원격 git에 있는 모든 파일들을 복사해서 붙여넣는다. clone으로 받은 프로젝트는 이미 git init이 되어 있음.

`git remote -v` : 현재 로컬 저장소에 등록된 원격 저장소 목록 보기

`git remote rm *원격_저장소_이름(ex. origin)*` : 현재 로컬 저장소에 등록된 원격 저장소 삭제

`git revert *commit_ID(구분할 수 있을 정도만)*` : revert 명령어

`git revert **--no-edit** *commit_ID*` : edit 없이 revert 실행

`git reset [옵션] *commit_ID*` : reset 명령어, [옵션]이 추가됨. (`--soft` , `--mixed` , `--hard`)

## 참고

<aside>

**로컬 (local)**

현재 사용자가 직접 접속하고 있는 기기 또는 시스템

개인 컴퓨터, 노트북, 태블릿 등 사용자가 직접 조작하는 환경

</aside>

Git은 꾸준히 써봐야 해결 방법을 찾아갈 수 있다. 실전으로 경험해보자.

그리고 git status를 잘 살피고, 검색해서 필요한 명령문을 찾으면 된다!
