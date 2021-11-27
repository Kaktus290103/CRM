from django.db import models
class Teachers(models.Model):
    f_name = models.TextField(max_length=30, verbose_name='Имя')
    s_name = models.TextField(max_length=30, verbose_name='Фамилия')
    time = models.IntegerField(null=True, verbose_name='Количество часов')

    class Meta:
        verbose_name = "Преподователь"
        verbose_name_plural = "Преподователи"
        
    def __str__(self):
        s = self.f_name + ' ' + self.s_name
        return s

 