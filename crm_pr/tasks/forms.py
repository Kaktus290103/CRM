from django import forms
from tasks.models import Tasks
from django.forms.widgets import DateInput

class TaskForm(forms.ModelForm):
    task = forms.CharField(max_length=50, label='Задача')
    #deadline = forms.DateField(label='Дедлайн', help_text='dd.mm.yyyy')
    class Meta:
        model = Tasks
        fields = ('task','klient','deadline','teacher',)
        widgets = {
            'deadline': DateInput(attrs={'placeholder': 'dd.mm.yyyy'}),
        }


# class TaskForm(forms.ModelForm):
#     check = forms.BooleanField(required=False)

#     class Meta:
#         model = Tasks
#         fields = ['check',]
