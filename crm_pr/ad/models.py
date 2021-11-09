from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
class Ad(models.Model):
    school = models.TextField(max_length=100, verbose_name='Школа')
    tag_ad = models.TextField(max_length=100, verbose_name='Вид рекламы')
    count_klients = models.IntegerField(null=True, verbose_name='Количество клиентов')
    email = models.EmailField(null=True, verbose_name='Email')
    telephone = PhoneNumberField(verbose_name='Телефон') 


    class Meta:
        verbose_name = ("Реклама")
        verbose_name_plural = ("Реклама")

    def __str__(self):
        return self.name
