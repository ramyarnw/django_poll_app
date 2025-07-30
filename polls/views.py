from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import Question
from django.template import loader

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
#def detail(request,question_id):
#    return HttpResponse("You are look at question %s." % question_id)
def results(request,question_id):
    response = "You are looking at results of question %s."
    return HttpResponse(response % question_id)
def vote(request,question_id):
    response = "You are voting on question %s."
    return HttpResponse(response % question_id)
    
#    index page
#    list recent top 3 question in index page
#def index(request):
#    latest_question_list = Question.objects.order_by("pub_date")[:3]
#    output = ", ".join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)

#render template
#def index(request):
#    latest_question_list = Question.objects.order_by("pub_date")[:3]
#    template = loader.get_template("polls/index.html")
#    context = {"latest_question_list": latest_question_list}
#    return HttpResponse(template.render(context, request))

#render shortcut
def index(request):
    latest_question_list = Question.objects.order_by("pub_date")[:3]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
#def detail(request,question_id):
#    try:
#       question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#       raise Http404("Question does not exist")
#       context = {"question": question}
#    return render(request, "polls/detail.html", context)

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "polls/detail.html", context)
    


    
    
 



    
