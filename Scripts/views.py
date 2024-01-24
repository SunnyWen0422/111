import json
import random
from . import models
from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector  # 导入mysql的连接器
# 连接到MySQL数据库
def connect_to_mysql():
    conn = mysql.connector.connect(
        host='127.0.0.1',  # 例如: localhost
        user='root',  # 你的数据库用户名
        password='770609',  # 你的数据库密码
        database='menu'  # 你的数据库名
    )
    return conn

def get_menu(request):
    if request.method == 'GET':
        meat_count = request.GET.get('meat')  # 获取荤菜数量
        veggie_count = request.GET.get('veggie')  # 获取素菜数量
        prev_dish = []  # 初始化一个空列表来存储之前的菜

        # 获取所有菜品
        all_dishes = models.dish.objects.all()

        # 根据类型筛选菜品并随机选择
        data = {
            'meat': [],
            'veggie': []
        }

        meat, veggie = [], []
        for dish in all_dishes:
            if dish.type == 1:  # 如果菜品类型为meat，则添加到meat列表中
                meat.append(dish.name)
            elif dish.type == 2:  # 如果菜品类型为veggie，则添加到veggie列表中
                veggie.append(dish.name)
            meat_dishes = Dish.objects.filter(type=1).order_by('?')[:int(meat_count)]  # 获取指定数量的荤菜
            veggie_dishes = Dish.objects.filter(type=2).order_by('?')[:int(veggie_count)]  # 获取指定数量的素菜

    response = {
        "code": '10002',
        "message": "success",
        "data": data,
        "prev_dish": prev_dish  # 将空列表作为prev_dish返回，因为之前没有存储数据
    }
    return HttpResponse(json.dumps(response))
