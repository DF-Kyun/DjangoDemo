from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Banner, Article, Tag, Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def hello(request):
    return HttpResponse('欢迎使用Django！')

# 首页
def index(request):
    allcategory = Category.objects.all()   #通过Category表查出所有分类
    banner = Banner.objects.filter(is_active=True)[0:4]
    tui = Article.objects.filter(tui__id=1)[:3]  #查询推荐位ID为1的文章
    allarticle = Article.objects.all().order_by('-id')[0:10]
    hot = Article.objects.all().order_by('views')[:10]
    remen = Article.objects.filter(tui__id=2)[:6]
    tags = Tag.objects.all()
    link = Link.objects.all()
    context = {
            'allcategory': allcategory,
            'banner':banner,
            'tui':tui,
            'allarticle': allarticle,
            'hot':hot,
            'remen':remen,
            'tags':tags,
            'link':link,
        }
    return render(request, 'index.html', context)

#列表页
def list(request,lid):

    list = Article.objects.filter(category_id=lid) 
    page = request.GET.get('page')
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    cname = Category.objects.get(id=lid) 
    remen = Article.objects.filter(tui__id=2)[:6] 
    allcategory = Category.objects.all() 
    tags = Tag.objects.all()    
    return render(request, 'list.html', locals())

#内容页
def show(request,sid):

    show = Article.objects.get(id=sid)
    allcategory = Category.objects.all()
    tags = Tag.objects.all()
    remen = Article.objects.filter(tui__id=2)[:6]
    hot = Article.objects.all().order_by('?')[:10]
    previous_blog = Article.objects.filter(created_time__gt=show.created_time,category=show.category.id).first()
    netx_blog = Article.objects.filter(created_time__lt=show.created_time,category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'show.html', locals())

#标签页
def tag(request, tag):
    list = Article.objects.filter(tags__name=tag)
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    tname = Tag.objects.get(name=tag)
    page = request.GET.get('page')
    tags = Tag.objects.all()
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)  
    except PageNotAnInteger:
        list = paginator.page(1)  
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  
    return render(request, 'tags.html', locals())

# 搜索页
def search(request):
    ss=request.GET.get('search')
    list = Article.objects.filter(title__icontains=ss)
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    page = request.GET.get('page')
    tags = Tag.objects.all()
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page) 
    except PageNotAnInteger:
        list = paginator.page(1) 
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, 'search.html', locals())

# 关于我们
def about(request):
    allcategory = Category.objects.all()
    return render(request, 'page.html',locals())
