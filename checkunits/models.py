from django.db import models

# Create your models here.
class Unit(models.Model):
    name = models.CharField(max_length=30)
    utype = models.CharField(max_length=30)
    status = models.BooleanField(default=False)

    def __unicode__(self):
        return "{} - {} - Out: {}".format(self.name,
                                          self.utype,
                                          self.status)
