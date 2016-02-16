from django.shortcuts import render
#
# # Create your views here.


from django.http import HttpResponse
import json

def index(request):
    arr = [[x+y for x in [1,2,3,4]] for y in [10,100,1000]]
    s = json.dumps(arr, sort_keys=True, indent=4)
    return HttpResponse("<pre>Hello, world. You're at the polls index.\n" + s)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

    
