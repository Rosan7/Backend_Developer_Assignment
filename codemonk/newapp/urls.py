from django.contrib import admin
from django.urls import path,include
from .views import *


# router = routers.DefaultRouter()
# router.register(r'paragraphs',ParaViewSet)
urlpatterns = [
    path('post_para',post_paragraphs,name="post_para"),
    path('get_paras',get_paras,name='get_paras'),
    path('login',login_page,name="login_page"),
    path('register',register,name="signup_page")
]
