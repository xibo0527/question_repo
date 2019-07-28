from django.shortcuts import render,redirect,HttpResponse
import logging
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