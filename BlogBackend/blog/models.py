from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Essay(models.Model):
    """文章模型"""
    title = models.CharField(max_length=200, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        db_table = 'essay'
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-created_at']  # 按创建时间倒序排列
    
    def __str__(self):
        return self.title

class UserInfo(AbstractUser):
    # ✅ 不要重新定义 username, password, email
    # AbstractUser 已经包含了这些字段
    # 用户头像
    avatar = models.ImageField(upload_to='avatars/', blank=True, verbose_name="头像")
    
    class Meta:
        db_table = "user_info"
        verbose_name = "用户"
        verbose_name_plural = "用户"
    
    def __str__(self):
        return self.username  # ✅ 直接用父类的 username


