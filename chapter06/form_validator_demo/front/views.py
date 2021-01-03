from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import MyForm
# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        form = MyForm(request.POST)
        if not form.is_valid():
            print(form.errors.get_json_data())
            return HttpResponse("fail")
        return HttpResponse("success")
