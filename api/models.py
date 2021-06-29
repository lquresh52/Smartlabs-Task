from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='user')
    discount = models.DecimalField(max_digits=9,decimal_places=2)

    def __str__(self):
        return f'{self.user} - {self.discount}'

class Item(models.Model):
    name = models.CharField(max_length=100)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name='order')
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.order} - {self.price}'