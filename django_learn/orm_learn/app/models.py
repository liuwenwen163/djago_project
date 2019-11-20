# coding:utf-8
from django.db import models
from django.db.models import Model,CharField,IntegerField,SmallIntegerField,EmailField,TextField,DateTimeField,BigIntegerField


class Test(Model):
    name = CharField(max_length=20)
    ages = IntegerField()


class User(Model):
    id = IntegerField(primary_key=True)
    username = CharField(unique=True, max_length=50, blank=False)
    age = SmallIntegerField(default=0)
    phone = BigIntegerField(db_index=True, blank=True, default=0)
    email = EmailField(blank=True, default='')
    info = TextField()
    create_time = DateTimeField(auto_now_add=True)
    update_time = DateTimeField(auto_now=True)

    class Meta:
        index_together = ['username', 'phone']


class Userprofile(Model):
    """创建一个一对一的实例"""
    id = IntegerField(primary_key=True)
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)
    birthday = CharField(max_length=100, blank=True, default='')


class Diary(Model):
    """创建一个一对多的实例"""
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, related_name='diary',
                             on_delete=models.SET_NULL,
                             blank=True, null=True)
    content = models.TextField()
    # 存时间戳到数据库里
    create_time = models.IntegerField()


class Group(Model):
    """多对多关系的表结构，一个用户在多个组里，一个组里有多个用户"""
    id = models.IntegerField(primary_key=True)
    user = models.ManyToManyField(User, related_name='group')
    name = models.CharField(max_length=20)
    create_time = IntegerField()

