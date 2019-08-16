from libs.repo_data import user_answer_data
from apps.repo.models import Answers,Category

def repo_data(request):
    if request.user.is_authenticated:
        user_data = user_answer_data(request.user)
    hot_question = Answers.objects.hot_question()
    hot_user = Answers.objects.hot_user()
    category = Category.objects.all()
    current_url = request.path
    return locals()

"""
hot_question:
<QuerySet [{'questions__title': '单向链表如何使用快速排序算法进行排序；', 'id__count': 3}, 
{'question__title': '三次握手', 'id__count': 2}, {'question__title': 'ARP协议', 'id__count': 1}, {'question__title': 'c10k问题', 'id__count': 1}, {'question__title': 'urllib和urllib2的区别', 'id__count': 1}]>
hot_user:
< QuerySet[{'user__username': 'admin', 'id__count': 8}, {'user__username': 'xibo', 'id__count': 3}, {
        'user__username': 'hrb', 'id__count': 1}] >
"""