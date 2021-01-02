from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Article


def add_article(request):
    articles = list()
    for x in range(0, 102):
        article = Article(title=f'标题:{x}', content=f'内容:{x}')
        articles.append(article)
    Article.objects.bulk_create(articles)
    return HttpResponse("add success")


class ArticleListView(ListView):
    # 指定要使用的model
    model = Article
    # 指定要渲染的模板名称
    template_name = 'article_list_1.html'
    # 指定返回给模板的结果集名称
    context_object_name = 'articles'
    # 分页参数 一页展示条数
    paginate_by = 10
    # 查询结果集根据什么字段排序
    ordering = 'add_time'
    # 指定分页参数名称
    page_kwarg = 'p'

    def get_context_data(self, **kwargs):
        # 先调用继承父类ArticleListView的get_context_data()方法
        context = super(ArticleListView, self).get_context_data(*kwargs)
        context['username'] = 'tomtao'
        paginator = context['paginator']
        # 总共有多少页
        print(f"总共有{paginator.num_pages}页")
        # 总共有多少条数据
        print(f"总共有{paginator.count}条数据")
        # 分区区间
        print(f"分区区间-{paginator.page_range}")
        page_obj = context['page_obj']
        print(page_obj.number)
        paginator_data = self.get_pagination_data(paginator, page_obj)
        context.update(paginator_data)
        return context

    # 如果需要对返回的数据进行的过滤 则需要使用get_queryset()方法 不然则默认返回全部数据
    # 即 return Article.objects.all()
    # def get_queryset(self):
        # 查询id小于9的数据并返回
        # return Article.objects.filter(id__lte=9)

    def get_pagination_data(self, paginator, page_obj, around_count=2):
        # 总页数
        num_pages = paginator.num_pages
        current_page = page_obj.number
        left_has_more = False
        right_has_more = False
        # 左边的页码
        if current_page <= around_count+2:
            left_pages = range(1, current_page)
        else:
            left_has_more = True
            left_pages = range(current_page-around_count, current_page)
        # 右边的页码
        if current_page >= num_pages-around_count-1:
            right_pages = range(current_page+1, num_pages+1)
        else:
            right_has_more = True
            right_pages = range(current_page+1, current_page+around_count+1)
        return dict(left_pages=left_pages,
                    current_page=current_page,
                    right_pages=right_pages,
                    left_has_more=left_has_more,
                    right_has_more=right_has_more,
                    num_pages=num_pages)
