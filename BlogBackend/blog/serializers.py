# 序列化器,用于后端安全验证
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import UserInfo


class UserRegisterSerializer(serializers.Serializer):
    """
    用户注册序列化器类，用于验证和序列化用户注册数据
    继承自serializers.Serializer，提供数据验证和序列化功能
    """
    # 用户名验证
    username = serializers.CharField(
        required=True, min_length=3, max_length=30, error_messages={
            "required": "用户名不能为空",
            "min_length": "用户名至少为3个字符",
            "max_length": "用户名至多为30个字符"
        }
    )

    # 密码长度验证
    password = serializers.CharField(
        required=True, min_length=6, error_messages={
            "required": "密码不能为空",
            "min_length": "密码至少为6个字符"
        }
    )

    # 确认密码验证
    passwordAgain = serializers.CharField(
        required=True, write_only=True, error_messages={
            "required": "确认密码不能为空"
        }
    )

    # 邮箱验证
    email = serializers.EmailField(
        required=True, error_messages={
            "required": "邮箱不能为空"
        }
    )

    def validate_username(self, value):
        # 验证用户名是已否存在
        if UserInfo.objects.filter(username=value).exists():
            raise serializers.ValidationError("用户名已存在")
        return value
    
    def validate_email(self, value):
        # 验证邮箱是否已存在
        if value and UserInfo.objects.filter(email=value).exists():
            raise serializers.ValidationError("邮箱已被注册")
        return value

    def validate(self, attrs):
        # 验证两次密码是否一致
        if attrs["password"] != attrs["passwordAgain"]:
            raise serializers.ValidationError(
                {"passwordAgain": "两次密码不一致"}
            )
        
        # 使用Django的密码验证器
        try:
            validate_password(attrs["password"])
        except Exception as e:
            raise serializers.ValidationError(
                {"password": list(e.messages)}
            )
        return attrs
    

class UserLoginSerializer(serializers.Serializer):
    """用户登录序列化器"""
    username = serializers.CharField(
        required=True,
        error_messages={'required': '用户名不能为空'}
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        error_messages={'required': '密码不能为空'}
    )


class UserInfoSerializer(serializers.ModelSerializer):
    """用户信息序列化器"""
    avatar_url = serializers.SerializerMethodField()
    
    class Meta:
        model = UserInfo
        fields = ['id', 'username', 'email', 'avatar', 'avatar_url', 
                  'date_joined', 'last_login']
        read_only_fields = ['id', 'username', 'date_joined', 'last_login']
    
    def get_avatar_url(self, obj):
        """获取头像完整URL"""
        if obj.avatar:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.avatar.url)
            return obj.avatar.url
        return None