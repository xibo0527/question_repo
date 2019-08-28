from django.shortcuts import render,redirect,HttpResponse
import logging
from django.views.generic import View
from apps.repo.models import Questions
from django.core.paginator import Paginator
# Create your views here.

logger = logging.getLogger('apis')

def logtest(request):
    logger.info('欢迎访问')
    return HttpResponse('日志测试')

def index(request):
    kwgs = {
    'username' : [{'name':'admin'},
        {'name':'xibo'},
        {'name':'dema'},
        {'name':'bancun'},
        {'name':'niushao'},
        {'name':'dajiao'},
        {'name':'bige'},
        {'name':'gebulin'},
        {'name':'goulaiji'},
        {'name':'dige'},]
    }
    return render(request,'app01/title.html',kwgs)

class Pagi(View):
    def get(self,request):
        page_num = request.GET.get('page')
        pagesize = 25
        objects = Questions.objects.all()
        p = Paginator(objects,pagesize)
        contacts = p.page(page_num)
        kwgs = {
            'contacts':contacts
        }
        return render(request,'list.html',kwgs)