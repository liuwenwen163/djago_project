from django.http import HttpResponse
from django.views.generic import View


class Index(View):
    def get(self, request, name, age):
        print(dir(request))
        return HttpResponse('hello i am {0}, age is {1}'.format(name, age))