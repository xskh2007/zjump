# coding: utf-8
from django.db import models
from datetime import *


# Create your models here.
class Env(models.Model):


    old_env = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"旧环境")
    new_env = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"新环境")


    def __unicode__(self):
        return self.new_env


