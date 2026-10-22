from django.db import models

# Create your models here.
class Loans(models.Model):
    type = models.CharField(max_length=50)
    interest_rate = models.IntegerField()

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'loans'
        verbose_name = 'Loans'
        verbose_name_plural = 'Loans'