from django import forms
from services.models import ServiceModel
from teachers.models import Teachers


class ServiceForm(forms.ModelForm):
    name = forms.CharField(max_length=20, label='Название')
    class Meta:
        model = ServiceModel
        fields = ('name','type','teacher','count','max_count','price','sale_price')

class TeachersForm(forms.ModelForm):
    f_name = forms.CharField(max_length=20, label='Имя')
    s_name = forms.CharField(max_length=20, label='Фамилия')
    class Meta:
        model = Teachers
        fields = ('f_name','s_name','time',)
