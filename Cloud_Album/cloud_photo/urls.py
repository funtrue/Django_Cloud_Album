from django.urls import path
from cloud_photo.views import home

# App名称
# 用于Django幕后的url查询
app_name = 'photo'

# url列表
urlpatterns = [
    path('', home, name='home'),
]