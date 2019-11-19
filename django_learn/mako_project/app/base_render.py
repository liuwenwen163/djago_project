# encoding: utf-8

from mako.lookup import TemplateLookup
from django.template import RequestContext, Context
from django.conf import settings
from django.http import HttpResponse


def render_to_response(request, template, data=None):
    context_instance = RequestContext(request)
    # 获取模板的路径
    path = settings.TEMPLATES[0]['DIRS'][0]

    # 创建mako需要的配置文件
    lookup = TemplateLookup(
        directories=[path],
        output_encoding='utf-8',
        input_encoding='utf-8'
    )
    mako_template = lookup.get_template(template)

    if not data:
        data = {}

    # 判断当前实例是否存在，不存在的话将实例加入
    if context_instance:
        context_instance.update(data)
    else:
        context_instance = Context(data)

    result = {}

    for d in context_instance:
        result.update(d)

    result['csrf_token'] = '<input type="hidden" name="csrfmiddlewaretoken" value="{0}" />'.format(request.META.get('CSRF_COOKIE', ''))
    return HttpResponse(mako_template.render(**result))



