from django.db import models
from klients.models import Klients
from teachers.models import Teachers
# Create your models here.

class Tasks(models.Model):
    task = models.TextField(max_length=100, verbose_name='Задача')
    klient = models.ForeignKey(Klients, related_name='tasks', on_delete=models.CASCADE, null=True, verbose_name='Клиент')
    deadline = models.DateField(verbose_name='Срок выполнения')
    teacher = models.ForeignKey(Teachers, related_name='tasks', on_delete=models.CASCADE, null=True, verbose_name='Ответственный')
    check = models.BooleanField(default=False, verbose_name='Выполнено')


    class Meta:
        verbose_name = ("Задача")
        verbose_name_plural = ("Задачи")

    def __str__(self):
        return self.task