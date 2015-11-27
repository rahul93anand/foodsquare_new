from django.db import models

class menu(models.Model):
    rest_name = models.CharField(max_length=50)
    item_name = models.CharField(max_length=50)
    available = models.BooleanField(default=False)



    def __unicode__(self):

        return "%s %s" % (
            self.rest_name,
            self.item_name
        )






class orderplaced(models.Model):
    username = models.CharField(max_length=50)
    order = models.CharField(max_length=256)
    order_id = models.CharField(max_length=40)
    placed_on = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=30, default="Order Placed")

    def __unicode__(self):

        return "%s %s %s %s %s"  % (
            self.username,
            self.order,
            self.order_id,
            self.placed_on,
            self.status
        )

class verification(models.Model):
    verification_number = models.CharField(max_length=10)
    username = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)
    def __unicode__(self):

        return "%s %s %s "  % (
            self.verification_number,
            self.username,
            self.verified

        )
