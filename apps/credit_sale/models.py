from django.db import models


# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    credit = models.IntegerField()

    def __str__(self):
        return self.name


class Operation(models.Model):
    OPERATION = [(0, 'credit_withdrawal'), (1, 'increase_credit')]
    seller = models.ForeignKey(Seller, related_name="operation", on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, default=None, blank=True, null=True)
    operation = models.IntegerField(choices=OPERATION)
    operation_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['operation_time']
