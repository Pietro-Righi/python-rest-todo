from django.db import models
from django.utils.text import *

class Todos(models.Model):
    stato = models.BooleanField()
    testo = models.CharField(max_length=200)
    def is_task_done(self):
        return  "Fatto " if self.stato else "Non Fatto "
    def __str__(self):
        return ("{ stato : " + ("Fatto " if self.stato else "Non Fatto ")  + " , testo : " + self.testo + "}")
# Create your models here.


class TextRequest(models.Model):
    language=models.CharField(max_length=20)
    request=models.CharField(max_length=200)
    def getTask(self):
        self.request.replace("INSERISCI" , " ")
