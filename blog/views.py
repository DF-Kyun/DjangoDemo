from django.http import HttpResponse

def hello(request):
    return HttpResponse('欢迎使用Django！')
