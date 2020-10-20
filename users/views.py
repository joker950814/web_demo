from django.shortcuts import render

from django.http import HttpResponse

def register(request):
    """注册View视图函数"""
    if request.method == 'GET':
        # 使用 register.html 模板文件, 返回响应
        return render(request, 'register.html')
    else:
        # 获取表单post提交的用户名和密码
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('username: %s password: %s' % (username, password))
        print(123)

        # TODO: 进行注册业务处理

        return HttpResponse('注册成功')
# Create your views here.
