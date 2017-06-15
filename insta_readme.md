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
15. settings.py 에 ```#custom user
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
11. post view작성
  - templates폴더 루트 아래 생성
  - templates를 settings에 추가
  - TEMPLATE_DIR = os.path.join(BASE_DIR,'templates') // TEMPLATES = [TEMPLATE_DIR,] 까지 추가
  - config/urls.py에 include로 작성
  - 프로젝트 메인에 urls.py에 작성
  - url(r'^post/',include(views.post_list),
  - 메인에서 오는 주소를 받는 곳을 post app에 urls.py로 생성
```from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post_list),
]
```

  - post로 받은 주소를 post_list뷰어로 보내준다
  - views.post_list에서는 render가되어 post_list.html로 전달
12. admin.py에 설정
- ```from django.contrib import admin
from .models import Post
class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post,PostAdmin)
```

13. admin 생성 두가지 방법
   - ./manage createsuperuser로 생성
   - Auth_user_model 사용으로 db_shell에서 u = User.objects.create_user('name')
   - u.set_password('password insert')
14. 이미지파일을 업로드했을 때 설정을 하지 않은 기본일때는 루트 디렉토리에 저장이된다 이것을 방지하고자 루트 폴더에 media 폴더를 생성한다 .gitignore에 media가 추가가되어있어서 git했을때 저장이 되지않게 지정되어있다.
 - 이미지 파일 업로드를 media에 폴더로 저장이되는것을 확인
 - 하지만 아직 이미지 파일을 post에서 보는건 되지않는다
 - 이유는 어디를 참조를 해서 불러와야될지를 설정을 하지 않았기때문이다
 - 메인 admin.py에 media를 추가로 수정한다
 - urlpatterns = []+ static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
 - 왜 + 일까? 뒤에 리스트를추가하기위해서라고 함
 - static함수가 리스트로 리턴해준다
 - media_url로 접근했을때 media_root로 가게 해준다
 - 이미지파일을 모든 post에 다 넣어주고
 - 이미지를 html에서 확인
 - 이미지파일을 또 다시 관리를 해야된다 한파일에 데이타파일을 계속 업로드를 하게되면 용량이커져서 느려지게된다 
 - 그래서 생성하는 upload_to를 이용하여 지정하여준다
 - 루트 디렉토리(MEDIA_ROOT)아래에 지정한 이름으로 폴더를 없다면 만들고 있다면 그안에 파일을 저장하게된다
 - 