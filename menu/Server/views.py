import json
import random
from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector  # 导入mysql的连接器
from Server.views import index

# 连接到MySQL数据库
def connect_to_mysql():
    conn = mysql.connector.connect(
        host='localhost',  # 例如: localhost
        user='root',  # 你的数据库用户名
        password='Sunny418',  # 你的数据库密码
        database='menu'  # 你的数据库名
    )
    return conn


# 获取菜单数据
def get_menu(request):
    if request.method == 'GET':
        meat = request.GET.get('1')
        veggie = request.GET.get('2')
        prev_dish = []  # 初始化一个空列表来存储之前的菜

        # 连接到数据库并获取数据
        conn = connect_to_mysql()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM menu")  # 假设你的表名为menu，字段为id, name, type
        all_dishes = cursor.fetchall()  # 获取所有菜品数据
        cursor.close()
        conn.close()

        # 根据类型筛选菜品并随机选择
        data = {
            '1': [],
            '2': []
        }
        for dish in all_dishes:
            dish_name, dish_type = dish[1], dish[2]  # 假设id为菜品ID，name为菜品名，type为菜品类型
            if dish_type == '1':  # 如果菜品类型为meat，则添加到meat列表中，并随机选择两个
                data['meat'].append(dish_name)
                if random.choice([True, False]):  # 随机选择一个是否需要加入新的菜品到meat列表中（只选择两次）
                    data['meat'].append(random.choice(data['meat']))  # 从meat列表中随机选择一个菜品加入到列表中（如果需要的话）
            elif dish_type == '2py':  # 如果菜品类型为veggie，则添加到veggie列表中，并随机选择一个
                data['veggie'].append(dish_name)
                if random.choice([True, False]):  # 随机选择一个是否需要加入新的菜品到veggie列表中（只选择一次）
                    data['veggie'].append(random.choice(data['veggie']))  # 从veggie列表中随机选择一个菜品加入到列表中（如果需要的话）
        response = {
            "code": '10002',
            "message": "success",
            "data": data,
            "prev_dish": prev_dish  # 将空列表作为prev_dish返回，因为之前没有存储数据
        }
        return HttpResponse(json.dumps(response))