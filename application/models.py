from django.db import models

class menu(models.Model):
    rest_name = models.CharField(max_length=50)
    item_name = models.CharField(max_length=50)
    available = models.BooleanField(default=False)



    def __unicode__(self):
<<<<<<< HEAD
        return "%s %s" % (
            self.rest_name,
            self.item_name,
        )
=======
        return self.item_name
>>>>>>> 5cb727255ffb1bbda89b4243baf35058d2ab7ead





