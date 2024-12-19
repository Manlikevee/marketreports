from django.contrib import admin

from .models import Account_opening_Submission, market_data, fx_data

#
# # Register your models here.
admin.site.register(market_data)
admin.site.register(fx_data)
admin.site.register(Account_opening_Submission)
