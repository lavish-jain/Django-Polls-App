from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
# from django.template import loader

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    # output = ", ".join([q.question_text for q in latest_questions])
    context = {
        "latest_questions": latest_questions
    }
    return render(request, "polls/index.html", context)

def details(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question with given ID does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/details.html", {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
    # Redisplay the details page with error
        return render(request, "polls/details.html", {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

