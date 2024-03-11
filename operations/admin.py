from django.contrib import admin
from .models import Operation, Coin, UserBalance


admin.site.register(Operation)
admin.site.register(Coin)
admin.site.register(UserBalance)
