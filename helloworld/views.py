from django.shortcuts import render

from django.http import HttpResponse

def first_view_func(request):
    """
    第一个 View 视图处理函数
    request: 每个视图函数都必须有一个参数, 用来接收请求对象, 参数名习惯叫做request
    """

    return HttpResponse('<h1>hello world</h1>')
# Create your views here.
