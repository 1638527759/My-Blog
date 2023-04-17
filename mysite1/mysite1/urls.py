"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.conf.urls import url, include
from django.urls import re_path as url,include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
# from blog.views import sign_in, sign_up, view_1
from blog.views import View_1, View_2, View_3, Test


urlpatterns = [
    # path('',)
    path('admin/', admin.site.urls),
    path('',View_1.as_view()),
    path('view2/',View_2.as_view()),
    path('view3/',View_3.as_view(),name = "person"),
    path('test/',Test.as_view()),
    url(r'mdeditor/', include('mdeditor.urls')),

    # 用户管理
    # path('info/list/',views.orm),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
