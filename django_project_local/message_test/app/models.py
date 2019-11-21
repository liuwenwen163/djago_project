# coding:utf-8
from django.db import models


class Message(models.Model):
    content = models.TextField()
    message_type = models.CharField(max_length=10, db_index=True)
    created_time = models.IntegerField(default=0)

    def __str__(self):
        return 'type:{}, content:{}'.format(self.message_type, self.content)


