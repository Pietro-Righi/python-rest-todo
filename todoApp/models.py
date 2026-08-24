from django.db import models

class Todos(models.Model):
    stato = models.BooleanField()
    testo = models.CharField(max_length=200)
    def is_task_done(self):
        return  "Fatto " if self.stato else "Non Fatto "
    def __str__(self):
        return ("{ stato : " + ("Fatto " if self.stato else "Non Fatto ")  + " , testo : " + self.testo + "}")
# Create your models here.
