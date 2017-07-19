# coding:utf-8
from django import forms

from envmanage.models import Env

class EnvForm(forms.ModelForm):

    class Meta:
        model = Env

        fields = [
            "old_env", "new_env"

        ]
