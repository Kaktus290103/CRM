from django.db import models
from services.models import ServiceModel
from phonenumber_field.modelfields import PhoneNumberField

class StatusKlienta(models.Model):
    status = models.TextField(max_length=15, verbose_name='Статус Клиента')
    class Meta:
        verbose_name = 'Статус клиента'
        verbose_name_plural = 'Статус клиента'
    
    def __str__(self):
        return self.status  

class Istochnik(models.Model):
    istochnik = models.TextField(max_length=30, verbose_name='Источник')
    class Meta:
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'
    
    def __str__(self):
        return self.istochnik

# Create your models here.
class Klients(models.Model):
    f_name = models.TextField(max_length=30, verbose_name='Имя')
    s_name = models.TextField(max_length=30, verbose_name='Фамилия')
    servise = models.ForeignKey(ServiceModel, related_name='klienty', on_delete=models.CASCADE, null=True, verbose_name='Услуга')
    town = models.TextField(max_length=30, verbose_name='Город')
    school = models.TextField(max_length=30, verbose_name='Школа')
    telephone = PhoneNumberField(verbose_name='Телефон')
    call = models.BooleanField(default= False, verbose_name='Обзвонить')
    another_inf = models.TextField(max_length=500, verbose_name='Доп. информация')
    status = models.ForeignKey(StatusKlienta, related_name='klienty', on_delete=models.CASCADE, null=True, verbose_name='Статус клиента')
    istochnik = models.ForeignKey(Istochnik, related_name='klienty', on_delete=models.CASCADE, null=True, verbose_name='Источник')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('f_name',)
    
    def __str__(self):
        return self.s_name
        