'''

'''
from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver

# 当请求完成后，打印一个日志
# @receiver(request_finished)
# def all_log(sender,**kwargs):
#     print(sender,kwargs)
#     print('使用信号记日志')

# 当创建了一条记录Maillog之后，会自动执行发送邮件
'''
@receiver(post_save,sender=MailLog)
def send_mail(sender,instance,**kwargs):
    pass
'''