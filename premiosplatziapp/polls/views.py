from django import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic


from django.utils import timezone

from .models import Question, Choice


#Las vistas siempre reciben un request http
"""
def index(request):
  latest_question_list = Question.objects.all() #traer todas las preguntas
  
  return render(request, "polls/index.html", {
    "latest_question_list": latest_question_list
  })


#Class Based views - Generoc Visews
#Vistas genéricas para evitar Don Repeat Yourself

def detail(request, question_id):
  #Obtener el detalle
  question = get_object_or_404(Question, pk=question_id) #tare el objeto pero si tiene un error ejecuta automáticamente el 404
  return render(request, "polls/detail.html", {
    "question": question
  })


def results(request, question_id):
  question = get_object_or_404(Question, pk = question_id)
  return render(request, "polls/results.html", {
    "question": question
  })


"""

"""Vistas basadas en clases"""
class IndexView(generic.ListView):
  template_name = "polls/index.html"
  context_object_name = "latest_question_list"
  
  def get_queryset(self):
    """Retorna las ultimas 5 respuestas publicadas"""
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
                                   
  

class DetailView(generic.DetailView):
  model = Question
  template_name= "polls/detail.html"
  
  def get_queryset(self):
    #Excluir cualquier pregunta que no han sido publicadas todavía
    return Question.objects.filter(pub_date__lte=timezone.now())
  

class ResultView(generic.DetailView):
  model = Question
  template_name= "polls/results.html"

def vote(request, question_id):
  """Funcionalidad de elección de respuesta"""
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST["choice"])
  except(KeyError, Choice.DoesNotExist):
    return render(request, "polls/detail.html", {
      "question": question,
      "error_message": "No elegiste una respuesta."
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    


def prueba(request):
  return render(request, 'polls/prueba.html', {
    "texto_prueba": 'Este es el texto de prueba'
  })