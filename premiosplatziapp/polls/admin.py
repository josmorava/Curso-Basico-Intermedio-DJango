from django.contrib import admin
from secretstorage import search_items
from .models import Question,Choice



class ChoiceInline(admin.StackedInline):
  #Agregar la opcion de poner respuestas al poner la pregunta
  model = Choice
  extra = 3
  
  
class QuestionAdmin(admin.ModelAdmin):
  #Clase que personaliza como se ve el modelo Question dentro de Admin
  fields = ["pub_date", "question_text"]
  inlines = [ChoiceInline]
  
  #modificar como se ve la lista del modelo
  list_display = ("question_text", "pub_date", "was_published_recently")
  list_filter = ["pub_date"]
  search_fields= ["question_text"]

#Hacer modificable el modelo dentro de /admin/
admin.site.register(Question, QuestionAdmin)
