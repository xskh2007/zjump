# coding:utf-8
from django import forms

from dbtool.models import Sqllog,Dblist
'''# "user_id","db_name","sqllog","create_time","status","comments","type"'''

class SqllogForm(forms.ModelForm):

    class Meta:
        model = Sqllog
        ordering = ['-create_time']

        fields = [
            "user_id","user_name","db_name","sqllog","check_mod_rows","real_mod_rows","create_time","status","comments","type"
        ]

class DblistForm(forms.ModelForm):

    class Meta:
        model = Dblist

        fields = [
            "dbname","db_role"
        ]



