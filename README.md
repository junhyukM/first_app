# Django

1. 프로젝트 생성
```bash
django-admin startproject <project name>
```

2. 프로젝트 폴더 이동
```bash
cd <project name>
```

3. vscode 실행

4. 가상환경 설정
```bash
python -m venv venv
```

5. 가상환경 활성화
```bash
source venv/Scripts/activate
```

6. 가상환경 비활성화
```bash
deactivate
```

7. 가상환경 내부에 django 설치
```bash
pip install django
```

8. 서버 실행 확인 (종료 : 'Ctrl + c')
```bash
python manage.py runserver
```

9. 앱 생성
```bash
django-admin startapp firts_app
```

10. 앱 등록
- 'setting.py'의 'INSTALLED_APPS'에 등록

11. urls.py
- 이정표를 작성하고 거기서 어떤 동작을 할지 작성
```python
from first_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('index/', views.index),
```

12. views.py
파일 내에서 함수 정의
```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
```

13. template 폴더 생성

14. html 파일 생성 및 작성

