from django import forms
from tasks.models import Tasks

class TaskForm(forms.ModelForm):
    check = forms.BooleanField(required=False)

    class Meta:
        model = Tasks
        fields = ['check',]
