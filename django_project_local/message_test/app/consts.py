# encoding: utf-8
"""consts文件一般都存储一些静态文件"""

from enum import Enum


class MessageType(Enum):
    info = 'info'
    warning = 'warning'
    error = 'error'
    danger = 'danger'


MessageType.info.label = '信息'
MessageType.warning.label = '警告'
MessageType.error.label = '错误'
MessageType.danger.label = '危险'


MessageType.info.color = 'green'
MessageType.warning.color = 'orange'
MessageType.error.color = 'gray'
MessageType.danger.color = 'red'

# 定义一些敏感词由过滤器捕获
SensitiveWord = ['天气', '坏人', '不开心']
# 非常敏感的词，不允许存入数据库
SensitiveWordInit = ['专业', '生活']
