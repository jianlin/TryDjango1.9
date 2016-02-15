from django.shortcuts import render
#
# # Create your views here.


from django.http import HttpResponse
import json

def index(request):
    arr = [[x+y for x in [1,2,3,4]] for y in [10,100,1000]]
    s = json.dumps(arr, sort_keys=True, indent=4)
    return HttpResponse("<pre>Hello, world. You're at the polls index.\n" + s)
