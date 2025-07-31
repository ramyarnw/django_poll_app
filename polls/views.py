from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.db.models import F
from django.views import generic






##render shortcut
#def index(request):
#    latest_question_list = Question.objects.order_by("pub_date")[:3]
#    context = {"latest_question_list": latest_question_list}
#    return render(request, "polls/index.html", context)
#    
#
#   
#def detail(request,question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    context = {"question": question}
#    return render(request, "polls/detail.html", context)

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last three published questions."""
        return Question.objects.order_by("-pub_date")[:3]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
# Redisplay the question voting form.
        context = {
            "question": question,
            "error_message": "You didn't select a choice.",
        }
        return render(request, "polls/detail.html", context)
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
#        prevent data process twice, if we cick back
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        
#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    context = {"question": question}
#    return render(request, "polls/results.html", context)
        
    
    
    
 



    
