from django.shortcuts import render
from rest_framework.views import APIView
from luffyapi.utils.response import APIResponse
# Create your views here.


# class TestView(APIView):
#     def get(self,request):
#         dic = {'name':'lmk'}
#         print('xxx')
#         # 允许8001朝我这里发
#         return APIResponse(result=dic,headers={'Access-Control-Allow-Origin':'*'})
#
#     def post(self,request):
#         dic = {'name':'lmk'}
#         print('post')
#         # 允许8001朝我这里发
#         return APIResponse(result=dic,headers={'Access-Control-Allow-Origin':'*'})
#
#     def options(self, request, *args, **kwargs):
#         print('options')
#         return APIResponse()

from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from . import models
from .serializer import BannerModelSerializer
from django.conf import settings


class BannerView(GenericViewSet,ListModelMixin):
    # 无论有多少条待展示的数据，就展示3条
    limit = models.SysConfig.objects.filter(conf='BANNER_COUNTER').first().limit
    limit = int(limit)
    queryset = models.Banner.objects.filter(is_delete=False,is_show=True).order_by('display_order')[:limit]
    serializer_class = BannerModelSerializer
