from django.contrib import admin
from .models import Question,Choice


#Hacer modificable el modelo 
admin.site.register(Question)
admin.site.register(Choice)
