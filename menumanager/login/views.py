from django.http import HttpResponse
# Create your views here.

def login(name):
  return HttpResponse("登录页面")
from django.shortcuts import render,redirect
# Create your views here.

def login(request):
  if request.method == 'POST':
     username = request.POST.get('username')
     passowrd = request.POST.get('password')
     if username=='sunbowen' and passowrd =='770609':
        return redirect('/index')
     else:
        return render(request,'login.html',{"error":"用户名或密码错误"})

  return render(request,'login.html')


from django.shortcuts import render  
from django.shortcuts import render  
from .models import UserChoice  # 设模型类名为userchoice  
from easygui import msgbox  
import random  
import mysql.connector  
import datetime  
  
def calculate(request):  
    if request.method == 'GET':  
        msg = "嗨,今天想吃什么菜啊。"  
        title = "点菜互动"  
        choices = ["一荤两素一汤", "两荤一素一汤"]  
        return render(request, 'your_template_name.html', {'msg': msg, 'title': title, 'choices': choices})
    elif request.method == 'POST':  
        choice = request.POST.get('choice')  # 获取用户的选择  
        if choice == '一荤两素一汤':  
            # 处理选择一荤两素一汤的情况   
            pass  
        elif choice == '两荤一素一汤':  
            # 处理选择两荤一素一汤的情况  
            pass  
        return render(request, 'result_template.html', {'result': '相应的结果'})
