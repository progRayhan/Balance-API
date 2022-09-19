from django.contrib import admin
from .models import Balances, Bank

# Register your models here.
admin.site.register(Balances)
admin.site.register(Bank)