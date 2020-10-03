# Django Study

참고한 블로그 및 github

[DarrenKwonDev 블로그](https://darrengwon.tistory.com/category/python%2C%20Selenium%2C%20Django/%F0%9F%94%AB%20Django)  
[멋쟁이사자처럼 Django 정리 github](https://github.com/LikeLionSCH/LikeLion_Django_Study_Summary)

## command

- 가상 환경 구성 및 실행 후 django 설치  
  python -m venv .venv  
  .\ .venv\Scripts\activate  
  python install django

- 프로젝트 생성 및 구동  
  django-admin startproject [이름]

- 앱 만들기  
  python manage.py startapp [app 이름]

- 실행  
  python manage.py runserver

- 어드민 유저 생성  
  python manage.py createsuperuser

- DB 마이그레이션(작성한 model 스키마를 DB에 적용 후 마이그레이션)  
  python manage.py makemigrations  
  python manage.py migrate

<br/>

---

<br/>

## tips

- app 관리  
  [app].apps.config를 project/settings.py에 추가

- url 패턴  
  project/urls.py에서 path를 추가하자.  
  해당 app의 views.py에 있는 특정 함수를 두번 쨰 인자로 지정하고
  템플릿에서 쉽게 사용하기 위해 name을 지정합시다.
  `urlpatterns = [path("admin/", admin.site.urls), path("", app_view.home, name="home")]`

- templates 일원화  
  각 app에서 templates 폴더 생성하기보다 templates는 일원화하자. 이를 위해서 project/setting.py에서 template의 DIRS를
  `os.path.join(BASE_DIR, "templates")`로 수정하자

- model.py를 admin.py에 등록
  `admin.site.register(models.Blog)`  
  데코레이터를 활용하는 방법도 있음

- 가장 간단한 형태의 Queryset  
  단순히 model을 불러와서 objects로 Manager를 가져와
  적절한 메서드를 사용하면 된다.

```
from django.shortcuts import render
from . import models
def home(request):
    blogs = models.Blog.objects.all()
    return render(request, "home.html", {"blogs": blogs})
```
