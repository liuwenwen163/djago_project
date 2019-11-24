# coding:utf-8
from django.contrib import admin
from .models import Message


# 将Message注册进入admin
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'message_type', 'times']
    readonly_fields = ['created_time']

    list_filter = ['message_type']
    search_fields = ['content']
    ordering = ['-id']
    list_per_page = 5

    def save_model(self, request, obj, form, change):
        if change:
            # update
            obj.content = obj.content + 'update'
        else:
            #create
            obj.content = obj.content + 'create'

        super(MessageAdmin, self).save_model(request, obj, form, change)
