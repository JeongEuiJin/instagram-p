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


##Post.models

1. User, Post, Comment, Tag
2. 