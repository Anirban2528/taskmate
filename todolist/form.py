from django import forms
from todolist.models import Todolist

class TaskForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['task','done']
