# Django Study

참고한 블로그 및 github

[DarrenKwonDev 블로그(본인 블로그)](https://darrengwon.tistory.com/category/python%2C%20Selenium%2C%20Django/%F0%9F%94%AB%20Django)  
[멋쟁이사자처럼 Django 정리 github](https://github.com/LikeLionSCH/LikeLion_Django_Study_Summary)

## command

- 가상 환경 구성 및 실행 후 django 설치  
  python -m venv .venv  
  .\ .venv\Scripts\activate  
  python install django

- vscode에서 python interpreter를 설정한 가상환경으로 잡아주기  
  `ctrl + shift + P`  
  `Python: Select Interpreter` 선택  
  사용하고자 하는 가상 환경에서 마련한 인터프리터를 선택

- 프로젝트 생성 및 구동  
  django-admin startproject [이름]  
  [구성되는 파일의 역할](https://darrengwon.tistory.com/343?category=879979)

- 앱 만들기  
  python manage.py startapp [app 이름]  
  [구성되는 파일의 역할](https://darrengwon.tistory.com/343?category=879979)

- 실행  
  python manage.py runserver

- 어드민 유저 생성  
  python manage.py createsuperuser

- DB 마이그레이션(작성한 model 스키마를 DB에 적용 후 마이그레이션)  
  python manage.py makemigrations  
  python manage.py migrate

<br/>
<br/>

## tips

### app 관리

[app].apps.config를 project/settings.py에 추가

### url 패턴

project/urls.py에서 path를 추가하자.  
 해당 app의 views.py에 있는 특정 함수를 두번 쨰 인자로 지정하고
템플릿에서 쉽게 사용하기 위해 name을 지정합시다.
`urlpatterns = [path("admin/", admin.site.urls), path("", app_view.home, name="home")]`

### templates 일원화

각 app에서 templates 폴더 생성하기보다 templates는 일원화하자. 이를 위해서 project/setting.py에서 template의 DIRS를
`os.path.join(BASE_DIR, "templates")`로 수정하자

- model.py를 admin.py에 등록
  `admin.site.register(models.Blog)`  
  데코레이터를 활용하는 방법도 있음

- 가장 간단한 형태의 Queryset  
  단순히 model을 불러와서 objects로 Manager를 가져와
  적절한 메서드를 사용하면 된다.  
  모델 관계를 이용한 Queryset과 좀 더 자세한 Queryset 정보는 [여기로](https://darrengwon.tistory.com/352?category=879979)

```
from django.shortcuts import render
from . import models
def home(request):
    # 모델을 불러와 objects로 Manager 호출
    blogs = models.Blog.objects.all()
    return render(request, "home.html", {"blogs": blogs})
```

### 모델 클래스에 정의한 메서드와 속성은 queryset 객체들이 사용 가능

```
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    body = models.TextField()

    def summary(self):
        return self.body[:100]
```

위와 같은 모델이 있다면 쿼리셋 객체들은 title, pub_date, body 속성을 가지고 있으며 summary라는 메서드를 사용할 수 있게 된다. 이를 템플릿에서 사용하면 다음과 같다.

```
<div class="chunk">
  <div class="upperChunk">
    <h2 class="title">{{blog.title}}</h2>
    <h5 class="date">{{blog.pub_date}}</h5>
  </div>
  <div class="downChunk">{{blog.summary}}
    <a href={% url 'detail' blog.id %}> ...more </a>
  </div>
</div>
```

### [path converter](https://darrengwon.tistory.com/478)

여러 객체들을 다루는, 계층적인 url을 자동 생성할 때 유리  
`<type : 변수이름>` 꼴로 사용함.
공식 문서에 따르면 type으로 str, int, slug, uuid 가능함.
자세한 내용은 [공식 문서](https://docs.djangoproject.com/en/3.1/topics/http/urls/)

```
# project/url.py에 path converter 활용
path('blog/<int:blog_id>', blog.views.detail, name="detail")

# app/views.py에서 함수의 인자로 사용
from django.shortcuts import render, get_object_or_404

def detail(request, blog_id):
    blog_detail = get_object_or_404(models.Blog, pk=blog_id)

    return render(request, "detail.html", {"blog": blog_detail})
```

### static 파일 서빙하기

[공식문서](https://docs.djangoproject.com/en/3.1/howto/static-files/)

필요에 따라 각각의 Django App마다 App별 정적 파일을 담는 별도의 "static" 폴더를 둘 수도 있지만
관리를 편하기 하기 위해 최상위 경로에 static 폴더를 만들기로 함.

만약 App 별로 static 폴더를 만들어 관리하는 방법을 선택했다면
STATIC_ROOT를 지정한 후 python manage.py collectstatic 명령을 사용해야 한다.

1. project/settings.py에서 STATIC_URL, STATICFILES_DIRS 지정

```
# STATIC_URL : {% static '경로' %}가 '/static/경로' 로 바뀌게 됨
STATIC_URL = '/static/'

# STATICFILES_DIRS : static이 어디에 있는지 static 경로 지정.
# 우리는 최상위 경로에 static을 만들어 줬으므로 다음과 같이 작성
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

2. static 파일 사용

최상단에 static 로드

- {% load staticfiles %} and {% load admin_static %} were deprecated in Django 2.1, and removed in Django 3.0.

`{% load static %}`

사용  
`{% static 'STATIC_URL 이후의 경로' %}`

```
# 사용 예시
<img class="card-img-top" src="{% static 'Poster.png' %}" alt="" />
```

| static                                                                   | media                                            |
| ------------------------------------------------------------------------ | ------------------------------------------------ |
| 정적 파일은 어디에 뒀나요 `STATICFILES_DIRS`                             | x                                                |
| 정적 파일을 보려면 어느 경로로 `STATIC_URL`                              | 업로드한 이미지를 보려면 어느 경로로 `MEDIA_URL` |
| 어디로 모을지(static을 app 별로 분리해서 관리할 때만 사용) `STATIC_ROOT` | 어디로 모을지 `MEDIA_ROOT`                       |
