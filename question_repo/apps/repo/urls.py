
from django.conf.urls import url,include
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    url('^$',views.index,name='index'),
    # 题目列表
    url('^questions/$',views.QuestionsList.as_view(),name='questions'),
    # 贡献题目
    url('^question/$',views.Question.as_view(),name='question'),
    # 题目详情
    url('^question/(?P<id>\d+)/$',views.QuestionDetail.as_view(),name='question_detail'),
]
