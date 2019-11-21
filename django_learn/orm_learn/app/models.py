# coding:utf-8
import json
from functools import wraps

from django.db import models
from django.db.models import Model,CharField,IntegerField,SmallIntegerField,EmailField,TextField,DateTimeField,BigIntegerField
from django_redis import get_redis_connection

_cache = get_redis_connection('default')


def cache(func):
    """django中redis的用法"""
    @wraps(func)
    def wrapper(obj, *args):
        key = args[0]
        value = _cache.get(key)
        if value:
            return json.loads(value)
        rs = func(obj, *args)
        _cache.set(key, json.dumps(rs))
        return rs
    return wrapper



class Test(Model):
    name = CharField(max_length=20)
    ages = IntegerField()

"""删去了各个数据模型中的id字段，id就变成了自增的，写上就需要手动添加"""

class User(Model):
    username = CharField(unique=True, max_length=50, blank=False)
    age = SmallIntegerField(default=0)
    phone = BigIntegerField(db_index=True, blank=True, default=0)
    email = EmailField(blank=True, default='')
    info = TextField()
    create_time = DateTimeField(auto_now_add=True)
    update_time = DateTimeField(auto_now=True)

    class Meta:
        index_together = ['username', 'phone']

    def __str__(self):
        return 'username:'+self.username

    @classmethod
    @cache
    def get(cls, id):
        rs = cls.objects.get(id=id)
        return {
            'id': rs.id,
            'username': rs.username,
            'age': rs.age,
            'email': rs.email,
            'info': rs.infl,
            'create_time': str(rs.create_time),
            'update_time': str(rs.update_time)
        }


class Userprofile(Model):
    """创建一个一对一的实例"""
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)
    birthday = CharField(max_length=100, blank=True, default='')


class Diary(Model):
    """创建一个一对多的实例"""
    user = models.ForeignKey(User, related_name='diary',
                             on_delete=models.SET_NULL,
                             blank=True, null=True)
    content = models.TextField()
    # 存时间戳到数据库里
    create_time = models.IntegerField()


class Group(Model):
    """多对多关系的表结构，一个用户在多个组里，一个组里有多个用户"""
    user = models.ManyToManyField(User, related_name='group')
    name = models.CharField(max_length=20)
    create_time = IntegerField()

