"""class_view_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.BookListView.as_view(), name='book_list'),
    path('add_book/', views.AddBookView.as_view(), name='add_book'),
    path('book_detail/<book_id>/', views.BookDetailView.as_view(), name='book_detail'),
    # 如果需要渲染的模板不需要传递任何的参数，建议在urls中使用TemplateView
    # path('about/', TemplateView.as_view(template_name='about.html')),
    # 如若需要传递参数，则需要使用新的view视图
    path('about/', views.AboutView.as_view(), name='about'),
    path('article/', include('front.urls'))
]
