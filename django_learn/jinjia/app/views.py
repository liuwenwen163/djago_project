from django.shortcuts import render

# Create your views here.

def test(request):
    data = {'name':'liming', 'age':18}
    return render(request, 'test.html')


