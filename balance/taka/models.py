from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Bank(models.Model):
    bank_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.bank_name

class Balances(models.Model):
    # account_holder = models.ForeignKey(User, on_delete=models.CASCADE)
    userName = models.CharField(max_length=50)
    current_balance = models.IntegerField()
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='banklist')
    
    def __str__(self):
        return self.userName
        # return f'{self.account_holder}'