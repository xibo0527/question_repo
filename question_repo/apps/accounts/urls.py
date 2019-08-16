from django.conf.urls import url,include

from . import views
urlpatterns = [
    url(r'register/$',views.Register.as_view(),name='register'),
    url(r'login/$',views.Login.as_view(),name='login'),
    url(r'logout/$',views.logout,name='logout'),
    url(r'password/forget/$',views.PasswordForget.as_view(),name='passwd_forget'),
    url(r'password/reset/(?P<verify_code>\w+)/$',views.PasswordReset.as_view(),name='passwd_reset'),
]
