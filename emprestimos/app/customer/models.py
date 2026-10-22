from django.db import models

# Create your models here.
class Customer(models.Model):
    age = models.IntegerField()
    cpf = models.CharField(max_length=11)
    name = models.CharField(max_length=255)
    income = models.FloatField(default=0.00)
    location = models.CharField(max_length=2)


    def __str__(self):
        return f'{self.name} | {self.income}'

    class Meta:
        db_table = 'customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
