from django.contrib import admin
import crm.models as models

class CompanyAdmin(admin.ModelAdmin):
    fields = ["name", "phone_number", "email", "address", "status", "identification_number"]
    readonly_fields = ["status", "identification_number"]
    list_display = ["name", "status", "email"]
    list_filter = ["status"]
    search_fields = ["name", "email", "identification_number", "opportunity__description"]

class OpportunityAdmin(admin.ModelAdmin):
    list_display = ["status", "value"]
    list_filter = ["status"]
    search_fields = ["description"]
admin.site.register(models.Opportunity, OpportunityAdmin)

admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.Employee)
