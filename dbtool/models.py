from django.db import models
from datetime import *


# Create your models here.
class Sqllog(models.Model):
    """
    asset modle
        create_time = models.DateTime(default=datetime.now)
    """
    user_id = models.IntegerField(max_length=128, blank=True, null=True, verbose_name=u"user_id")
    user_name = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"user_name")
    db_name = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"db_name")
    sqllog = models.TextField(max_length=2000, blank = True, null = True, verbose_name = u"sqllog")
    create_time=models.DateTimeField(default=datetime.now,blank = True)
    status = models.IntegerField(max_length=20, blank=True, null=True, verbose_name=u"status")
    comments = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"comments")
    type = models.IntegerField(max_length=20, blank=True, null=True, verbose_name=u"type")



    def __unicode__(self):
        return self.user_id


class Dblist(models.Model):
    """
    asset modle
        create_time = models.DateTime(default=datetime.now)
    """
    dbname=models.CharField(max_length=20, blank=True, null=True, verbose_name=u"DB_IP")


    def __unicode__(self):
        return self.dbname