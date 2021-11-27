from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
class Text(models.Model):
    thema = models.TextField(max_length=20, verbose_name='Тема', null=True)
    text = models.TextField(max_length=300, verbose_name='Текст отправки', null=True)

class Ad(models.Model):
    get = models.TextField(max_length=100, verbose_name='Получатель', null=True)
    email = models.EmailField(null=True, verbose_name='Email')



    class Meta:
        verbose_name = ("Реклама")
        verbose_name_plural = ("Реклама")

    def __str__(self):
        return self.get
