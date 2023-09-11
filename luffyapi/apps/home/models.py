from django.db import models
from utils.models import BaseModel
# Create your models here.


class Banner(BaseModel):
    name = models.CharField(max_length=32, verbose_name='图片名字')
    img = models.ImageField(upload_to='banner',verbose_name='轮播图',help_text='图片尺寸必须是：3840*800')
    link = models.CharField(max_length=255,verbose_name='跳转链接')
    info = models.TextField(null=True)
    max_display_count = models.IntegerField(default=3)

    def __str__(self):
        return self.name


class SysConfig(models.Model):
    conf = models.CharField(max_length=64)
    limit = models.CharField(max_length=32)