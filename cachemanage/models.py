from django.db import models

# Create your models here.


class Redislist(models.Model):
    """
    asset modle
        create_time = models.DateTime(default=datetime.now)
    """
    redis_host=models.CharField(max_length=100, blank=True, null=True, verbose_name=u"redis_host")
    redis_role = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"redis_role")


    def __unicode__(self):
        return self.redis_host