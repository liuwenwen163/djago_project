# coding:utf-8
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
