# Git-bash

## CLI VS GUI
- CLI (commend line inter face) : 커맨드(명령어)를 통해 작동하는 인터페이스
- GUI(Graphic User Interface) : 그래픽 기반 인터페이스

## 명령어
 1. pwd(Print working difrectory) : 현재 위치 출력
 2. ls(list): 현재 폴더의 파일/ 폴더 출력
 3. cd(change directory) 
    - cd [경로명] :폴더변경 tab을 눌러 자동완성을 활용하자
    - cd .. : 상위 폴더 이동
    - cd ~ : 홈 폴더 이동

 4. mkdir(make directory)
    - mkdir [폴더명] : 폴더 생성
 5. rm(remove) 
    - rm [파일명] : 파일 삭제
    - rm -r [폴더명] : 폴더 삭제 / r : 리커시브
    - rm -rf [폴더명] : 강제 삭제. 깃폴더 삭제
 6. touch 
    - touch [파일명] : 파일 생성
 7. mv      
    - mv(move) : 파일/ 폴더명 변경
    - mv [파일/폴더명] [바꿀파일/폴더명]: 파일 또는 폴더를 이동
 8. cp
    - cp [파일명] [파일위치] :파일 복사
    - cp -r [폴더명] [위치] : 폴더를 복사
 9.  home directory  
        - ~ :  홈 디렉토리(git bash 처음 열면 나오는 기본폴더)
10. sudo : 관리자 권한으로 다음 명령어를 실행
11. git clone [깃허브코드주소] [폴더명]
    - 깃허브에 백업해놓은 것들을 해당 폴더에 복사
    - 디렉토리 상하위에 git프로젝트를 중복해서 설치하지 않도록 주의(Error)

<br>

## 절대 경로와 상대 경로의 차이
- 절대 경로의 시작은 루트 디렉토리(/)이다.
- 상대 경로의 시작은 현재 디렉토리(.)이다.  
  
<br>
   
## CLI 파일 편집기
- CLI에서 텍스트 에디터 nano, vim 등을 이용해 파일을 수정하고, 저장할 수 있다.
- nano는 기본적으로 다 설치되어있다. 프롬프트에 nano 를 입력하여 실행시킨다.


