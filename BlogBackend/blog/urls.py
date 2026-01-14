from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import EssayView, RegisterView
from . import views

urlpatterns = [
    path('essay/', EssayView.as_view(), name='essay-list'),
    # 用户认证相关
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    # token刷新
    path('token/refresh', TokenRefreshView.as_view(), name="token_refresh"),
    # 用户信息（支持GET和PUT） 
    path('user/info/', views.UserInfoView.as_view(), name="user_info")
]
