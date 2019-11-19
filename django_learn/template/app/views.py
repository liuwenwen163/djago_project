# encoding: utf-8
from django.shortcuts import render
from django.views.generic import View

class Index(View):
    TEMPLATE = 'index.html'

    def get(self, request, name):
        data = {}
        data['name'] = name
        data['array'] = range(10)
        data['count'] = 20
        return render(request, self.TEMPLATE, data)


