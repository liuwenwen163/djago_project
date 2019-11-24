# encoding: utf-8

import jieba

from django import forms

from .consts import MessageType, SensitiveWordInit


# 动态的从 MessageType 中获取类别信息
# 元组中第一个值是提交值，第二个值是表单中的展示值
MESSAGE_TYPE_CHOICES = tuple(
    [(message.value, message.value) for message in MessageType]
)

class MessageForm(forms.Form):
    content = forms.CharField(label='消息内容', max_length=100, required=True)
    message_type = forms.CharField(
        label='数据类型',
        max_length=10,
        widget=forms.Select(choices=MESSAGE_TYPE_CHOICES)
    )

    def clean_message_type(self):
        # sel.cleaned_data 是一个上面两个字段作为key的dict字典数据
        # 此处就是获取到实际传入的表单中，message_type对应的value
        message_type = self.cleaned_data.get('message_type')

        if not message_type:
            raise forms.ValidationError('消息类型不能为空！')

        try:
            # 从元组类中看能否获取到内部对应的数据
            message_type_obj = MessageType[message_type]
        except:
            raise forms.ValidationError('无效的消息类型')

        return message_type_obj

    def clean_content(self):
        content = self.cleaned_data.get('content')

        if not content:
            raise forms.ValidationError('消息不能为空')

        cut_message = jieba.lcut(content)

        check = list(set(cut_message) & set(SensitiveWordInit))

        if check:
            raise forms.ValidationError('该消息涉及违禁词汇，已被屏蔽')

        return content


