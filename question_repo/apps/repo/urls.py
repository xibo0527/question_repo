
from django.conf.urls import url,include
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    url('^$',TemplateView.as_view(template_name="index.html"),name='index'),
    # 题目列表
    url('^questions/$',TemplateView.as_view(template_name="questions.html"),name='questions'),
    # 贡献题目
    url('^question/$',views.test,name='question'),
    # 题目详情
    url('^question/id/$',
        TemplateView.as_view(template_name="question_detail.html"),
        views.test,name='question_detail'),
]
