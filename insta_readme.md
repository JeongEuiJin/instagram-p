##초기 설정
1. pyenv virtualenv 3.6.1 instagram-p-env
2. pyenv local instagram-p-env
3. pip install django
4. pip install django-extensions
5. pip install ipython
6. https://pillow.readthedocs.io/en/4.1.x/installation.html
 - brew는 한번 설치 해두면 root에 설치가되어 한번만 설치하면되고 pip install Pillow만 설치하면된다.
7. .gitignore 설치 /djang/(projectname)생성
8. django-admin startproject config
9. mv config django-app
10. config/settings.py -> language_code = 'ko-kr' , Time_zone = 'Asia/Seoul' 변경
11. installed_apps = 'django_extensions' 추가
12. 환경설정 -> project interpreter 설정 -> usr/local/var/pyenv/versions/instagram-p-env/python
13. ./manage.py startapp post로 생성
14. from django.contrib.auth.models import AbstractUser
15.settings.py 에 ```#custom user
AUTH_USER_MODEL = 'MEMBER.USER'```추가


##Post.models

1. User, Post, Comment, Tag
2. 사용자 인증 방법
 - 쿠키인증방식을 사용
 - 서버에서는 키값을 주어서 연결하는것을 좀더 빠르고 세션을 안끊고 계속 연결해둘수있다.
3. 장고에 내장된 User를 사용을 하고 ```from django.contrib.auth.models import User```을 사용한다
4. User생성시 password는 u.set_password('password')를 해야 해쉬로된패스워드가 저장
5. 나머지는 동일하게 u.first_name = 'eui-jin' 사용을 하면된다
6. ```Comment.objects.create(post=p1,author=u2,content='첫번째 댓글')```
7. ```p1.comment_set.create(author=u2,content='첫번째 댓글')```
8. get_or_create()
 - get으로 가져오는데 없다면 만들어서 가지고온다
9. 중간자 (m2m)에서 중간자 테이블을 만들고 적용시키는 방법
 - ManyToManyField에 through='적용시킬테이블명'
 - 중간자 테이블에 Meta 추가 , db_table=중간자로 생성된 DB에서의 테이블명과 같이 입력
 - 중간자 테이블에 장고에서 생성이된 것과 똑같이 만들어준다
 - makemigrations하고 migrate 할 때는 DB를 속이기위해서 --fake를 사용한다
10. AUTH_USER_MODEL을 settings.py에 생성을 해두어라 이미 진행된 migrations에서는 바꾸기가 힘들다
  - from django.conf import settings를 사용
  - User를 settings.AUTH_USER_MODEL로 외래키를 불러온다
  - 