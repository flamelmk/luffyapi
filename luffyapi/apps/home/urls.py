from django.urls import path, re_path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('banner', views.BannerView, 'banner')

urlpatterns = [
    # path('home/', views.TestView.as_view()),
    path('',include(router.urls)),
]
