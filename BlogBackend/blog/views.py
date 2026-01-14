from django.shortcuts import render

# Create your views here.
# views.py
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from blog.models import Essay, UserInfo
from django.db import transaction
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserInfoSerializer
import json


@method_decorator(csrf_exempt, name='dispatch')
class EssayView(APIView):
    """文章视图类"""
    def get(self, request, essay_id=None):
        """获取文章"""
        try:
            if essay_id:
                # 获取单篇文章
                essay = Essay.objects.get(id=essay_id)
                return JsonResponse({
                    'code': 200,
                    'message': '获取成功',
                    'data': {
                        'id': essay.id,
                        'title': essay.title,
                        'content': essay.content,
                        'created_at': essay.created_at.strftime('%Y-%m-%d %H:%M:%S')
                    }
                })
            else:
                # 获取文章列表
                essays = Essay.objects.all().order_by('-created_at')
                data = [{
                    'id': essay.id,
                    'title': essay.title,
                    'content': essay.content[:100] + '...' if len(essay.content) > 100 else essay.content,
                    'created_at': essay.created_at.strftime('%Y-%m-%d %H:%M:%S')
                } for essay in essays]
                
                return JsonResponse({
                    'code': 200,
                    'message': '获取成功',
                    'data': data,
                    'total': essays.count()
                })
        
        except Essay.DoesNotExist:
            return JsonResponse({
                'code': 404,
                'message': '文章不存在'
            }, status=404)
        
        except Exception as e:
            return JsonResponse({
                'code': 500,
                'message': f'获取失败: {str(e)}'
            }, status=500)
    
    def post(self, request):
        """上传文章"""
        try:
            data = json.loads(request.body)
            title = data.get('title', '').strip()
            content = data.get('content', '')
            
            # 验证标题不能为空
            if not title:
                return JsonResponse({
                    'code': 400,
                    'message': '标题不能为空'
                }, status=400)
            
            # 保存到数据库
            essay = Essay.objects.create(
                title=title,
                content=content
            )
            
            return JsonResponse({
                'code': 200,
                'message': '文章上传成功',
                'data': {
                    'id': essay.id,
                    'title': essay.title,
                    'created_at': essay.created_at.strftime('%Y-%m-%d %H:%M:%S')
                }
            })
            
        except json.JSONDecodeError:
            return JsonResponse({
                'code': 400,
                'message': '无效的JSON数据'
            }, status=400)
        
        except Exception as e:
            return JsonResponse({
                'code': 500,
                'message': f'上传失败: {str(e)}'
            }, status=500)
        
class RegisterView(APIView):
    """
    用户注册视图类
    处理用户注册请求，包括数据验证、用户创建、JWT token生成等功能
    """
    # 设置权限类，允许任何用户访问此视图
    permision_classes = [AllowAny]
    def post(self, request):
        serializer = UserRegisterSerializer(data = request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    # 创建用户
                    user = UserInfo.objects.create_user(
                        username = serializer.validated_data["username"],
                        # email = serializer.validated_data.get("email", ""),
                        email = serializer.validated_data["email"],
                        password = serializer.validated_data["password"]
                    )
                    # 生成JWT token
                    refresh = RefreshToken.for_user(user)
                    
                    # 成功
                    return Response({
                        'code': 200,
                        'message': "注册成功",
                        'data': {
                            'user': {
                                'id': user.id,
                                'username': user.username,
                                'email': user.email
                            },
                            'token': {
                                'refresh': str(refresh),
                                'access': str(refresh.access_token)
                            }
                        }
                    }, status = status.HTTP_201_CREATED)
                
            except Exception as e:
                return Response({
                    'code': 500, 
                    'message': f"注册失败: {str(e)}"
                }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({
            'code': 400,
            'message': "数据验证失败",
            'error': serializer.errors
        }, status = status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):

    """
    登录视图类，处理用户登录请求
    
    继承自View类，用于处理HTTP POST请求，实现用户认证功能
    允许任何用户访问，无需权限验证
    """
    permision_classes = [AllowAny]  # 设置权限类为允许任何用户访问

    def post(self, request):
        serializer = UserLoginSerializer(data = request.data)

        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            # 验证用户
            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:
                    # 生成JWT token
                    refresh = RefreshToken.for_user(user)

                    return Response({
                        'code': 200,
                        'message': "登录成功",
                        'data': {
                            'user': {
                                'id': user.id,
                                'username': user.username,
                                'email': user.email,
                                'avatar': user.avatar.url if user.avatar else None
                            },
                            'token': {
                                'refresh': str(refresh),
                                'access': str(refresh.access_token)
                            }
                        }
                    }, status = status.HTTP_200_OK)
                else:
                    return Response({
                        'code': 403,
                        'message': "账户已被禁用"
                    }, status = status.HTTP_403_FORBIDDEN)
            else:
                return Response({
                    'code': 401,
                    'message': "用户名或密码错误"
                }, status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'code': 400,
                'message': "数据验证失败"
            }, status = status.HTTP_400_BAD_REQUEST)
        
class LogoutView(APIView):
    permision_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
            return Response({
                'code': 200,
                'message': "登出成功"
            }, status = status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'code': 400,
                'message': f"登出失败:{str(e)}"
            }, status = status.HTTP_400_BAD_REQUEST)

class UserInfoView(APIView):
    permision_classes = [IsAuthenticated]
    
    def get(self, request):
        # 获取当前用户信息
        serializer = UserInfoSerializer(request.user, context = {'request': request})
        return Response({
            'code': 200,
            'message': '获取用户信息成功',
            'data': serializer.data
        }, status = status.HTTP_200_OK)
    
    
    def put(self, request):
        # 更新用户信息
        user = request.user
        serializer = UserInfoSerializer(user, data = request.data, partial = True, context = {'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': 200,
                'message': "更新成功",
                'data': serializer.data
            }, stauts = status.HTTP_200_OK)
        
        return Response({
            'code': 400,
            'message': "数据验证失败",
            'error': serializer.errors
        }, status = status.HTTP_400_BAD_REQUEST)






