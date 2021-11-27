from django import forms
from django.forms.widgets import TextInput
from ad.models import Ad, Text
class GetForm(forms.ModelForm):
    get = forms.CharField(max_length=20, label='Получатель')
    class Meta:
        model = Ad
        fields = ('get','email')

class AdForm(forms.ModelForm):
    thema = forms.CharField(max_length=20, label='Тема', required=True)
    class Meta:
        model = Text
        fields = ('thema','text',)



    