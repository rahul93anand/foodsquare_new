from django.db import models

class menu(models.Model):
    rest_name = models.CharField(max_length=50)
    item_name = models.CharField(max_length=50)
    available = models.BooleanField(default=False)



    def __unicode__(self):
        return self.item_name





