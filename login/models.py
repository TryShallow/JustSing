from django.db import models

# Create your models here.
class Account(models.Model):
    account_name = models.CharField(max_length = 20)
    phone_number = models.CharField(max_length = 11)
    password = models.CharField(max_length = 20)

    def __str__(self):
        return self.account_name