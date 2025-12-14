from django.db import models

# Create your models here.


class UserOrderNotification(models.Model):
    order_id = models.CharField(max_length=100)
    messages = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_order_notifications'
