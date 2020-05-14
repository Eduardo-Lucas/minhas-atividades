from django.contrib.auth.models import User
from django.db import models
from django.utils.datetime_safe import date


class Task(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_tarefa = models.DateField(max_length=10, )
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-data_tarefa', 'created')

    def __str__(self):
        return str(self.data_tarefa) + ' - ' + self.title

    def is_late(self):
        if self.data_tarefa < date.today():
            return True
        else:
            return False
