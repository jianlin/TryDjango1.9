from django.shortcuts import render
#
# # Create your views here.

from django.shortcuts import get_object_or_404, render

from django.http import Http404
from django.http import HttpResponse
from django.template import loader

from .models import Question

import json

#from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def index_using_loader(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def index_without_using_template(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', \n'.join([str(vars(q)) for q in latest_question_list])
    return HttpResponse("<pre>" + output)

def index1(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', \n'.join([q.question_text for q in latest_question_list])
    return HttpResponse("<pre>" + output)

def index2(request):
    arr = [[x+y for x in [1,2,3,4]] for y in [10,100,1000]]
    s = json.dumps(arr, sort_keys=True, indent=4)
    return HttpResponse("<pre>Hello, world. You're at the polls index.\n" + s)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    
def detail2(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def detail1(request, question_id):
    return HttpResponse("<pre>You're looking at question %s." % vars(Question.objects.get(pk=question_id)))


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
