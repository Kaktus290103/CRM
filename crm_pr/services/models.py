from django.db import models
from teachers.models import Teachers

class Schedule(models.Model):
    day = models.TextField(max_length=30, verbose_name='День')#Посмотреть нет ли типа для дней недели
    time = models.TextField(max_length=30, verbose_name='Время') #изменить время на соответствующий тип

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'

    def __str__(self):
        return self.day

class TypeService(models.Model):
    type = models.TextField(max_length=15, verbose_name='')

    class Meta:
        verbose_name = 'Вид услуги'
        verbose_name_plural = 'Виды услуги'

    def __str__(self):
        return self.type

# Create your models here.
class ServiceModel(models.Model):
    name = models.TextField(max_length=30, verbose_name='Название')
    type = models.ForeignKey(TypeService, related_name='service', on_delete=models.CASCADE, null=True, verbose_name='Вид услуги')
    teacher = models.ForeignKey(Teachers, related_name='service', on_delete=models.CASCADE, null=True, verbose_name='Преподователь')
    count = models.IntegerField(null=True, verbose_name='Количество клиентов в группе', blank=True)
    max_count = models.IntegerField(null=True, verbose_name='Максимальное количество клиентов в группе')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', blank=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Льготная цена', blank=True)
    # schedule = models.ForeignKey(Schedule, related_name='products', on_delete=models.CASCADE, null=True, verbose_name='Расписание', blank=True)
    
    #добавить расписание
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name






