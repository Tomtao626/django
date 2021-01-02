from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
# Create your views here.


def index(request):
    print(type(request.GET))
    print(type(request.POST))
    username = request.GET.get('username', 'testname')
    print(username)
    return HttpResponse('success')


@require_http_methods(['GET', 'POST'])
def add_article(request):
    if request.method == 'GET':
        return render(request, 'add_article.html')
    else:
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        # tags = request.POST.get('tags', '')
        # 如果对应传过来的key有多个值，就需要使用getlist
        tags = request.POST.getlist('tags', '')
        print(f"{title}-{content}-{tags}")
        return HttpResponse("success")
