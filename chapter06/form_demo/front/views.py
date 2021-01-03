from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import MessageBoardForm


# Create your views here.


class IndexView(View):
    def get(self, request):
        form = MessageBoardForm()
        return render(request, 'index.html', context=dict(form=form))

    def post(self, request):
        form = MessageBoardForm(request.POST)
        # 判断数据是否合法
        if not form.is_valid():
            print(form.errors)
            return HttpResponse("fail")
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        email = form.cleaned_data.get('email')
        reply = form.cleaned_data.get('reply')
        print(title)
        print(content)
        print(email)
        print(reply)
        return HttpResponse("success")
