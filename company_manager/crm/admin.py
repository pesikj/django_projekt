from django.contrib import admin
import crm.models as models

admin.site.register(models.Company)
admin.site.register(models.Opportunity)