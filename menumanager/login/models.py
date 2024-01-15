from django.db import models  
  
class UserChoice(models.Model):  
    CHOICES = (  
        ('option1', '一荤两素一汤'),  
        ('option2', '两荤一素一汤'),  
    )  
    choice = models.CharField(max_length=20, choices=CHOICES)  
    data = models.TextField()  # 用于存储从数据库中提取的数据