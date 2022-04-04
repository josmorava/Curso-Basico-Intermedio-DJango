from datetime import datetime
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
    
    """was_publish_recently retorna falso para preguntas publicadas con fecha en el futuro"""
    time = timezone.now() + datetime.timdedelta(days=30)
    future_question= Question(question_text="¿Quién es el mejor Course Director de Platzi?",pub_date=time)
    self.assertIs(future_question.was_publish_recently, False)
  