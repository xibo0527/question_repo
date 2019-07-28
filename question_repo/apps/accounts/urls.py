
from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'register/$',views.test,name='register'),
    url(r'login/$',views.test,name='login'),
    url(r'logout/$',views.test,name='logout'),
    url(r'password/forget/$',views.test,name='passwd_forget'),
    url(r'password/reset/token/$',views.test,name='passwd_reset'),
]
