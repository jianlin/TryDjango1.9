from django.shortcuts import render
#
# # Create your views here.


from django.http import HttpResponse


def index(request):
    arr = [[x+y for x in [1,2,3,4]] for y in [10,100,1000]]
    s = str(arr)
    return HttpResponse("<pre>Hello, world. You're at the polls index." + s)
