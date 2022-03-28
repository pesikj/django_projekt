from django.views.generic import CreateView, ListView, TemplateView
import crm.models as models
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = "index.html"

class CompanyCreateView(CreateView):
    model = models.Company
    template_name = "company/create_company.html"
    fields = ["name", "status", "phone_number", "email", "identification_number"]
    success_url = reverse_lazy("index")

