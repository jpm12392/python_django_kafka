from django.db import models

# Create your models here.


class Order(models.Model):
    user_id = models.CharField(max_length=100)
    order_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_orders"