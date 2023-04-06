from django import forms
from .models import *


class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = "__all__"
