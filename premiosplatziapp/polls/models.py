from django.db import models
from django.utils import timezone

import datetime

"""
Datos de la logica de los modelos de la app polls(encuentas)
"""

class Question(models.Model):
  """Class pregunta del modelo de la tabla questions"""
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField("Date published")
  
  def __str__(self):
    return self.question_text
  
  #Error en los test
  def was_published_recently(self):
    """Si la pregunta fue publicada recientemente"""
    return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
  
  
  
class Choice(models.Model):
  """Class eleccion del modelo de la tabla choises"""
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0) 
  
  def __str__(self):
    return self.choice_text 