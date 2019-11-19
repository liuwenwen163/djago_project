# encoding: utf-8
"""练习自定义过滤器"""

from django import template
from app.consts import SensitiveWord
import jieba

register = template.Library()

@register.filter
def sample_check(value):
    """使用jiaba将中文字符串拆分成数组"""
    # 使用jieba将
    cut_message = jieba.lcut(value)
    # print(cut_message)
    # print(SensitiveWord)

    check = list(set(cut_message) & set(SensitiveWord))

    if not check:
        return '该消息涉及违禁词汇，已被屏蔽'
    return value


@register.filter(name='deep_check_message')
def deep_check(value):
    cut_message = jieba.lcut(value)

    new_message = []

    for m in cut_message:
        if m in SensitiveWord:
            new_message.append('*')
        else:
            new_message.append(m)

    if new_message:
        return ''.join(new_message)
    return value

