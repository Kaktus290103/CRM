from django import forms
from klients.models import Klients
from services.models import ServiceModel

class KlientForm(forms.ModelForm):
    f_name = forms.CharField(max_length=20, label='Имя')
    s_name = forms.CharField(max_length=20, label='Фамилия')
    town = forms.CharField(max_length=20, label='Город') 
    school = forms.CharField(max_length=5, label='Школа')
    class Meta:
        model = Klients
        fields = ('f_name','s_name','servise','town','school','telephone','call','another_inf','status','istochnik')
