from django.shortcuts import render,HttpResponse
from django.views.generic import View,DetailView
from .models import Category,Questions,UserLog
from apps.accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    userlog = UserLog.objects.all()[:10]
    print(UserLog.objects.filter(operate=3).values('user').distinct()[:10])
    # user_id_lists = [item['user'] for item in UserLog.objects.filter(operate=3).values('user').distinct()[:10]]
    user_id_lists = [item['user'] for item in UserLog.objects.filter(operate=3).values('user').distinct()[:10]]
    print(user_id_lists)
    users = User.objects.filter(id__in=user_id_lists)
    # print(users)
    kwgs = {
        'userlog':userlog,
        'users':users
    }
    return render(request,'index.html',kwgs)

class QuestionsList(LoginRequiredMixin,View):
    def get(self,request):
        category = Category.objects.all().values("id", "name")
        grades = Questions.DIF_CHOICES
        search = request.GET.get('search', '')
        kwgs = {"category": category, "grades": grades, 'search':search}
        return render(request, 'questions.html', kwgs)

from apps.repo.models import Answers
import json
from django.core import serializers
from django.http import JsonResponse
import logging
logger = logging.getLogger('repo')

class QuestionDetail(LoginRequiredMixin,DetailView):
    model = Questions
    pk_url_kwarg = 'id'  # 默认按主键来选取一个model对象
    template_name = "question_detail.html"
    # 默认名：object
    context_object_name = "object"

    # 额外传递my_answer
    def get_context_data(self, **kwargs):
        # kwargs：字典、字典中的数据返回给html页面
        # self.get_object() => 获取当前id的数据（问题）
        question = self.get_object()  # 当前这道题目
        kwargs["my_answer"] = Answers.objects.filter(question=question, user=self.request.user)
        return super().get_context_data(**kwargs)

    def post(self, request, id):
        from django.db import transaction
        try:
            with transaction.atomic():
                # 没有回答过。create
                # 更新回答。get->update
                # 获取对象，没有获取到直接创建对象
                new_answer = Answers.objects.get_or_create(question=self.get_object(), user=self.request.user)
                # 元组：第一个元素获取/创建的对象， True（新创建）/False（老数据）
                new_answer[0].answer = request.POST.get("answer", "没有提交答案信息") # 更新答案
                new_answer[0].save() # models实例对象
                UserLog.objects.create(user=request.user,operate=3,question=self.get_object())
            my_answer = json.loads(serializers.serialize("json", [new_answer[0]]))[0]["fields"]
            msg = "提交成功"
            code = 200
        except Exception as ex:
            logger.error(ex)
            my_answer = {}
            msg = "提交失败"
            code = 500

        result = {"status": code, "msg": msg, "my_answer": my_answer}
        return JsonResponse(result)


class Question(LoginRequiredMixin,View):

    def post(self,request):
        try:
            title = request.POST.get("title")
            category = request.POST.get("category")
            content = request.POST.get("content")
            if category:
                Questions.objects.create(title=title, category_id=category, content=content, contributor=request.user)
            else:
                Questions.objects.create(title=title, content=content, contributor=request.user)
        except Exception as ex:
            logger.error(ex)
            return HttpResponse("提交失败!")
        return HttpResponse("提交成功")