from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .models import Article
from .forms import ArticleForm


# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    # def post(self, request):
    #     myfile = request.FILES.get('myfile')
    #     with open('somefile.jpg', 'wb') as fb:
    #         for chunk in myfile.chunks():
    #             fb.write(chunk)
    #     return HttpResponse("success")

    # def post(self, request):
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     file = request.FILES.get('myfile')
    #     Article.objects.create(title=title, content=content, thumbnail=file)
    #     return HttpResponse("success")

    def post(self,request):
        form = ArticleForm(request.POST, request.FILES)
        if not form.is_valid():
            print(form.errors.get_json_data())
            return HttpResponse("upload fail")
        form.save()
        return HttpResponse("success")

