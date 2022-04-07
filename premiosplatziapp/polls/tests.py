from urllib import response
from venv import create
from django.urls.base import reverse
import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Question

# Create your tests here.
"""Test para probar el funcionamiento del código
# Modelos
# Vistas
"""

class QuestionModelTest(TestCase):

  """Conjunto de test"""
  
  def test_was_published_recently_with_future_questions(self):
    #Testear las preguntas que están publicadas con fecha en el futuro
    
    """was_published_recently retorna falso para preguntas publicadas con fecha en el futuro"""
    time = timezone.now() + datetime.timedelta(days=30)
    future_question= Question(question_text="¿Quién es el mejor Course Director de Platzi?",pub_date=time)
    self.assertIs(future_question.was_published_recently(), False)
  
  
  
  def test_was_published_recently_with_present_questions(self):
    """was_published_recently retorna true para preguntas publicadas en el presente"""
    time = timezone.now() 
    present_question= Question(question_text="¿Quién es el mejor Course Director de Platzi?",pub_date=time)
    self.assertIs(present_question.was_published_recently(), True)
  
  
  
  def test_was_published_recently_with_past_questions(self):
    """was_published_recently retorna false para preguntas publicadas en el pasado"""
    time= timezone.now() - datetime.timedelta(days=30)
    past_question = Question(question_text="¿Quién es el mejor Course Director de Platzi?",pub_date=time)
    self.assertIs(past_question.was_published_recently(), False)
    

    
def create_question(question_text, days):
  """Crea una pregunta que trae el "question_text"""
  time = timezone.now() + datetime.timedelta(days=days)
  
  return Question.objects.create(question_text=question_text ,pub_date=time)
  
  
  
"""
class QuestionIndexViewTest(TestCase):
  def test_no_questions(self):
    #Si no existe ninguna pregunta, vamos a publicar un mensaje
    response = self.client.get(reverse("polls:index"))
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "No existen encuestas en esta pagina aún.")
    self.assertQuerysetEqual(response.context["latest_question_list"], []) 
  
  def test_future_question(self):
    #Preguntas que tenga una fecha de publicacion en el futuro no deben mostrarse en el index
    create_question("Pregunta del Futuro", days=30)
    response = self.client.get(reverse("polls:index"))
    self.assertContains(response, "No existe ninguna encuesta")
    self.assertQuerysetEqual(response.context["latest_question_list"], [])
    
  def test_past_question(self):
    #Preguntas que tengan una fecha de publicacion en el pasado deben mostarse en la pagina index
    question = create_question("Pregunta del pasado", days=-10)
    response = self.client.get(reverse("polls:index"))
    self.assertQuerysetEqual(response.content["latest_question_list"],[question])

  def test_future_question_and_past_question(self):
    #Si hay preguntas en pasado y futuro, mostrar las del pasado en el index
    past_question = create_question(question_text="Past question", days=-30)
    future_question = create_question(question_text="Future question", days=30)
    response = self.client.get(reverse("polls:index"))
    self.assertQuerysetEqual(
      response.context["latest_question_list"],
      [past_question]
    )
    
  def test_two_past_questions(self):
    #Mostrar en pantalla las preguntas pasadas
    past_question1 = create_question(question_text="Past question 1", days=-30)
    past_question2 = create_question(question_text="Past question 2", days=-40)
    response = self.client.get(reverse("polls:index"))
    self.assertQuerysetEqual(
      response.context["latest_question_list"],
      [past_question1, past_question2]
    )
"""


class QuestionDetailViewTest(TestCase):
  def test_future_question(self):
    #Si un usuario entra a un detalle de una pregunta con pub_date futura debe retornar 404 error
    future_question = create_question(question_text="Future question", days=30)
    url = reverse("polls:detail", args=(future_question.id,))
    response= self.client.get(url)
    self.assertEqual(response.status_code, 404)
  
  def test_past_question(self):
    #si un usuario entra a un detalle de una pregunta con pub_date pasada debe retornar el texto de la pregunta
    past_question = create_question(question_text="Past question", days=-30)
    url = reverse("polls:detail", args=(past_question.id,))
    response= self.client.get(url)
    self.assertContains(response, past_question.question_text)